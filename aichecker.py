import openai  # openai>=1.x
from dotenv import load_dotenv
import os

load_dotenv()  # .envファイルを読み込む
openai_api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=openai_api_key)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "好きなプログラミング言語は？"}]
)
print(response.choices[0].message.content)