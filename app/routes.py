from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/run_code", methods=["POST"])
def run_code():
    data = request.json
    code = data.get("code", "")

    try:
        # Execute the Python code in a subprocess for isolation
        result = subprocess.run(
            ["python3", "-c", code],
            capture_output=True,
            text=True,
            timeout=5  # Timeout for safety
        )
        output = result.stdout if result.returncode == 0 else result.stderr
        return jsonify({"success": True, "output": output})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
