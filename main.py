import os
import json
import re
import webbrowser
import logging
import time

from tools import create_folder, write_file

from dotenv import load_dotenv
load_dotenv()

# Optional OpenAI import (may be GROQ-compatible)
try:
    from openai import OpenAI
except Exception:
    OpenAI = None


def get_client():
    """Create and return an OpenAI/Groq-compatible client.

    Raises RuntimeError with actionable message if package is missing.
    """
    if OpenAI is None:
        raise RuntimeError("Missing 'openai' package. Install with: python -m pip install openai")

    api_key = os.environ.get("GROQ_API_KEY") or os.environ.get("OPENAI_API_KEY")
    base_url = os.environ.get("GROQ_BASE_URL", "https://api.groq.com/openai/v1")

    return OpenAI(api_key=api_key, base_url=base_url)

# -------------------------------
# TOOL MAP
# -------------------------------
tool_map = {
    "create_folder": create_folder,
    "write_file": write_file
}

# -------------------------------
# SYSTEM PROMPT
# -------------------------------
system_prompt = """
You are an AI Agent that builds websites step by step.

Rules:
1. Break task into steps
2. Use tools
3. DO NOT generate everything in one step
4. Always return ONLY valid JSON
5. Do NOT add explanation outside JSON

Steps:
START, THINK, TOOL, OBSERVE, OUTPUT

Goal:
Create a website similar to Scaler Academy landing page.

Requirements:
- Header (logo + navbar)
- Hero section (headline + CTA)
- Footer

You MUST create:
- index.html
- style.css
- script.js

Each file must be created in separate TOOL steps.

Tools:
1. create_folder(name)
2. write_file(filename, content)

IMPORTANT: Write files DIRECTLY as:
- write_file("index.html", content)
- write_file("style.css", content)
- write_file("script.js", content)

Do NOT use subfolder names like "website/" in filenames.

Output format:
{
 "step": "START | THINK | TOOL | OBSERVE | OUTPUT",
 "content": "string",
 "tool_name": "string",
 "tool_args": {
   "name": "string",
   "filename": "string",
   "content": "string"
 }
}

Do NOT stop until all files are created.
Return ONLY JSON.
"""

# -------------------------------
# CLI + Agent Loop
# -------------------------------
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def extract_json_objects(text: str):
    """Extract JSON objects from model text.

    Returns a list of parsed JSON objects and an error string (or None).
    Handles:
      - A single JSON object
      - A JSON array of objects
      - Multiple JSON objects concatenated
      - JSON inside triple-backtick blocks
    """
    if not text:
        return None, "empty response"

    decoder = json.JSONDecoder()

    # First try the whole response as JSON (covers single object and arrays).
    stripped = text.strip()
    try:
        obj = json.loads(stripped)
        return obj if isinstance(obj, list) else [obj], None
    except json.JSONDecodeError:
        pass

    # Then try a fenced JSON block if the model wrapped its output.
    code_block = re.search(r"```(?:json)?\n([\s\S]*?)\n```", text)
    if code_block:
        block = code_block.group(1).strip()
        try:
            obj = json.loads(block)
            return obj if isinstance(obj, list) else [obj], None
        except json.JSONDecodeError:
            text = block

    # Finally, scan through concatenated JSON values using raw_decode.
    objects = []
    idx = 0
    length = len(text)
    while idx < length:
        while idx < length and text[idx].isspace():
            idx += 1
        if idx >= length:
            break

        try:
            obj, end = decoder.raw_decode(text, idx)
        except json.JSONDecodeError:
            idx += 1
            continue

        if isinstance(obj, list):
            objects.extend(obj)
        else:
            objects.append(obj)
        idx = end

    if objects:
        return objects, None

    return None, "no JSON found"


def main():
    print("AI Agent CLI (Groq) - type 'exit' to quit")
    print("-" * 40)

    user_input = input(">> ")
    if user_input.lower() == "exit":
        return

    # Ensure output folder exists up front
    os.makedirs("output", exist_ok=True)

    try:
        client = get_client()
    except RuntimeError as e:
        logging.error(str(e))
        return

    # conversation messages stored as list of dicts for clarity
    messages = []

    while True:
        prompt = system_prompt + "\n" + json.dumps(messages, indent=2) + "\nUser: " + user_input

        # call API with a small retry/backoff
        response_text = None
        for attempt in range(1, 4):
            try:
                resp = client.chat.completions.create(
                    model=os.environ.get("AGENT_MODEL", "openai/gpt-oss-20b"),
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.2,
                )

                # Compatible access for returned structure
                choice = resp.choices[0]
                text = getattr(choice.message, "content", None) or choice.text
                response_text = text
                break
            except Exception as e:
                logging.warning(f"API attempt {attempt} failed: {e}")
                time.sleep(attempt * 1.0)

        if response_text is None:
            logging.error("Failed to get response from API after retries.")
            break

        print("\nRAW RESPONSE:\n", response_text)

        items, err = extract_json_objects(response_text)
        if err:
            logging.error("JSON PARSE ERROR: %s", err)
            messages.append({"role": "assistant", "content": response_text})
            continue

        # Process each JSON object in order
        for data in items:
            if not isinstance(data, dict):
                logging.warning("Skipping non-object JSON item: %r", data)
                continue

            messages.append({"role": "assistant", "content": data})

            step = data.get("step")

            if step == "TOOL":
                tool_name = data.get("tool_name")
                tool_args = data.get("tool_args", {})

                if tool_name in tool_map:
                    try:
                        result = tool_map[tool_name](**tool_args)
                    except Exception as e:
                        result = f"Tool execution error: {str(e)}"
                else:
                    result = "Tool not found"

                print("TOOL RESULT:", result)

                # Inform the model about the observation
                messages.append({"role": "system", "content": {"step": "OBSERVE", "content": result}})

                # continue processing next item
                continue

            elif step == "OUTPUT":
                print("\nFINAL OUTPUT:\n", data.get("content"))

                index_path = os.path.abspath(os.path.join("output", "index.html"))
                logging.info("Opening website: %s", index_path)
                try:
                    webbrowser.open(index_path)
                except Exception:
                    logging.warning("Could not open browser automatically.")

                return

            else:
                # START, THINK, OBSERVE or unknown - just continue
                continue


if __name__ == "__main__":
    main()