import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()  # .envファイルを読み込む

gemini_API = os.getenv("gemini_API")

genai.configure(api_key=gemini_API)
  # 一般的な環境変数名に修正（小文字→大文字）

model = genai.GenerativeModel("gemini-1.5-flash-latest")
response = model.generate_content("好きなプログラミング言語は？")
print(response.text)