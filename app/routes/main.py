# app/routes/main.py

from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('start.html')  # 例: スタートボタン付きトップ画面
