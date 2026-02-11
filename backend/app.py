from flask import Flask, request, jsonify
from flask_cors import CORS
from analyzer import analyze_incident, run_ml_assistant

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "AI Incident Root Cause Analyzer Backend is running"


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json

    # -----------------------------
    # Build incident object
    # -----------------------------
    incident = {
        "cpu": int(data.get("cpu", 0)),
        "memory": int(data.get("memory", 0)),
        "error": data.get("error", ""),
        "recent_deployment": bool(data.get("recent_deployment", False))
    }

    # -----------------------------
    # Rule-based analysis
    # -----------------------------
    rule_result = analyze_incident(incident)

    # -----------------------------
    # ML-assisted analysis
    # -----------------------------
    ml_result = run_ml_assistant(incident)

    # -----------------------------
    # ⭐ FINAL MERGED RESPONSE
    # -----------------------------
    return jsonify({
        "confidence": rule_result.get("confidence", "Low"),
        "root_causes": rule_result.get("root_causes", []),
        "explanation": rule_result.get("explanation", ""),
        "recommended_actions": rule_result.get("recommended_actions", []),

        # ML outputs
        "ml_prediction": ml_result.get("ml_prediction", ""),
        "ml_explanation": ml_result.get("ml_explanation", "")
    })


if __name__ == "__main__":
    app.run(debug=True)
