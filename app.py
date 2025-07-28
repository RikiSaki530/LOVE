from flask import Flask, render_template, request, jsonify
from app.services.scoring import record_answer  # 今回は services 配下のモジュールなのでこのまま
from app.services.scoring import get_total_score  # Firestoreに保存する関数
from app.services.openai_client import chat_with_gemini  # Firestoreにメッセージを保存する関数

app = Flask(__name__, template_folder='app/templates', static_folder='app/static')


# ルーティングの設定

from flask import redirect, url_for

@app.route('/')
def index():
    # ルート（/）にアクセスがあったら /start にリダイレクトする例
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


@app.route('/result')
def result():
    return render_template('result.html')




# 問題をFirestoreに保存するためのエンドポイント 
@app.route('/submit_survey', methods=['POST'])
def submit_survey():
    # 複数回答を受け取る（配列で取得）
    question_ids = request.form.getlist('question_id[]')
    scores = []
    # 送られてきたquestion_idの数だけscoreも拾う
    for i in range(len(question_ids)):
        # 例: score[0], score[1], ... で取得
        score = request.form.get(f'score[{i}]')
        scores.append(score)
        # Firestoreに保存
        record_answer(question_ids[i], int(score))

    return jsonify({'success': True, 'message': '保存しました！'})

@app.route('/submit_message', methods=['POST'])
def submit_message():
    message = request.form.get('message_box')
    if not message:
        return jsonify({'success': False, 'message': '入力がありません'})
    
    score, advice = chat_with_gemini(message)
    enquate_score = get_total_score()
    total_score = enquate_score + score

    # ここでresult.htmlに値を渡してページ遷移
    return render_template('result.html', total_score=total_score, advice=advice)




if __name__ == "__main__":
    app.run(debug=True)  # 必要ならport=5000やhost="0.0.0.0"も指定可