from flask import Blueprint, request, jsonify
from services.user_service import create_user, get_user_by_id

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    try:
        user = create_user(data["username"], data["email"], data["password"])
        return jsonify({"id": user.id, "username": user.username, "email": user.email}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
