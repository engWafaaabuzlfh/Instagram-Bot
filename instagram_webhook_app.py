#https://developers.facebook.com/docs/messenger-platform/instagram/features/send-message
#https://developers.facebook.com/docs/messenger-platform/webhooks
from flask import Flask, request, redirect, url_for, render_template, jsonify
from werkzeug.utils import secure_filename
import os
import requests
import threading
from PIL import Image
import io
from gemini_pil import genaiImagesProccessing, genaiTextProccessing
ALLOWED_EXTENSIONS = {'txt'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


app = Flask(__name__)

VERIFY_TOKEN = 'DEFAULT_VALUE'
PAGE_ACCESS_TOKEN = 'DEFAULT_VALUE'

HISTORY = {}
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        token_sent = request.args.get('hub.verify_token')
        if token_sent == VERIFY_TOKEN:
            return request.args.get('hub.challenge')
        return 'Invalid verification token'

    elif request.method == 'POST':
        output = request.get_json()
        threads = []
        for entry in output.get('entry', []):
            for messaging_event in entry.get('messaging', []):
                if 'message' in messaging_event:
                    sender_id = messaging_event['sender']['id']
                    message_text = messaging_event['message'].get('text')
                    attachments = messaging_event['message'].get('attachments', [])
                    if message_text:
                        thread = threading.Thread(target=handle_message, args=(sender_id, message_text, attachments))
                        thread.start()
                        threads.append(thread)
        for thread in threads:
            thread.join()
        return "Message Processed"

def handle_message(sender_id, message_text, attachments):
    if sender_id not in HISTORY:
        HISTORY[sender_id] = []
    if message_text:
        HISTORY[sender_id].append({
            "role": "user",
            "parts": [message_text],
        })

    if attachments:
        for attachment in attachments:
            if attachment['type'] == 'image':
                image_url = attachment['payload']['url']
                url = requests.get(image_url)
                img = Image.open(io.BytesIO(url.content))
                try:
                    response_genai = genaiImagesProccessing(img=img, text=message_text)
                    sender_message(sender_id, response_genai)
                    HISTORY[sender_id].append({
                            "role": "model",
                            "parts": [response_genai],
                             })
                except:
                    sender_message(sender_id, "عذرا منك عزيزي هل يمكنك معاودة ارسال الصورة لانه لم يتم تحميلها بالشكل الصحيح، وشكرا جزيلا")
                
                
    if message_text and (attachment == []):
        response = genaiTextProccessing(text=message_text, history=HISTORY[sender_id])
        HISTORY[sender_id].append({
            "role": "model",
            "parts": [response],
        })
        sender_message(sender_id, response)

def sender_message(recipient_id, message_text):
    url = 'https://graph.facebook.com/v20.0/me/messages'
    params = {
        'access_token': PAGE_ACCESS_TOKEN
    }
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        'recipient': {'id': recipient_id},
        'message': {'text': message_text}
    }
    response = requests.post(url, params=params, headers=headers, json=data)
    if response.status_code != 200:
        print('Failed to send message:', response.status_code, response.text)

@app.route('/')
def index():
    return render_template('upload_panel.html')

@app.route('/send_message', methods=['POST'])
def send_message_from_html():
    data = request.get_json()
    user_message = data['message']
    response_text = "This is a response to your message: " + user_message
    return jsonify({'response': response_text})

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        content = file.read()

        # Overwrite the content of an existing file
        with open('data.txt', 'wb') as existing_file:
            existing_file.write(content)
        return 'File successfully uploaded'
    else:
        return 'File not allowed'

if __name__ == '__main__':
    app.run(port=5000)

