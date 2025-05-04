from flask import Blueprint, jsonify, render_template, request
from .calculator import calculate_emissions, load_data

bp = Blueprint("main", __name__)

@bp.route("/")
def home():
    df = load_data()
    return render_template("index.html", tables=[df.to_html(classes='data')])

@bp.route("/api/emissions", methods=["POST"])
def get_emissions():
    data = request.json
    emissions = calculate_emissions(data["mode"], data["distance"])
    return jsonify({"emissions_kg": emissions})