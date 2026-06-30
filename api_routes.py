from flask import Blueprint, request, jsonify, abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import File, User
from utils import compute_checksum, allowed_file, sanitize_filename
from app import db
import os

file_routes = Blueprint("files", __name__, url_prefix="/api/files")

@file_routes.route("/", methods=["GET"])
@jwt_required()
def list_files():
    user_id = get_jwt_identity()
    files = File.query.filter_by(user_id=user_id, is_deleted=False).all()
    return jsonify([{
        "id": f.id,
        "filename": f.filename,
        "size_bytes": f.size_bytes,
        "checksum": f.checksum,
        "uploaded_at": f.uploaded_at.isoformat()
    } for f in files]), 200

@file_routes.route("/<int:file_id>", methods=["DELETE"])
@jwt_required()
def delete_file(file_id: int):
    user_id = get_jwt_identity()
    f = File.query.filter_by(id=file_id, user_id=user_id).first_or_404()
    f.is_deleted = True
    db.session.commit()
    return jsonify({"message": "File deleted"}), 200
