from flask import Flask, jsonify, request, render_template, redirect, url_for

app = Flask(__name__)

# Временно "база данни" в паметта
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

@app.route('/')
def index():
    return render_template("index.html", devices=content_data)

@app.route('/edit/<device_id>', methods=["GET", "POST"])
def edit(device_id):
    if request.method == "POST":
        content_type = request.form["type"]
        url = request.form["url"]
        content_data[device_id] = {
            "type": content_type,
            "url": url
        }
        return redirect(url_for('index'))
    return render_template("edit.html", device_id=device_id, data=content_data.get(device_id, {}))

@app.route('/add', methods=["POST"])
def add():
    device_id = request.form["device_id"]
    content_data[device_id] = {
        "type": "none",
        "url": ""
    }
    return redirect(url_for('edit', device_id=device_id))

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
