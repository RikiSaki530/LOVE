import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()  # .envファイルを読み込む


genai.configure(api_key=os.getenv("gemini_API"))  # 一般的な環境変数名に修正（小文字→大文字ならなお良い）
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-1.5-pro")  # "gemini-pro" か "gemini-1.5-pro" など推奨

def chat_with_gemini(prompt_str: str):
    print("[DEBUG] chat_with_gemini() called with prompt:", prompt_str)  # ←入口
    gemini_prompt = """
    "あなたはLOVELOVEチェッカーくんの恋愛マスターです。"
    "入力された恋愛エピソードから相手との関係性を30点満点でスコア化し、簡潔なアドバイスを出力してください。"
    "出力は**必ずPythonの辞書や文章形式ではなく、厳密なJSON**（ダブルクォートのみ）で、"
    '{"score": 数値, "advice": "アドバイス"} の形で返してください。'
    """

    all_prompts = gemini_prompt + prompt_str

    try:
        model = genai.GenerativeModel(GEMINI_MODEL)
        response = model.generate_content(all_prompts)
        # GeminiのAPIレスポンスは .text で取得
        result_json = response.text
        result = json.loads(result_json)
        score = result.get('score')
        advice = result.get('advice')
        print("[DEBUG] score:", score, "advice:", advice)
        return score, advice

    except Exception as e:
        import traceback
        traceback.print_exc()
        return 0, f"Gemini API call failed: {e}"
