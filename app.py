from flask import Flask, request, jsonify, send_file
from twilio.rest import Client
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Twilio credentials
account_sid = "AC2d1ff15cbc93ae35758549ea64c9a146"
auth_token = "28e781f694ac5e9c0bb5d2c5a98a5026"
twilio_number = "+18287959778"
my_phone = "+919142574197"

client = Client(account_sid, auth_token)

# Serve HTML pages
@app.route('/')
def index():
    return send_file('index.html')

@app.route('/story')
def story():
    return send_file('story.html')

@app.route('/love_letter')
def love_letter():
    return send_file('love_letter.html')

@app.route('/propose')
def propose():
    return send_file('propose.html')

# Serve CSS and JS
@app.route('/style.css')
def style():
    return send_file('style.css')

@app.route('/script.js')
def script():
    return send_file('script.js')

# API for sending answers
@app.route('/send-answer', methods=['POST'])
def send_answer():
    data = request.json
    user_answer = data.get('answer', '').strip()
    if not user_answer:
        return jsonify({'status':'error','message':'Answer cannot be empty'})
    
    try:
        client.messages.create(
            body=f"New Answer: {user_answer}",
            from_=twilio_number,
            to=my_phone
        )
        return jsonify({'status':'success','message':'Answer sent successfully!'})
    except Exception as e:
        return jsonify({'status':'error','message':str(e)})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
