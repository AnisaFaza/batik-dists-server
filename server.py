from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from PIL import Image
import io

app = Flask(__name__)
CORS(app)  # penting supaya Unity boleh akses

def compute_dists(img1, img2):
    """
    SEMENTARA: dummy score
    nanti bisa diganti DISTS asli
    """
    return 0.85

@app.route("/compare", methods=["POST"])
def compare():
    data = request.json

    ref_url = data.get("refImageUrl")
    user_url = data.get("userImageUrl")

    if not ref_url or not user_url:
        return jsonify({"error": "URL gambar tidak lengkap"}), 400

    # download gambar
    r1 = requests.get(ref_url)
    r2 = requests.get(user_url)

    img1 = Image.open(io.BytesIO(r1.content)).convert("RGB")
    img2 = Image.open(io.BytesIO(r2.content)).convert("RGB")

    score = compute_dists(img1, img2)

    return jsonify({
        "score": float(score),
        "metric": "DISTS"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
