from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def repair(code):
    prompt = f"""You're an expert Python developer. Fix the following code and return the corrected version only:

{code}
"""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that fixes Python code."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            max_tokens=800,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"# Error calling model: {str(e)}"
