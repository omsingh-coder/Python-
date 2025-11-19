from flask import Flask, request, jsonify
from twilio.rest import Client
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from frontend

# Twilio credentials (all as strings!)
account_sid = "AC2d1ff15cbc93ae35758549ea64c9a146"
auth_token = "28e781f694ac5e9c0bb5d2c5a98a5026"
twilio_number = "+18287959778"
my_phone = "+919142574197"

client = Client(account_sid, auth_token)

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