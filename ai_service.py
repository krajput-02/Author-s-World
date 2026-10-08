# All Gemini API calls live here.
# ANY problem (bad key, quota, no internet, timeout) becomes AIUnavailable,
# so the app can switch to demo mode.
import os
import json
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()  # reads GEMINI_API_KEY from the .env file
MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")


class AIUnavailable(Exception):
    """Raised when the AI service cannot be used."""


def _ask(prompt, as_json=False):
    key = os.getenv("GEMINI_API_KEY")
    if not key or key == "your_key_here":
        raise AIUnavailable("No API key")
    try:
        client = genai.Client(api_key=key, http_options=types.HttpOptions(timeout=30000))
        config = types.GenerateContentConfig(response_mime_type="application/json") if as_json else None
        response = client.models.generate_content(model=MODEL, contents=prompt, config=config)
        if not response.text:
            raise AIUnavailable("Empty response")
        return response.text
    except AIUnavailable:
        raise
    except Exception as error:  # quota, invalid key, network, timeout...
        raise AIUnavailable(str(error))


def get_tough_sentences(text):
    """Ask Gemini for the 5 hardest sentences, why, and a simpler version."""
    prompt = f"""You are an editor helping an author.
Find the 5 most DIFFICULT sentences in the text below. Do NOT just pick the longest.
Consider: long structure, complex vocabulary, technical words, difficult grammar,
and too many ideas in one sentence.

Return ONLY a JSON list of 5 objects with these keys:
"original" (copy the sentence exactly), "why" (one short reason), "simpler" (easier rewrite, same meaning).

TEXT:
{text}"""
    raw = _ask(prompt, as_json=True)
    try:
        data = json.loads(raw)
        items = data if isinstance(data, list) else data.get("sentences", [])
        result = [
            {k: str(item[k]) for k in ("original", "why", "simpler")}
            for item in items[:5]
        ]
    except (ValueError, KeyError, TypeError, AttributeError):
        raise AIUnavailable("Bad AI response")
    if not result:
        raise AIUnavailable("No sentences returned")
    return result


def generate_blog(text):
    """Ask Gemini for a ~150-word promotional paragraph."""
    prompt = f"""Write an engaging promotional blog paragraph of about 150 words for the chapter below.
Rules:
- Start with an interesting opening line.
- Use easy, natural language.
- Use ONLY information from the chapter. No false facts.
- No exaggerated claims. Do NOT promise or mention any number of readers.
- Return only the paragraph.

CHAPTER:
{text}"""
    return _ask(prompt).strip()
