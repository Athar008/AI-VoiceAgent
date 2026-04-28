# AI Voice Chatbot

A Python/Flask chatbot powered by Claude AI with text-to-speech output.

## Project structure

```
ai-voice-chatbot/
├── app.py                  # Flask backend (Python)
├── templates/
│   └── index.html          # Frontend UI (HTML + CSS)
├── requirements.txt        # Python dependencies
├── Procfile                # For Render.com deployment
├── .env                    # Your API key (never commit this)
└── .gitignore
```

## Run locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Add your API key to `.env`:
   ```
   ANTHROPIC_API_KEY=sk-ant-your-key-here
   ```

3. Start the server:
   ```bash
   python app.py
   ```

4. Open your browser at: http://localhost:5000

## Deploy free on Render.com

1. Push this project to GitHub
2. Go to https://render.com and sign up free
3. Click "New" → "Web Service"
4. Connect your GitHub repo
5. Set these settings:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
6. Add environment variable:
   - Key: `ANTHROPIC_API_KEY`
   - Value: your API key
7. Click Deploy → your app is live in ~2 minutes

## Notes

- Voice input (mic) requires Chrome or Edge
- Text-to-speech uses the browser's built-in engine (free)
- Uses Claude Haiku — fast and cheap (~$0.001 per message)
