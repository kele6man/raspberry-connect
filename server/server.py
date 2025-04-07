from flask import Flask, jsonify, request

app = Flask(__name__)

# Тук ще се пази какво съдържание да се покаже
content_data = {
    "device_001": {
        "type": "image",
        "url": "https://example.com/poster.jpg"
    },
    "device_002": {
        "type": "video",
        "url": "https://example.com/ad.mp4"
    }
}

@app.route('/get_content', methods=['POST'])
def get_content():
    data = request.json
    device_id = data.get("device_id")
    
    if device_id in content_data:
        return jsonify(content_data[device_id])
    else:
        return jsonify({"type": "none", "message": "No content found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
