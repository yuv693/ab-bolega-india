import os
from flask import Flask, request, jsonify, send_file

app = Flask(__name__)

@app.route('/')
def home():
    return send_file('index.html')

@app.route('/book', methods=['POST'])
def book_ticket():
    data = request.json
    irctc_id = data.get('irctc_id')
    train_no = data.get('train_no')
    passenger_name = data.get('name')
    age = data.get('age')

    if not irctc_id:
        return jsonify({"status": "error", "message": "IRCTC User ID is required for booking!"})

    return jsonify({
        "status": "success",
        "message": f"Ticket booked successfully via IRCTC ID: {irctc_id} for train {train_no}!",
        "passenger": passenger_name,
        "age": age,
        "fare": "₹1150"
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
