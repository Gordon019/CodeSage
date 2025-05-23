import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def analyze(code):
    prompt = f"""You are an expert Python code analyst.

Analyze the following Python code and summarize what it does, listing any defined functions and their purposes.

Only provide the analysis and function summaries. Avoid code repetition.

CODE:
\"\"\"
{code}
\"\"\"
"""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You analyze and summarize Python code structure."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=500,
        )
        return [response.choices[0].message.content]
    except Exception as e:
        return [f"Error during analysis: {str(e)}"]
