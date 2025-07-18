# app/routes/result.py

from flask import Blueprint, render_template, request

result_bp = Blueprint('result', __name__)

@result_bp.route('/result')
def result():
    try:
        score = int(request.args.get('score', 0))
    except:
        score = 0

    if score >= 10:
        message = "💖 これは…かなり脈ありかも！？"
    elif score >= 6:
        message = "😊 良い感じ！"
    elif score >= 3:
        message = "🤔 まだ様子見かも…"
    else:
        message = "😶 今のところは難しいかも"

    return render_template('result.html', score=score, message=message)
