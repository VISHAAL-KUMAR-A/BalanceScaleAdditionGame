# Balance Scale Addition API - Backend

FastAPI backend with Firebase Authentication for the Balance Scale Addition Game.

## Features

- 🔐 Firebase Authentication Integration
- 👥 Role-Based Access Control (User, Student, Teacher, Admin)
- 🛡️ Protected API Routes
- 📝 Session Management
- 🚀 Fast and Modern API with FastAPI

## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Configure environment variables:
Create a `.env` file with your Firebase credentials (see `.env.example`)

## Running the Server

```bash
# Development mode with auto-reload
uvicorn main:app --reload --port 8000

# Production mode
uvicorn main:app --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

API documentation at `http://localhost:8000/docs`

## Authentication

All protected routes require a Firebase ID token in the Authorization header:
```
Authorization: Bearer <firebase-id-token>
```

## User Roles

1. **User** - Basic authenticated user
2. **Student** - Can access student-specific features (games, progress)
3. **Teacher** - Can manage students and assignments
4. **Admin** - Full system access, can manage user roles

## API Endpoints

### Public Endpoints
- `GET /` - API information
- `GET /health` - Health check

### Authentication Endpoints
- `POST /api/auth/verify-token` - Verify Firebase token
- `GET /api/auth/me` - Get current user profile
- `POST /api/auth/set-role/{uid}` - Set user role (Admin only)
- `GET /api/auth/users/{uid}` - Get user info (Admin only)

### Protected Endpoints

#### General (Any authenticated user)
- `GET /api/dashboard` - User dashboard

#### Student Routes
- `GET /api/student/games` - Get available games
- `GET /api/student/progress` - Get student progress

#### Teacher Routes
- `GET /api/teacher/students` - Get teacher's students
- `GET /api/teacher/assignments` - Get assignments

#### Admin Routes
- `GET /api/admin/users` - Get all users
- `GET /api/admin/stats` - Get system statistics

## Project Structure

```
Backend/
├── app/
│   ├── api/
│   │   └── routes/
│   │       ├── auth.py          # Authentication routes
│   │       └── protected.py     # Protected routes
│   ├── core/
│   │   ├── config.py           # Configuration
│   │   ├── firebase.py         # Firebase setup
│   │   └── security.py         # Security & dependencies
│   └── models/
│       └── user.py             # User models
├── main.py                     # FastAPI application
├── requirements.txt            # Python dependencies
└── .env                        # Environment variables
```

## Security Notes

- All authentication is handled by Firebase
- Custom claims are used for role management
- Role hierarchy ensures proper access control
- CORS is configured for frontend integration

