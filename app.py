from flask import Flask, render_template, request, jsonify
from app.services.scoring import record_answer  # 今回は services 配下のモジュールなのでこのまま

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

if __name__ == "__main__":
    app.run(debug=True)  # 必要ならport=5000やhost="0.0.0.0"も指定可


# 問題をFirestoreに保存するためのエンドポイント 
@app.route('/submit_survey', methods=['POST'])
def submit_survey():
    question_id = request.form.get('question_id')
    score_value = request.form.get('personality_type')  # ラジオボタンのname属性に対応

    # Firebaseに保存
    record_answer(question_id, int(score_value))
    return jsonify({'success': True, 'message': '保存しました！'})

