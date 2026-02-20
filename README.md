# Instagram Bot (Flask + Webhook)

A sample Instagram bot project that uses a `Flask` webhook, with basic examples for working with the Meta Graph API.

## Files (After Renaming)

- `instagram_webhook_app.py`: Main app (webhook handling, incoming message processing, and text file upload endpoint).
- `fetch_facebook_pages.py`: Example script to fetch connected pages/accounts via Graph API.
- `instagram_messaging_examples.py`: Example script for fetching conversations and sending messages.
- `gemini_pil.py`: Gemini image/text processing helper used by the webhook app.
- `templates/upload_panel.html`: Simple HTML upload panel.

## Requirements

- Python 3.9+
- Python packages:
- `flask`
- `requests`
- `pillow`
- `google-generativeai`

Install dependencies:

```bash
pip install flask requests pillow google-generativeai
```

## Configure Sensitive Values

Update these values in `instagram_webhook_app.py`:

- `VERIFY_TOKEN`
- `PAGE_ACCESS_TOKEN`

Update API/token placeholders in:

- `fetch_facebook_pages.py`
- `instagram_messaging_examples.py`
- `gemini_pil.py`

## Run

Start the main app with:

```bash
python instagram_webhook_app.py
```

By default, it runs on port `5000`.

## Notes

- Current placeholder values are set to `DEFAULT_VALUE`.
- For production, move all tokens/keys to environment variables.
