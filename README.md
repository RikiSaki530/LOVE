# LOVELOVEcheckerくん






## ファイル構成
LOVE/                                # プロジェクトルート
├── app/                             # アプリケーション本体
│   ├── __init__.py                  # Flaskアプリ初期化
│   ├── config.py                    # 環境設定（Firebase／OpenAIキー読み込み等）
│   ├── routes/                      # ルーティング（Blueprintごとに分割）
│   │   ├── __init__.py
│   │   ├── main.py                  # トップページ・診断開始
│   │   ├── survey.py                # アンケート入力フォーム
│   │   └── result.py                # 結果表示・アドバイス
│   ├── models/                      # ドメインロジック
│   │   └── evaluation.py            # 名前画数・星座・血液型・AI評価の統合スコア計算
│   ├── services/                    # 外部APIラッパー／ユーティリティ
│   │   ├── firestore_client.py      # Firestore操作
│   │   ├── openai_client.py         # OpenAI API呼び出し
│   │   └── scoring.py               # 重み付けルール・ランダム要素
│   ├── static/                      # 静的ファイル
│   │   ├── css/
│   │   │   └── main.css
│   │   ├── js/
│   │   │   └── main.js
│   │   └── images/                  # アイコンや背景画像
│   └── templates/                   # HTMLテンプレート
│       ├── base.html                # 共通レイアウト
│       ├── survey.html              # アンケート画面
│       ├── result.html              # 診断結果画面
│       └── error.html               # エラー表示
│
├── tests/                           # テストコード
│   ├── test_routes.py               # ルーティングテスト
│   ├── test_evaluation.py           # スコア計算ロジックの単体テスト
│   └── test_services.py             # Firestore/OpenAI呼び出しのモックテスト
│
├── docs/                            # ドキュメント
│   ├── wireframes/                  # 画面遷移図・ワイヤーフレーム
│   └── er_diagram.svg               # ER図（Firestore構造イメージ）
│
├── .env                             # 環境変数（APIキー等：Git管理外）
├── requirements.txt                 # Python依存ライブラリ
├── README.md                        # 概要・セットアップ手順・ER図解説
└──.gitignore                        # Git管理外ファイル設定