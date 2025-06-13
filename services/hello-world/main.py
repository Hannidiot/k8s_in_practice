from flask import Flask, jsonify
import uuid
import datetime
import os

app = Flask(__name__)

# Generate a random server ID when the service starts
SERVER_ID = str(uuid.uuid4())

@app.route('/hello')
def hello():
    # Generate a random GUID as request ID
    request_id = str(uuid.uuid4())
    
    # Get current timestamp
    current_time = datetime.datetime.now().isoformat()
    
    return jsonify({
        'requestID': request_id,
        'serverID': SERVER_ID,
        'time': current_time
    })

@app.route('/')
def root():
    return jsonify({
        'message': 'Hello World Service',
        'endpoints': ['/hello']
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)