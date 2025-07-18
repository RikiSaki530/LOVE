# app/routes/survey.py

from flask import Blueprint, render_template, request, redirect, url_for

survey_bp = Blueprint('survey', __name__)

@survey_bp.route('/survey', methods=['GET', 'POST'])
def survey():
    if request.method == 'POST':
        # フォームの回答をセッションやクエリなどで渡す（簡略化例）
        answers = request.form.getlist('q')
        return redirect(url_for('result.result', score=sum(map(int, answers))))
    return render_template('survey.html')
