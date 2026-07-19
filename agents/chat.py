from tools.question_router import is_simple_question
from agents.pandas_agent import pandas_agent
from tools.llm import ask_llm


def chat_with_data(state, question):

    if is_simple_question(question):

        answer = pandas_agent(state, question)

        if answer:
            return answer

    df = state.get("cleaned_dataset")
    summary = state.get("summary")
    analysis = state.get("analysis")

    prompt = f"""
You are a Senior Data Scientist.

Dataset Summary:
{summary}

Statistics:
{analysis['statistics']}

Correlation:
{analysis['correlation']}

First 20 rows:
{df.head(20).to_markdown(index=False)}

User Question:
{question}

Answer ONLY from the uploaded dataset.
Be concise and professional.
"""

    return ask_llm(prompt)