# 🧠 UI Agent Framework

**An AI-driven UI automation framework built with Python and Selenium — designed to evolve into a self-healing, intelligent testing agent.**

---

## 🚀 Overview

`UI Agent Framework` is an open-source automation engine that bridges **traditional Selenium testing** with **next-generation AI capabilities**.  
It provides a dynamic, scenario-based automation layer where browser actions are executed from structured JSON files — forming the foundation for intelligent, self-healing test systems.

This framework is part of a larger initiative to demonstrate how **AI can understand, generate, and heal UI automation tasks** with minimal human input.

---

## ✨ Key Features

- **🧩 JSON-based scenario execution:**  
  Define browser actions in JSON, and let the agent execute them step by step.

- **🧭 Intelligent browser control:**  
  Uses Selenium WebDriver to navigate, interact, and validate UI elements.

- **📸 Automatic screenshot capture:**  
  Captures snapshots for each executed step for easy debugging and reporting.

- **📊 Modular design:**  
  Easily extendable for HTML reporting, error recovery, and AI-generated test steps.

- **🔄 Foundation for self-healing automation:**  
  Upcoming versions will integrate natural language understanding and AI-powered locator healing.

---

## 🧱 Architecture Overview

```text
┌─────────────────────────────┐
│         User Input           │
│ (JSON scenario / AI prompt)  │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│     Scenario Executor        │
│  (Parses and runs actions)   │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│     Browser Controller       │
│   (Selenium WebDriver)       │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│   Screenshot & Reporting     │
│ (Logs, screenshots, reports) │
└─────────────────────────────┘


⚙️ Setup & Installation
Requirements
Python 3.9+

Google Chrome (or another supported browser)

ChromeDriver (matching your browser version)

Installation Steps
Clone the repository:

bash
Copy code
git clone https://github.com/<your-username>/ui-agent-framework.git
cd ui-agent-framework

Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the agent:

bash
Copy code
python main.py
🧪 Example Scenario (JSON)
Create a file named scenarios.json and add this example:

json
Copy code
{
  "steps": [
    {"action": "open_url", "target": "https://www.google.com"},
    {"action": "type", "target": "input[name='q']", "value": "OpenAI"},
    {"action": "click", "target": "input[name='btnK']"}
  ]
}
Then update config.json to point to this scenario file and run the agent.

🧩 Roadmap
Version	Feature	Status
v0.1	JSON-based scenario executor (Selenium)	✅ Complete
v0.2	HTML reporting & visual logs	⏳ In development
v0.3	AI-driven step generation (LLM integration)	⏳ Planned
v0.4	Self-healing locators	⏳ Planned

🧠 Vision
The UI Agent Framework aims to demonstrate the transition from scripted test automation to autonomous, self-healing AI agents — a key innovation area in the evolution of software testing.

By combining automation engineering with generative AI, this project explores how test agents can:

Understand natural language test goals,

Generate executable steps, and

Automatically repair broken locators or workflows.

👨‍💻 Author
Saddam Ali Khan
Sr. Software QA Engineer | AI Automation Enthusiast
United Kingdom

🔗 LinkedIn • GitHub • Medium

💬 Contributions & Discussions
Contributions, discussions, and research collaborations are welcome.
Feel free to open issues, share improvements, or connect regarding AI in testing automation.