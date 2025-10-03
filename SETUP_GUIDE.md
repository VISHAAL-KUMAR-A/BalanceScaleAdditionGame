# Balance Scale Addition Game - Setup Guide

Complete authentication system with Firebase (Frontend) and FastAPI (Backend)

## 📋 Table of Contents

- [Prerequisites](#prerequisites)
- [Backend Setup](#backend-setup)
- [Frontend Setup](#frontend-setup)
- [Running the Application](#running-the-application)
- [Testing Authentication](#testing-authentication)
- [User Roles](#user-roles)
- [Troubleshooting](#troubleshooting)

## Prerequisites

### Required Software

- **Python 3.8+** (for Backend)
- **Node.js 20.19.0+ or 22.12.0+** (for Frontend)
- **Firebase Account** (already configured)

### Firebase Configuration

Your Firebase project is already configured with:
- Project ID: `solesync-38630`
- Authentication methods: Email/Password and Google Sign-in

## Backend Setup

### 1. Navigate to Backend Directory

```bash
cd Backend
```

### 2. Create Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**macOS/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Verify Environment Variables

The `.env` file is already configured with your Firebase credentials. No changes needed unless you want to update them.

### 5. Start the Backend Server

```bash
uvicorn main:app --reload --port 8000
```

The API will be available at: `http://localhost:8000`

API Documentation: `http://localhost:8000/docs`

**Expected Output:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete.
Firebase Admin SDK initialized successfully
```

## Frontend Setup

### 1. Navigate to Frontend Directory

```bash
cd Frontend/BalanceScaleAddition
```

### 2. Install Dependencies

```bash
npm install
```

This will install:
- Vue 3
- Vue Router
- Pinia (State Management)
- Firebase SDK
- Axios

### 3. Verify Environment Variables

The `.env` file is already configured with your Firebase configuration. No changes needed.

### 4. Start the Development Server

```bash
npm run dev
```

The application will be available at: `http://localhost:5173`

**Expected Output:**
```
VITE v7.1.7  ready in 500 ms

➜  Local:   http://localhost:5173/
➜  Network: use --host to expose
```

## Running the Application

### Start Both Servers

**Terminal 1 (Backend):**
```bash
cd Backend
# Activate virtual environment if using one
uvicorn main:app --reload --port 8000
```

**Terminal 2 (Frontend):**
```bash
cd Frontend/BalanceScaleAddition
npm run dev
```

### Access the Application

Open your browser and navigate to: `http://localhost:5173`

## Testing Authentication

### 1. Register a New User

1. Click "Register" on the home page
2. Fill in your details:
   - Display Name: "Test User"
   - Email: "test@example.com"
   - Password: "password123"
3. Click "Register"
4. You'll be redirected to the dashboard

### 2. Test Google Sign-in

1. Click "Sign up with Google" or "Continue with Google"
2. Select your Google account
3. Authorize the application
4. You'll be redirected to the dashboard

### 3. Test Protected Routes

Try accessing these URLs directly (while logged in):

- Dashboard: `http://localhost:5173/dashboard` ✅ All users
- Student Games: `http://localhost:5173/student/games` ⚠️ Requires student role
- Teacher Panel: `http://localhost:5173/teacher/students` ⚠️ Requires teacher role
- Admin Panel: `http://localhost:5173/admin/users` ⚠️ Requires admin role

### 4. Assign User Roles (Admin Function)

To test role-based access, you need to assign roles. You can do this via the API:

**Using the API Documentation (`http://localhost:8000/docs`):**

1. First, register a user and get their user ID from the dashboard
2. Sign in as an admin (or make yourself admin using Firebase Console)
3. Go to `http://localhost:8000/docs`
4. Find the `POST /api/auth/set-role/{uid}` endpoint
5. Click "Try it out"
6. Enter:
   - `uid`: The user's Firebase UID
   - Request body: `{"role": "student"}` (or "teacher", "admin")
7. Click "Execute"

**Using Firebase Console (Quick Method):**

1. Go to Firebase Console: https://console.firebase.google.com/
2. Select your project: `solesync-38630`
3. Go to Authentication → Users
4. Find your user
5. Use Cloud Functions or Firebase CLI to set custom claims

**Using Postman/cURL:**

```bash
# First, get your Firebase ID token from the browser console:
# console.log(await firebase.auth().currentUser.getIdToken())

curl -X POST "http://localhost:8000/api/auth/set-role/USER_UID_HERE" \
  -H "Authorization: Bearer YOUR_FIREBASE_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"role": "student"}'
```

## User Roles

### Role Hierarchy

1. **User** (Default) - Basic access
2. **Student** - Can play games and view progress
3. **Teacher** - Can manage students and assignments
4. **Admin** - Full system access

### Role Permissions

| Feature | User | Student | Teacher | Admin |
|---------|------|---------|---------|-------|
| Dashboard | ✅ | ✅ | ✅ | ✅ |
| Play Games | ❌ | ✅ | ✅ | ✅ |
| View Progress | ❌ | ✅ | ✅ | ✅ |
| Manage Students | ❌ | ❌ | ✅ | ✅ |
| Create Assignments | ❌ | ❌ | ✅ | ✅ |
| User Management | ❌ | ❌ | ❌ | ✅ |
| System Stats | ❌ | ❌ | ❌ | ✅ |

## Troubleshooting

### Backend Issues

**Error: "Firebase Admin SDK initialization failed"**
- Check your `.env` file has correct Firebase credentials
- Verify the `FIREBASE_PRIVATE_KEY` has proper newline characters
- Ensure all Firebase environment variables are set

**Error: "Module not found"**
- Make sure you're in the Backend directory
- Activate virtual environment: `.\venv\Scripts\activate`
- Reinstall dependencies: `pip install -r requirements.txt`

**Port 8000 already in use:**
```bash
# Use a different port
uvicorn main:app --reload --port 8001

# Update frontend .env: VITE_API_URL=http://localhost:8001
```

### Frontend Issues

**Error: "Cannot find module"**
- Delete `node_modules` and reinstall:
  ```bash
  rm -rf node_modules package-lock.json
  npm install
  ```

**Firebase Authentication Error:**
- Verify Firebase configuration in `.env`
- Check Firebase Console that Email/Password and Google authentication are enabled
- Ensure your domain is authorized in Firebase Console

**CORS Error:**
- Verify backend is running on port 8000
- Check `VITE_API_URL` in frontend `.env`
- Ensure backend CORS settings allow `http://localhost:5173`

**Port 5173 already in use:**
```bash
# Vite will automatically use next available port
# Or specify a different port in vite.config.js
```

### Authentication Issues

**Token Verification Failed:**
- Make sure both frontend and backend use the same Firebase project
- Check that Firebase Admin SDK is properly initialized in backend
- Verify user is logged in before making API calls

**Google Sign-in Not Working:**
- Enable Google Sign-in in Firebase Console
- Check that authorized domains include `localhost`
- Verify Google OAuth credentials are configured

## API Endpoints Reference

### Authentication Endpoints

- `POST /api/auth/verify-token` - Verify Firebase token
- `GET /api/auth/me` - Get current user profile
- `POST /api/auth/set-role/{uid}` - Set user role (Admin only)

### Protected Endpoints

**General:**
- `GET /api/dashboard` - User dashboard

**Student:**
- `GET /api/student/games` - Get available games
- `GET /api/student/progress` - Get student progress

**Teacher:**
- `GET /api/teacher/students` - Get teacher's students
- `GET /api/teacher/assignments` - Get assignments

**Admin:**
- `GET /api/admin/users` - Get all users
- `GET /api/admin/stats` - Get system statistics

## Next Steps

Now that authentication is set up, you can:

1. **Implement the Balance Scale Game Logic**
   - Create game components
   - Add scoring system
   - Implement the visual balance scale

2. **Add Database Integration**
   - Store user progress
   - Save game scores
   - Track student performance

3. **Enhance Teacher Features**
   - Assignment creation
   - Student monitoring
   - Progress reports

4. **Add Admin Dashboard**
   - User management interface
   - System analytics
   - Role assignment UI

## Support

If you encounter any issues:

1. Check the console for error messages (F12 in browser)
2. Review the backend logs in the terminal
3. Verify all environment variables are correct
4. Ensure both servers are running
5. Check Firebase Console for authentication issues

## Security Notes

⚠️ **Important:** 
- Never commit `.env` files to version control
- Keep Firebase private keys secure
- Use environment-specific configurations for production
- Enable Firebase App Check for production
- Implement rate limiting for API endpoints
- Use HTTPS in production

