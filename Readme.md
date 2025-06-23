# 📡 Auto Research + Email Automation Agent

# 🤖 Auto Research + Email Automation Agent

An AI-powered LangGraph agent that automates research, summarization, and batch email delivery.  
It fetches academic and general info from Arxiv + Wikipedia, summarizes it via a Groq-hosted open-source LLM (like Gemma-2B), and sends the summary to multiple email addresses via SMTP — all triggered from a simple Flask frontend.

---

## 🚀 Key Features

- 🔍 Search Wikipedia + Arxiv automatically
- ✍️ Summarize using Groq API + OSS models like Gemma
- 📧 Email summaries to multiple recipients from `emails.csv`
- 🌐 Clean Flask web interface
- ✅ Powered by LangGraph (stateful AI workflows)

---

## 📦 Installation

```bash
pip install -r requirements.txt


## 📁 Folder Structure
auto-research-email-automation-agent/
├── app.py                 # Flask backend
├── automation_agent.pkl   # Compiled LangGraph workflow
├── emails.csv             # Email recipient list
├── templates/
│   ├── index.html         # Input form
│   └── result.html        # Output summary
├── requirements.txt       # Python dependencies
├── README.md




## ✅ requirements.txt

flask
dill
pandas
langchain
langgraph
openai
wikipedia
arxiv


## ✅   AI Agent Workflow

| 🔢 Step | 🧠 Task Description                    | 🛠️ Tool/Library Used                     | 🎯 Output of Step                         |
|--------|----------------------------------------|------------------------------------------|-------------------------------------------|
| 1️⃣     | User submits query via frontend        | `Flask` (form in `index.html`)           | Query string passed to backend             |
| 2️⃣     | Fetch general information              | `WikipediaQueryRun` (via LangChain)      | Raw text result from Wikipedia             |
| 3️⃣     | Fetch academic papers                  | `ArxivAPIWrapper` (LangChain)            | Paper abstracts/text from Arxiv            |
| 4️⃣     | Combine Wiki + Arxiv                   | Python string formatting                 | Combined input text for summarization      |
| 5️⃣     | Summarize research                     | `Groq API` + LLM (e.g., `Gemma-2B`)      | Concise summary (LLM-generated)            |
| 6️⃣     | Send summary to all emails in CSV      | `smtplib.SMTP_SSL` (Email via Gmail)     | Sends summary email to all recipients      |
| 7️⃣     | Return confirmation to user            | `Flask` (`result.html`)                  | Webpage with summary + delivery status     |




📤 Email Automation
Emails are sent using smtplib.SMTP_SSL() (Gmail SMTP by default)

You must use a valid Gmail App Password

All emails from emails.csv will receive the same summarized research content


🧾 Example CSV Format

email
person1@example.com
person2@example.com


📬 SMTP Notes
Replace credentials in send_email() with your Gmail & app password

Use an environment variable or .env for security in production