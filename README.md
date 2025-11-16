# AI専門家相談アプリ

LangChainとOpenAI GPTを使用したStreamlitアプリです。

## 機能

- 4種類の専門家AI（医療、IT、ビジネス、教育）から選択可能
- ラジオボタンで専門家を切り替え
- 入力フォームから質問を送信
- AIからの回答を画面に表示

## ローカル実行方法

1. 依存パッケージをインストール:
```bash
pip install -r requirements.txt
```

2. `.env`ファイルまたは`stream.env`ファイルにOpenAI APIキーを設定:
```
OPENAI_API_KEY=your-api-key-here
```

3. アプリを起動:
```bash
streamlit run app.py
```

## デプロイ

### Streamlit Community Cloudへのデプロイ手順

1. GitHubにリポジトリを作成し、コードをプッシュ
   - `.gitignore`により`.env`と`stream.env`は除外されます

2. Streamlit Community Cloudでアプリをデプロイ
   - Pythonバージョン: **3.11**

3. **重要: Secretsの設定**
   
   デプロイ後、アプリの設定画面で以下の手順でAPIキーを設定してください:
   
   - アプリのダッシュボードから「Settings」→「Secrets」を開く
   - 以下の形式でOpenAI APIキーを入力:
   
   ```toml
   OPENAI_API_KEY = "your-api-key-here"
   ```
   
   - 「Save」をクリック
   
   ⚠️ **注意**: `.env`ファイルはGitHubにアップロードされないため、Streamlit Community Cloud上ではSecrets機能でAPIキーを設定する必要があります。
