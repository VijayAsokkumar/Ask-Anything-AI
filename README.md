```markdown
# 🧠 Ask Anything – AI Agent with Think / Reason / Act

A lightweight AI Agent that simulates human-like decision-making using a three-stage process: **Think → Reason → Act**. It takes user queries, performs web search, analyzes web content, and generates structured answers — powered by a **local LLaMA 3 model**.

---

## 🚀 Features

- 🧠 **Think**: Analyzes the user's intent and identifies required information
- 🧩 **Reason**: Plans the steps to answer the question logically
- 🎯 **Act**: Searches the web, processes content, and generates structured answers
- ✅ Runs **completely offline** (LLM) with internet only for web search
- 🖼️ Optional UI using **Streamlit**

---

## 📂 Project Structure

```

ai-agent-workshop/
├── models/                        # Place your GGUF model file here
│   └── mistral-7b-instruct-v0.1.Q5_K_M.gguf
├── agent/
│   └── ai\_agent.py               # Core agent logic (Think / Reason / Act)
├── frontend/
│   └── app.py                    # Streamlit UI
└── README.md

````

---

## ⚙️ Requirements

- Python 3.9+
- [mistral-7b-instruct-v0.1.Q5_K_M.gguf GGUF model](https://huggingface.co/TheBloke/*)
- Internet (for web search only)

### 🧪 Install Dependencies

```bash
pip install streamlit llama-cpp-python duckduckgo-search beautifulsoup4 requests
````

---

## 🤖 Usage

### 1. Download and place the `.gguf` model in the `models/` folder

Recommended:

* `mistral-7b-instruct-v0.1.Q5_K_M.gguf`

### 2. Run the Streamlit app

```bash
cd frontend
streamlit run app.py
```

---

## 🧠 Example Query

> **User**: “Find me the best laptops under ₹30,000”

The agent will:

1. Analyze what kind of data is needed
2. Plan how to get it
3. Search online and generate a final structured list with specs

---

## 📸 Sample Output

```
💭 Think
→ User is asking for laptop recommendations under a budget.
→ Need product listings, specs like RAM/CPU/Storage.
→ Source: E-commerce + review websites.

🧩 Reason
→ Step 1: Define specs
→ Step 2: Search laptops under ₹30K
→ Step 3: Compare and return top 3

🎯 Act
• HP Pavilion x360 – Intel i3, 4GB RAM, 512GB SSD
• Lenovo V15 – AMD Ryzen 3, FHD screen, 256GB SSD
• Acer Aspire Lite – 8GB DDR5, MS Office included
```

---

## 🔧 Customizing It

You can easily extend the agent to:

* Use tools (e.g. calculator, local DB)
* Store memory across multiple queries
* Integrate APIs for structured product info

---

## 📝 Coming Soon

✔️ Blog post: [How I Built This Agent with LLaMA 2](https://medium.com/@vijayjun89/ask-anything-with-my-ai-agent-can-it-find-the-best-laptop-under-30-000-158e95172913)
🎥 YouTube Video: “My AI Agent Thinks Before It Answers”
💡 Next version: memory + multi-turn conversations

---

## 📜 License

MIT License. You can fork, modify, or reuse with credits.

---

Built with 💻 by [Vijay Asokkumar](https://github.com/VijayAsokkuma) – follow for more AI agent experiments!

```

---

Let me know if you want:
- This converted to a real GitHub repo with upload instructions
- Or want to include Medium/blog/youtube links once they’re live 💪
```
