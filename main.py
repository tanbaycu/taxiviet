from flask import Flask, render_template, redirect, request
import logging
from user_agents import parse as parse_ua

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__, static_folder="app/static", template_folder="app/templates")

def _should_use_mobile_template(user_agent_string: str) -> bool:
    """Detect if user is on mobile or tablet."""
    user_agent = parse_ua(user_agent_string or "")
    return bool(user_agent.is_mobile or user_agent.is_tablet)

@app.route("/")
def index():
    """Redirect to mobile or desktop template."""
    use_mobile = _should_use_mobile_template(request.headers.get("User-Agent", ""))
    return redirect("/mobile.html" if use_mobile else "/index.html")

@app.route("/index.html")
def index_html():
    return render_template("index.html")

@app.route("/mobile.html")
def mobile_html():
    return render_template("mobile.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)