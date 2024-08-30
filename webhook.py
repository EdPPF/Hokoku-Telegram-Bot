import os
import requests
from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

TELEGRAM_TOKEN = os.getenv('BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('GROUP_CHAT')  # ID do grupo

def send_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': text
    }
    requests.post(url, data=payload)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    # Supondo que o webhook manda informações da atualização da planilha
    sheet_update_info = data.get('sheet_update_info')

    message = f"Planilha atualizada: {sheet_update_info}"
    send_message(message)

    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(port=5000)
