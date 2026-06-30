import hashlib
import os
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {"txt", "pdf", "png", "jpg", "jpeg", "docx", "xlsx"}

def compute_checksum(file_path: str) -> str:
    """Compute SHA-256 checksum of a file."""
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

def allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def sanitize_filename(filename: str) -> str:
    return secure_filename(filename)
