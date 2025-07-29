import openai
import os
from dotenv import load_dotenv
import json

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI(api_key=OPENAI_API_KEY)

def chat_with_openai(prompt_str: str, timeout: int = 30):
    system_prompt = (
    "あなたはLOVELOVEチェッカーくんの恋愛マスターです。"
    "入力された恋愛エピソードから相手との関係性を30点満点でスコア化し、簡潔なアドバイスを出力してください。"
    "出力は**必ずPythonの辞書や文章形式ではなく、厳密なJSON**（ダブルクォートのみ）で、"
    '{"score": 数値, "advice": "アドバイス"} の形で返してください。'
    )
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt_str}
            ],
            max_tokens=256,
            temperature=0.7,
            timeout=timeout
        )
        # 新APIではこうやって取得
        result_json = response.choices[0].message.content
        result = json.loads(result_json)
        score = result.get("score")
        advice = result.get("advice")
        return score, advice
    except Exception as e:
        print("[ERROR]", e)
        return 0, "OpenAI APIエラー: " + str(e)