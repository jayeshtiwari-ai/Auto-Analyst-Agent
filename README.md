# 🤖 Auto Analyst Agent

> **An AI-powered automated data analytics platform that profiles datasets, recommends data cleaning, performs statistical analysis, generates visualizations, produces AI-driven business insights, and enables natural language interaction with your data.**

---

## 📌 Overview

Auto Analyst Agent is an intelligent data analytics application that automates the complete analytics workflow. Users can upload a CSV dataset, receive AI-powered cleaning recommendations, analyze the data, generate visualizations, obtain business insights, and interact with the dataset using natural language.

This project demonstrates the integration of AI with traditional data analytics to reduce manual effort and accelerate data-driven decision-making.

---

## ✨ Features

- 📂 Upload CSV datasets
- 📊 Automatic dataset profiling
- 🤖 AI-powered data cleaning recommendations
- 🧹 One-click dataset cleaning
- 📈 Statistical analysis
- 📉 Automatic visualization generation
- 💡 AI-generated business insights
- 💬 Chat with your dataset using natural language
- 📥 Download cleaned dataset

---

## 🖥️ Application Workflow

```text
Upload Dataset
      │
      ▼
Dataset Profiling
      │
      ▼
AI Cleaning Advisor
      │
      ▼
Clean Dataset
      │
      ▼
Statistical Analysis
      │
      ▼
Visualization Generation
      │
      ▼
AI Business Insights
      │
      ▼
Chat with Your Dataset
```

---

## 🛠️ Tech Stack

### Frontend
- Streamlit

### Backend
- Python

### Data Processing
- Pandas
- NumPy

### Machine Learning & Analytics
- Scikit-learn

### Visualization
- Matplotlib
- Seaborn

### AI Integration
- Groq API
- OpenAI Python SDK

### Utilities
- Python Dotenv
- ReportLab

---

## 📁 Project Structure

```text
Auto-Analyst-Agent/
│
├── agents/
│   ├── analyzer.py
│   ├── chat.py
│   ├── cleaner.py
│   ├── cleaning_advisor.py
│   ├── insight.py
│   ├── planner.py
│   ├── profiler.py
│   ├── visualizer.py
│
├── tools/
│   ├── helper.py
│   ├── llm.py
│   ├── loader.py
│   ├── preprocessing.py
│   ├── question_router.py
│   ├── state.py
│   ├── statistics.py
│   ├── summary_builder.py
│
├── outputs/
├── data/
├── streamlit_app.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/jayeshtiwari-ai/Auto-Analyst-Agent.git

cd Auto-Analyst-Agent
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file.

```env
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run Application

```bash
streamlit run streamlit_app.py
```

---

## 💬 Example Questions

You can ask:

- What is the highest salary?
- What is the average age?
- Which department has the most employees?
- Are there any missing values?
- Show business insights.
- Summarize this dataset.
- Which columns are highly correlated?
- What recommendations would you give?

---

## 📸 Screenshots

Add screenshots here after uploading them.

Example:

```
screenshots/
│
├── dashboard.png
├── analysis.png
├── chat.png
└── insights.png
```

---

## 🔮 Future Improvements

- PDF report generation
- Interactive Plotly visualizations
- Advanced AI planning agent
- Multi-file analysis
- Database connectivity
- Excel support
- Export AI reports

---

## 📚 Learning Outcomes

This project demonstrates practical experience with:

- Artificial Intelligence Integration
- Data Analytics
- Data Cleaning
- Statistical Analysis
- Data Visualization
- Prompt Engineering
- Streamlit Development
- LLM Integration
- Python Development
- Software Design

---

## 👨‍💻 Author

**Jayesh Tiwari**

LinkedIn: www.linkedin.com/in/jayesh-tiwari-949609293

GitHub: https://github.com/jayeshtiwari-ai

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
