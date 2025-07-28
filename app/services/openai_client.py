import os
import json
import google.generativeai as genai


genai.configure(api_key=os.getenv("gemini_API"))  # ←環境変数名を確認！
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-flash")

def chat_with_gemini(prompt_str: str, timeout: int = 30):
    print("[DEBUG] chat_with_gemini() called with prompt:", prompt_str)  # ←入口
    gemini_prompt = """
    あなたはLOVELOVEチェッカーくんの恋愛マスターです。
    ユーザからの入力に対して、評価してください。
    点数は、0~30 内でつける。
    相手にポジティブな印象を与えるアドバイスを一言添える。
    出力は
    {
        "score": 点数,
        "advice": アドバイス
    }
    の形式でJSONで出力してください。
    """

    all_prompts = gemini_prompt + prompt_str

    try:
        response = genai.chat.create(
            model=GEMINI_MODEL,
            messages=[{"role": "user", "content": all_prompts}]
        )
        # 最新APIのレスポンス例：response['choices'][0]['message']['content']
        # 必ずprint(response)で構造を確認するのがおすすめ
        result_json = response['choices'][0]['message']['content']
        result = json.loads(result_json)
        score = result.get('score')
        advice = result.get('advice')
        print("[DEBUG] score:", score, "advice:", advice)  # ←出口
        return score, advice

    except Exception as e:
        import traceback
        traceback.print_exc()
        return None, f"Gemini API call failed: {e}"
