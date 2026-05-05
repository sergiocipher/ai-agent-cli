# 🚀 AI Agent CLI Tool (Scaler Website Clone)

## 📌 Overview

This project is a **conversational CLI-based AI agent** that can generate a working website using natural language instructions.

The agent follows a reasoning loop (START → THINK → TOOL → OBSERVE → OUTPUT) and uses tools to create files step-by-step instead of generating everything at once.

The final output is a **fully working website (HTML, CSS, JS)** that resembles the Scaler Academy landing page.

---

## 🎯 Features

* 💬 Conversational CLI interface
* 🧠 Multi-step reasoning agent loop
* 🛠 Tool-based execution (file creation)
* 🌐 Generates real website files
* 🚀 Automatically opens output in browser
* ⚡ Powered by Groq API (fast LLM inference)

---

## 🏗️ Project Structure

```
ai-agent-cli/
│
├── main.py          # Agent loop + CLI interface
├── tools.py         # File system tools
├── output/          # Generated website files
│
├── .env             # API key (not pushed)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone Repository

```
git clone <your-repo-link>
cd ai-agent-cli
```

### 2. Create Virtual Environment

```
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

## 🔑 Setup API Key (Groq)

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run the Project

```
python main.py
```

Then type:

```
clone scaler academy website
```

---

## 🔁 Agent Workflow

The agent follows a structured loop:

1. **START** → Understand task
2. **THINK** → Break into steps
3. **TOOL** → Execute action (create files)
4. **OBSERVE** → Read tool result
5. **OUTPUT** → Final response

---

## 🛠 Tools Used

* `create_folder(name)` → Creates directories
* `write_file(filename, content)` → Writes files

---

## 🌐 Output

Generated files:

```
output/
├── index.html
├── style.css
└── script.js
```

The website includes:

* Header
* Hero Section
* Footer

---

## 🎥 Demo

👉 Add your YouTube demo link here

---

## 🧠 Technologies Used

* Python
* Groq API (OpenAI-compatible)
* LLM (LLaMA / GPT-OSS)
* CLI-based interaction

---

## ⚠️ Notes

* The UI is generated dynamically and may vary slightly
* Focus is on agent reasoning and tool execution
* API key is required for execution

---

## 🚀 Future Improvements

* Better UI styling (closer to Scaler)
* More tools (edit file, preview changes)
* Streaming responses
* Error recovery improvements

---

## 👨‍💻 Author

Your Name
