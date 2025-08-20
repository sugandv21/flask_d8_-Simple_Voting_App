from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder="../frontend")

candidates = {
    "Alice": 0,
    "Bob": 0,
    "Charlie": 0
}

@app.route("/")
def index():
    return render_template("index.html", candidates=candidates)

@app.route("/api/vote", methods=["POST"])
def vote():
    data = request.get_json()
    candidate = data.get("candidate")

    if candidate not in candidates:
        return jsonify({"error": "Invalid candidate"}), 400

    candidates[candidate] += 1
    return jsonify({"message": f"Vote recorded for {candidate}", "results": candidates})

@app.route("/api/results")
def results():
    return jsonify(candidates)

if __name__ == "__main__":
    app.run(debug=True)
