# 🚀 AI Agent CLI Tool 

[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue?style=flat-square&logo=python)](https://www.python.org/)
[![Groq API](https://img.shields.io/badge/Powered%20by-Groq-orange?style=flat-square)](https://groq.com/)
[![OpenAI SDK](https://img.shields.io/badge/OpenAI-Compatible_API-black?style=flat-square)](https://platform.openai.com/docs/)
[![CLI Agent](https://img.shields.io/badge/AI-Agent-purple?style=flat-square)]()
[![HTML5](https://img.shields.io/badge/HTML5-Markup-E34F26?style=flat-square&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-Styling-1572B6?style=flat-square&logo=css3)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-Frontend-F7DF1E?style=flat-square&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Status: Active](https://img.shields.io/badge/Status-Active-success?style=flat-square)]()

---

# 📌 Overview

AI Agent CLI Tool is a **conversational terminal-based AI agent** capable of generating a complete landing page website using natural language instructions.

The agent follows a **multi-step reasoning loop** similar to Cursor or Windsurf:

```text
START → THINK → TOOL → OBSERVE → OUTPUT
```

Instead of generating everything in one shot, the agent:
- reasons step-by-step
- executes tools
- creates real files
- generates a working website

The final output includes:
- ✅ Header
- ✅ Hero Section
- ✅ Footer
- ✅ HTML/CSS/JS files
- ✅ Browser preview

---

# ✨ Features

| Feature | Description |
|---|---|
| 💬 Conversational CLI | Interact with the agent directly in terminal |
| 🧠 Multi-Step Reasoning | Agent thinks before taking actions |
| 🛠 Tool Calling System | Uses tools to create folders and files |
| 🌐 Website Generation | Generates HTML, CSS, and JavaScript |
| ⚡ Groq Powered | Fast inference using Groq API |
| 🚀 Auto Browser Open | Opens generated website automatically |
| 📁 Real File Output | Produces actual frontend files |

---

# 🏗️ Architecture

```text
User Input
    ↓
CLI Agent
    ↓
Reasoning Loop
    ↓
Groq LLM
    ↓
Tool Execution
    ↓
HTML/CSS/JS Generation
    ↓
Browser Output
```

---

# 📂 Project Structure

```text
ai-agent-cli/
│
├── main.py              # Main agent loop
├── tools.py             # Tool implementations
│
├── output/              # Generated website files
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── .env                 # API key
├── .gitignore
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone <your-repo-link>
cd ai-agent-cli
```

---

## 2️⃣ Create Virtual Environment

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Setup

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

---

# ▶️ Running the Project

```bash
python main.py
```

Example prompt:

```text
clone scaler academy website
```

---

# 🔁 Agent Workflow

| Step | Purpose |
|---|---|
| START | Understand user request |
| THINK | Break task into smaller steps |
| TOOL | Execute tool action |
| OBSERVE | Analyze tool output |
| OUTPUT | Final completion response |

---

# 🛠 Tools Used

| Tool | Function |
|---|---|
| `create_folder(name)` | Creates folders |
| `write_file(filename, content)` | Writes files to output directory |

---

# 🌐 Generated Output

```text
output/
├── index.html
├── style.css
└── script.js
```

The generated website includes:
- ✅ Responsive Header
- ✅ Hero Section
- ✅ CTA Button
- ✅ Footer
- ✅ Modern Styling

---

# 🧠 Tech Stack

| Technology | Usage |
|---|---|
| Python | Core backend logic |
| Groq API | LLM inference |
| OpenAI SDK | API integration |
| HTML/CSS/JS | Website generation |
| CLI | User interaction |

---

# 📸 Demo

## 🎥 YouTube Demo
> [YouTube Demo — Watch on YouTube](https://youtu.be/4C-Mz3K5cMg)

---

# 🚀 Example CLI Interaction

```text
>> clone scaler academy website

START → Understanding request

THINK → Need to create folder structure

TOOL → create_folder("output")

OBSERVE → Folder created

THINK → Generate HTML

TOOL → write_file("index.html")

THINK → Generate CSS

TOOL → write_file("style.css")

THINK → Generate JavaScript

TOOL → write_file("script.js")

OUTPUT → Website generated successfully
```

---

# ⚠️ Important Notes

| Note | Description |
|---|---|
| API Key Required | Groq API key is needed |
| Dynamic Output | UI may vary slightly per generation |
| Multi-Step System | Agent intentionally avoids one-shot generation |

---

# 🔮 Future Improvements

- 🎨 Better UI similarity to Scaler
- 🧠 More advanced reasoning
- 🛠 Additional tools (edit/read files)
- ⚡ Streaming responses
- 🌙 Better CLI visuals
- 📦 Docker support

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Somyajit Saha**

---
