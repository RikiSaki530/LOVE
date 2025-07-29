from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from app.services.scoring import record_answer
from app.services.openai_client import chat_with_gemini  # Gemini用
from app.services.gemini import chat_with_openai         # OpenAI用

app = Flask(__name__, template_folder='app/templates', static_folder='app/static')
app.secret_key = 'my_secret_dev_key_2025_07_29'

# ここで合計スコアをグローバルに管理
total_score = 0

@app.route('/')
def index():
    return redirect(url_for('start'))

@app.route('/start')
def start():
    return render_template('start.html')

@app.route('/enquete1')
def enquete1():
    return render_template('enquete1.html')

@app.route('/enquete2')
def enquete2():
    return render_template('enquete2.html')

@app.route('/enquete3')
def enquete3():
    return render_template('enquete3.html')

# 設問回答の保存・加算
@app.route('/submit_survey', methods=['POST'])
def submit_survey():
    global total_score
    question_ids = request.form.getlist('question_id[]')
    scores = []
    for i in range(len(question_ids)):
        score = request.form.get(f'score[{i}]')
        scores.append(score)
        record_answer(question_ids[i], int(score))
        total_score += int(score)
    return jsonify({'success': True, 'message': '保存しました！'})

# メッセージ送信＋AIスコア加算
@app.route('/submit_message', methods=['POST'])
def submit_message():
    global total_score
    message = request.form.get('message_box')
    if not message:
        return jsonify({'success': False, 'message': '入力がありません'})
    score, advice = chat_with_openai(message)
    if score is not None:
        total_score += score
    session['score'] = total_score
    session['advice'] = advice
    return jsonify({'success': True, 'redirect': '/result'})

@app.route('/result')
def result():
    score = session.get('score', '')
    advice = session.get('advice', '')
    return render_template('result.html', total_score=score, advice=advice)

if __name__ == "__main__":
    app.run(debug=True)