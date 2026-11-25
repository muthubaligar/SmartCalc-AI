SMARTCALC AI — SETUP GUIDE
===========================

WHAT'S INCLUDED
- index.html: responsive calculator website
- server.py: small secure backend for AI requests
- manifest.webmanifest + sw.js: installable PWA support
- .env.example: environment variable template

IMPORTANT
The calculator, converters, statistics, history and basic math workspace work in the browser.
The AI tutor and photo-question solving need an OpenAI API key, an internet connection,
and the Python backend. API usage may incur charges. ChatGPT subscriptions and API
billing are separate. Never put your API key in index.html or share it publicly.

RUN ON YOUR LENOVO WINDOWS LAPTOP
1. Install Python 3.11 or newer from https://www.python.org/downloads/
2. Extract this ZIP into a folder, for example Desktop\SmartCalcAI.
3. Open that folder in File Explorer. Click the address bar, type cmd, press Enter.
4. Run:
       py -m venv .venv
       .venv\Scripts\activate
       pip install -r requirements.txt
5. Set your API key in PowerShell (replace with your own key):
       $env:OPENAI_API_KEY="YOUR_SECRET_KEY"
   Optional model selection:
       $env:OPENAI_MODEL="gpt-5.5"
6. Start the website:
       uvicorn server:app --reload
7. Open Chrome and visit:
       http://127.0.0.1:8000

AI STATUS
The header says "AI needs setup" until OPENAI_API_KEY is set in the terminal
and the server is restarted. If you only want the non-AI calculator, open
index.html directly, but the AI backend will not work from a file:// URL.

INSTALL AS AN ANDROID APP
For a proper installable PWA, the website must be hosted on HTTPS (or localhost).
Deploy the folder to a hosting service that supports Python/FastAPI and configure
OPENAI_API_KEY as a server-side environment variable in its dashboard.
Then open the HTTPS website in Chrome on Android > menu (⋮) > Install app
(or Add to Home screen). Do not expose your API key in frontend files.

SECURITY / PRODUCTION NOTES
This is a student starter project. Before public release, add user authentication,
rate limiting, request-size limits, abuse protection, privacy policy and monitoring.
The included server does not implement accounts or per-user quotas. Keep the API
key private and monitor API usage. Photo uploads are sent to the configured AI
provider when you ask the AI to solve them.

MATH NOTES
- Scientific calculator uses Math.js from a CDN, so its first load needs internet.
- Trigonometric functions use radians.
- Statistics shown are population variance and population standard deviation.
- Numerical definite integration uses Simpson's rule.
- This is an educational assistant, not a certified engineering calculator.
