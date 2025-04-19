# AI Tagging App

## Local Setup

1. `python3 -m venv venv && source venv/bin/activate`
2. `pip install -r requirements.txt`
3. Create `.env` with your OAuth keys (see `app.py` placeholders).
4. `flask run --host 0.0.0.0`

## Docker

```bash
docker build -t ai-tagging-app .
docker run -p 5000:5000 ai-tagging-app
```
