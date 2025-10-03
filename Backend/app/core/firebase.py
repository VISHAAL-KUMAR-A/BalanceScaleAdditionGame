import firebase_admin
from firebase_admin import credentials, auth as firebase_auth
from app.core.config import settings
import json


def initialize_firebase():
    """Initialize Firebase Admin SDK"""
    if not firebase_admin._apps:
        # Parse the private key (handle escaped newlines)
        private_key = settings.FIREBASE_PRIVATE_KEY.replace('\\n', '\n')

        cred_dict = {
            "type": "service_account",
            "project_id": settings.FIREBASE_PROJECT_ID,
            "private_key": private_key,
            "client_email": settings.FIREBASE_CLIENT_EMAIL,
            "token_uri": "https://oauth2.googleapis.com/token",
        }

        cred = credentials.Certificate(cred_dict)
        firebase_admin.initialize_app(cred, {
            'databaseURL': settings.FIREBASE_DATABASE_URL
        })
        print("Firebase Admin SDK initialized successfully")


def verify_firebase_token(token: str):
    """Verify Firebase ID token"""
    try:
        decoded_token = firebase_auth.verify_id_token(token)
        return decoded_token
    except Exception as e:
        print(f"Token verification failed: {e}")
        return None


def get_user_by_uid(uid: str):
    """Get user information by UID"""
    try:
        user = firebase_auth.get_user(uid)
        return user
    except Exception as e:
        print(f"Failed to get user: {e}")
        return None


def set_custom_user_claims(uid: str, claims: dict):
    """Set custom claims for a user (e.g., roles)"""
    try:
        firebase_auth.set_custom_user_claims(uid, claims)
        return True
    except Exception as e:
        print(f"Failed to set custom claims: {e}")
        return False
