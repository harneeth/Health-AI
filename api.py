from flask import Flask, request, jsonify
from flask_cors import CORS
from process import main

app = Flask(__name__)

CORS(app)

@app.route('/api', methods=["POST"])
def process_data():
    data = request.json
    fresult = process_function(data)
    return jsonify(fresult)

def process_function(fdata):
    result = main(fdata)
    formattedresult = {'identified_disease': result}

    return formattedresult

if __name__ == '__main__':
    app.run(port=5000)
