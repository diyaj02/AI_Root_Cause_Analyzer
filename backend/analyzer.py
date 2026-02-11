# ================================
# AI Incident Root Cause Analyzer
# FINAL VERSION (Enhanced)
# ================================

import warnings
from sklearn.exceptions import ConvergenceWarning
from sklearn.linear_model import LogisticRegression
import numpy as np

warnings.filterwarnings("ignore", category=ConvergenceWarning)

# ------------------------------------------------
#  RULE-BASED SINGLE INCIDENT ANALYZER
# ------------------------------------------------
def analyze_incident(incident):
    root_causes = []
    explanations = []
    score = 0

    # Weights for confidence scoring
    weights = {
        "Bad deployment causing CPU spike": 3,
        "Possible memory leak leading to timeouts": 2,
        "Overall resource exhaustion": 2
    }

    cpu = incident.get("cpu", 0)
    memory = incident.get("memory", 0)
    error = incident.get("error", "")
    recent_deployment = incident.get("recent_deployment", False)

    # Rule 1: Bad deployment
    if cpu > 85 and recent_deployment:
        cause = "Bad deployment causing CPU spike"
        root_causes.append(cause)
        explanations.append(
            "CPU usage is critically high shortly after a recent deployment."
        )
        score += weights[cause]

    # Rule 2: Memory leak
    if memory > 80 and error == "TimeoutException":
        cause = "Possible memory leak leading to timeouts"
        root_causes.append(cause)
        explanations.append(
            "High memory usage combined with timeout errors suggests a memory leak."
        )
        score += weights[cause]

    # Rule 3: Resource exhaustion
    if cpu > 90 and memory > 85:
        cause = "Overall resource exhaustion"
        root_causes.append(cause)
        explanations.append(
            "CPU and memory are both extremely high, indicating resource exhaustion."
        )
        score += weights[cause]

    # ------------------------------------------------
    # If nothing detected
    # ------------------------------------------------
    if not root_causes:
        return {
            "root_causes": [],
            "confidence": "Low",
            "explanation": "No strong failure patterns detected.",
            "recommended_actions": []
        }

    # ------------------------------------------------
    # Confidence from weighted score
    # ------------------------------------------------
    if score <= 2:
        confidence = "Low"
    elif score <= 4:
        confidence = "Medium"
    else:
        confidence = "High"

    # ------------------------------------------------
    # ⭐ Recommended Actions Generator (NEW)
    # ------------------------------------------------
    actions = []

    for cause in root_causes:
        if "deployment" in cause.lower():
            actions.append("Rollback recent deployment")
            actions.append("Restart affected service")

        if "memory" in cause.lower():
            actions.append("Check memory allocation")
            actions.append("Scale memory resources")

        if "resource exhaustion" in cause.lower():
            actions.append("Scale CPU and memory resources")
            actions.append("Enable autoscaling or optimize workload")

    return {
        "root_causes": root_causes,
        "confidence": confidence,
        "explanation": " ".join(explanations),
        "score": score,
        "recommended_actions": actions
    }


# ------------------------------------------------
#  INCIDENT HISTORY ANALYZER
# ------------------------------------------------
def analyze_incident_history(incidents):
    root_cause_frequency = {}

    for incident in incidents:
        result = analyze_incident(incident)
        for cause in result["root_causes"]:
            root_cause_frequency[cause] = root_cause_frequency.get(cause, 0) + 1

    if not root_cause_frequency:
        return {
            "most_common_issue": "None",
            "occurrences": 0,
            "confidence": "Low"
        }

    most_common_cause = max(
        root_cause_frequency,
        key=root_cause_frequency.get
    )

    occurrences = root_cause_frequency[most_common_cause]
    confidence = "High" if occurrences >= 3 else "Medium"

    return {
        "most_common_issue": most_common_cause,
        "occurrences": occurrences,
        "confidence": confidence
    }


# ------------------------------------------------
#  HUMAN-READABLE SUMMARY FORMATTER
# ------------------------------------------------
def print_history_summary(history_result):
    print("\n===== INCIDENT HISTORY ANALYSIS SUMMARY =====")
    print(f"Most Common Issue : {history_result['most_common_issue']}")
    print(f"Occurrences       : {history_result['occurrences']}")
    print(f"Overall Confidence: {history_result['confidence']}")

    print("\nSystem Insight:")
    if history_result["confidence"] == "High":
        print(
            "This issue appears repeatedly across incidents and is very likely the primary root cause."
        )
    elif history_result["confidence"] == "Medium":
        print(
            "This issue has occurred multiple times and should be investigated further."
        )
    else:
        print(
            "No strong recurring issue detected from incident history."
        )


# ------------------------------------------------
#  ML-ASSISTED ROOT CAUSE SUGGESTION
# ------------------------------------------------
class MLRootCauseAssistant:
    def __init__(self):
        self.model = LogisticRegression(max_iter=1000)
        self.label_map = {
            0: "Normal",
            1: "Bad Deployment",
            2: "Memory Leak",
            3: "Resource Exhaustion"
        }

    def train(self):
        # Simulated training data
        X = np.array([
            [90, 85, 1, 1],
            [88, 80, 1, 0],
            [95, 92, 1, 1],
            [70, 40, 0, 0],
            [60, 85, 1, 0],
            [92, 88, 0, 1]
        ])
        y = np.array([1, 2, 3, 0, 2, 1])
        self.model.fit(X, y)

    def predict(self, incident):
        cpu = incident.get("cpu", 0)
        memory = incident.get("memory", 0)
        error = 1 if incident.get("error") == "TimeoutException" else 0
        deployment = 1 if incident.get("recent_deployment") else 0

        prediction = self.model.predict([[cpu, memory, error, deployment]])[0]
        return self.label_map[prediction]


# ------------------------------------------------
# ⭐ ML Assistant Wrapper (ENHANCED)
# ------------------------------------------------
def run_ml_assistant(incident):
    ml = MLRootCauseAssistant()
    ml.train()

    prediction = ml.predict(incident)

    explanation = (
        f"ML model detected patterns similar to '{prediction}' "
        f"based on CPU, memory, error signals, and deployment activity."
    )

    return {
        "ml_prediction": prediction,
        "ml_explanation": explanation
    }
