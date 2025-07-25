import os
import json
import google.generativeai as genai

# Configure Gemini API client
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-flash")


def chat_with_gemini(prompt_str: str, timeout: int = 30) -> dict:
    """
    Sends the prompt string to Google Gemini via the Python API client and returns the parsed JSON response.

    Args:
        prompt_str (str): The input prompt to send to Gemini.
        timeout (int): Unused for API client, kept for signature consistency.

    Returns:
        dict: Parsed response from Gemini API, or an error dict on failure.
    """
    gemini_prompt = """
    あなたはLOVELOVEチェッカーくんの恋愛マスターです。
    ユーザからの入力に対して、評価してください。
    評価は以下の通りにします。
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
            prompt=all_prompts
        )
        # Extract score and advice from the JSON response
        score = response.get("score")
        advice = response.get("advice")
        return score, advice
    
    except Exception as e:
        return None, f"Gemini API call failed: {e}"
