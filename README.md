# 🧠 AI-Powered Documentation Question Answering Agent

This project is a terminal-based AI assistant that answers user questions based on help documentation from websites like `help.zluri.com` or `help.slack.com`. It uses semantic search and a large language model (LLM) to generate accurate answers, with source references when available.

---

## 📌 Features

- ✅ Crawl and parse help center websites
- ✅ Extract and clean documentation content
- ✅ Embed content using sentence-transformers
- ✅ Store embeddings in a FAISS vector database
- ✅ Accept user queries via CLI
- ✅ Retrieve relevant chunks using semantic search
- ✅ Generate answers with OpenAI GPT-4
- ✅ Cite documentation sources
- ✅ Gracefully handle unanswered questions
- ✅ Docker-ready deployment

---

## 🏗️ Project Structure

ai_qa_agent/
├── main.py # Entry point for CLI
├── crawler.py # Recursively crawls help site pages
├── parser.py # Extracts and cleans HTML content
├── embedder.py # Embeds and indexes content with FAISS
├── retriever.py # Finds relevant chunks from the index
├── answerer.py # Generates answers using OpenAI
├── requirements.txt # Python dependencies
├── .env.example # Template for OpenAI API key
├── Dockerfile # Container setup
├── README.md # Project documentation
└── tests/
└── test_sample.py # Unit tests

yaml
Copy
Edit

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai_qa_agent.git
cd ai_qa_agent
2. Set Up Environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
3. Configure API Key
Create a .env file from the example:

bash
Copy
Edit
cp .env.example .env
Then paste your OpenAI key in .env:

ini
Copy
Edit
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx
💡 Usage Example
Run the agent with a URL and a question:

bash
Copy
Edit
python main.py --url https://help.zluri.com --question "Does Zluri support Slack integration?"
Sample Output:

bash
Copy
Edit
✅ Answer:
Yes, Zluri supports Slack integration. You can enable it via the integrations section of the admin dashboard.
(Source: https://help.zluri.com/slack-integration)
🧪 Testing
bash
Copy
Edit
pytest tests/
Includes sample test cases for expected answers and system behavior.

🐳 Docker (Optional)
To build and run the project in Docker:

bash
Copy
Edit
docker build -t ai_qa_agent .
docker run --env-file .env ai_qa_agent --url https://help.example.com --question "How to enable 2FA?"
📈 Design Decisions
Chose FAISS for fast local vector search

Used all-MiniLM-L6-v2 model for balanced speed/accuracy

Modular code for flexibility (e.g., switch to FastAPI later)

Clear separation of crawling, parsing, embedding, QA logic

🛠️ Known Limitations
Only supports HTML documentation

No pagination or rate-limit handling for large sites

Currently CLI-only (no web UI yet)

🔮 Future Improvements
Add support for PDF, Markdown, and API docs

Web API via FastAPI or Flask

Confidence scoring in answers

Multi-source embedding

Better session memory for follow-ups

📬 Submission Instructions
✅ Code: Private GitHub repo

✅ Include test cases, README, and documentation

✅ Share access with cvp@c4scale.com

✅ Optional: Attach a 5-minute demo video

👤 Author
[priya]
Email: [priyaiyyanar02@gmail.com]
GitHub: [github.com/nancyriya]
