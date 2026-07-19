from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return jsonify({
        "project": "MarketMind AI",
        "message": "Intelligent Market Research Assistant API is Running"
    })


@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.get_json()

    company = data.get("company", "")

    if company == "":
        return jsonify({
            "error": "Company name is required."
        }), 400

    response = {
        "company": company,

        "market_trend": "Growing Market",

        "competitors": [
            "Competitor A",
            "Competitor B",
            "Competitor C"
        ],

        "customer_sentiment": "Positive",

        "prediction": "Market demand is expected to increase over the next 6 months.",

        "recommendation": "Invest in innovation, customer engagement, and digital marketing."
    }

    return jsonify(response)


@app.route("/health")
def health():
    return jsonify({
        "status": "Running"
    })


if __name__ == "__main__":
    app.run(debug=True)
