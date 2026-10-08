# AuthorAI – Smart Readability & Content Assistant

**What it does:** Paste a chapter → get readability score, 5 toughest sentences (with simpler versions), and a ~150-word promo blog.

**Tech:** Python, Streamlit, textstat, Gemini API, python-dotenv.

## Install
    pip install -r requirements.txt

## Get a Gemini API key
1. Open https://aistudio.google.com/apikey
2. Sign in with Google → "Create API key" → copy it.

## Add the key
Create a file named `.env` in this folder:

    GEMINI_API_KEY=your_key_here

(`.env` is in `.gitignore`, so it is never uploaded.)

## Run
    streamlit run app.py

## Demo / Fallback mode
If the AI fails (quota, bad key, no internet, timeout), the app shows
"AI service is temporarily unavailable. Demo mode is being used." and loads sample
results from `demo_data.py`, clearly labelled **Demo / Fallback Mode**.
Readability numbers always work because textstat runs offline.

## College demo tips
1. Click **Use sample chapter** → **Analyze Chapter**.
2. Show the cards, score bar, and 5 tough sentences.
3. Click **Generate 150-Word Blog** and the copy icon.
4. Show the demo mode by removing the key from `.env` and running again.
5. Say clearly: the blog helps interest, it does not guarantee readers.
