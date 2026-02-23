import bcrypt
from datetime import datetime, timezone
from database import get_users_collection
from pymongo.errors import DuplicateKeyError


def hash_password(password: str) -> str:
    """Hash a password with bcrypt (10 salt rounds). Returns a UTF-8 string."""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt(rounds=10)).decode("utf-8")


def verify_password(password: str, hashed) -> bool:
    """Verify a password against its bcrypt hash."""
    if isinstance(hashed, bytes):
        hashed = hashed.decode("utf-8")
    return bcrypt.checkpw(password.encode("utf-8"), hashed.encode("utf-8"))


def register_user(name: str, email: str, password: str) -> dict:
    """
    Register a new user.
    Returns {"success": True, "user": {...}} or {"success": False, "message": "..."}.
    """
    name = name.strip()
    email = email.strip().lower()

    if not name or not email or not password:
        return {"success": False, "message": "Please fill in all fields."}

    if len(password) < 6:
        return {"success": False, "message": "Password must be at least 6 characters."}

    users = get_users_collection()
    hashed = hash_password(password)

    try:
        result = users.insert_one({
            "name": name,
            "email": email,
            "password": hashed,
            "createdAt": datetime.now(timezone.utc),
        })
        return {
            "success": True,
            "user": {
                "id": str(result.inserted_id),
                "name": name,
                "email": email,
            },
        }
    except DuplicateKeyError:
        return {"success": False, "message": "An account with this email already exists."}
    except Exception as e:
        return {"success": False, "message": f"Server error — {str(e)}"}


def login_user(email: str, password: str) -> dict:
    """
    Login a user by email and password.
    Returns {"success": True, "user": {...}} or {"success": False, "message": "..."}.
    """
    email = email.strip().lower()

    if not email or not password:
        return {"success": False, "message": "Please provide email and password."}

    users = get_users_collection()
    user = users.find_one({"email": email})

    if not user:
        return {"success": False, "message": "Invalid email or password."}

    if not verify_password(password, user["password"]):
        return {"success": False, "message": "Invalid email or password."}

    return {
        "success": True,
        "user": {
            "id": str(user["_id"]),
            "name": user["name"],
            "email": user["email"],
            "createdAt": user.get("createdAt", datetime.now(timezone.utc)),
        },
    }
