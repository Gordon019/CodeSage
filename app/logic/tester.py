from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def generate_tests(code):
    prompt = f"""
You are an expert Python developer. The following is valid Python code.

Write pytest-style unit tests for any defined functions. Only return test function code.

Code:
\"\"\"
{code}
\"\"\"
"""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You write high-quality unit tests for Python code."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            max_tokens=600,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"# Error generating tests: {str(e)}"