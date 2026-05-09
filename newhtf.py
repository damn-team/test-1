from flask import Flask, render_template, request, jsonify
from mitre.mapper import get_intents, resolve_intent
from recon.passive import recon_checklist
from core.validator import validate_domain
from recon.google import google_dorks
from flask import redirect, url_for



app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template("dashboard.html", intents=get_intents())

@app.route("/mitre")
def mitre_view():
    return redirect(url_for("dashboard"))


@app.route("/api/intent", methods=["POST"])
def intent_api():
    data = request.json
    intent_key = data.get("intent")
    domain = data.get("domain")

    if not validate_domain(domain):
        return jsonify({"error": "Invalid domain"}), 400

    intent = resolve_intent(intent_key)
    if not intent:
        return jsonify({"error": "Unknown intent"}), 400

    plan = [
        recon_checklist(t)
        for t in intent["techniques"]
    ]

    dorks = google_dorks(domain, intent_key)

    return jsonify({
        "domain": domain,
        "goal": intent["label"],
        "description": intent["description"],
        "plan": plan,
        "google_dorks": dorks,
        "note": "Google dorks are provided as links. Manual execution recommended for OPSEC."
    })

if __name__ == "__main__":
    app.run(port=5000)
