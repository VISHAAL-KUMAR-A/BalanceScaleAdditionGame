# 🎯 Balance Scale Addition Game

A modern educational platform for teaching addition through visual intuition using balance scales.

## ✅ Current Status: Authentication Complete

The authentication system is **fully implemented and ready to use**! This includes:

- 🔐 **Firebase Authentication** (Email/Password + Google Sign-in)
- 🛡️ **Protected Routes** (Frontend and Backend)
- 👥 **Role-Based Access Control** (User, Student, Teacher, Admin)
- 🔄 **Session Management** (Persistent auth state)
- 🎨 **Modern UI** with responsive design

## 🚀 Quick Start

### Prerequisites

- Python 3.8+ (Backend)
- Node.js 20.19+ (Frontend)
- Firebase project (already configured)

### Installation

**1. Backend Setup:**
```bash
cd Backend
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

**2. Frontend Setup:**
```bash
cd Frontend/BalanceScaleAddition
npm install
npm run dev
```

**3. Open Browser:**
```
http://localhost:5173
```

🎉 That's it! The authentication system is ready to use.

## 📚 Documentation

- **[SETUP_GUIDE.md](SETUP_GUIDE.md)** - Complete setup instructions with troubleshooting
- **[FEATURES.md](FEATURES.md)** - Detailed feature list and architecture
- **[Backend/README.md](Backend/README.md)** - Backend API documentation
- **[Frontend/BalanceScaleAddition/README.md](Frontend/BalanceScaleAddition/README.md)** - Frontend documentation

## 🎯 What's Included

### Backend (FastAPI)
- ✅ Firebase Admin SDK integration
- ✅ Token verification middleware
- ✅ Role-based authorization
- ✅ Protected API endpoints
- ✅ CORS configuration
- ✅ Comprehensive error handling

### Frontend (Vue.js 3)
- ✅ Firebase Authentication integration
- ✅ Vue Router with navigation guards
- ✅ Pinia state management
- ✅ Login/Register components
- ✅ Google Sign-in
- ✅ Protected route components
- ✅ Role-based UI rendering
- ✅ Modern, responsive design

## 👥 User Roles

| Role | Access |
|------|--------|
| **User** | Basic dashboard |
| **Student** | Games + Progress tracking |
| **Teacher** | Student management + Assignments |
| **Admin** | Full system access + User management |

## 🔑 Key Features

### Authentication
- Email/Password registration and login
- Google Sign-in (one-click)
- Persistent sessions
- Secure token management

### Authorization
- Protected routes (frontend + backend)
- Role-based access control
- Hierarchical permissions
- Custom Firebase claims

### User Interface
- Modern gradient design
- Smooth animations
- Loading states
- Error handling
- Mobile-responsive

## 📊 Project Structure

```
Vuejs/
├── Backend/                    # FastAPI backend
│   ├── app/
│   │   ├── api/routes/        # API endpoints
│   │   ├── core/              # Config, Firebase, Security
│   │   └── models/            # Data models
│   ├── main.py                # FastAPI app
│   └── requirements.txt
│
├── Frontend/BalanceScaleAddition/
│   ├── src/
│   │   ├── api/               # Axios client
│   │   ├── config/            # Firebase config
│   │   ├── router/            # Vue Router + guards
│   │   ├── stores/            # Pinia stores
│   │   ├── views/             # Page components
│   │   ├── App.vue
│   │   └── main.js
│   └── package.json
│
├── SETUP_GUIDE.md             # Detailed setup instructions
├── FEATURES.md                # Complete feature list
└── README.md                  # This file
```

## 🎮 Testing the System

### 1. Register a New User
```
http://localhost:5173/register
```

### 2. Login with Email/Password
```
http://localhost:5173/login
```

### 3. Try Google Sign-in
Click "Continue with Google" on login page

### 4. Access Protected Routes

**Try these URLs (logged in):**
- Dashboard: `/dashboard` ✅
- Student Games: `/student/games` (requires student role)
- Teacher Panel: `/teacher/students` (requires teacher role)
- Admin Panel: `/admin/users` (requires admin role)

### 5. Test Role-Based Access

By default, new users have "user" role. To test other roles:

**Option 1: Use API (http://localhost:8000/docs)**
```json
POST /api/auth/set-role/{uid}
{
  "role": "student"  // or "teacher", "admin"
}
```

**Option 2: Firebase Console**
Set custom claims via Firebase Console → Authentication

## 🌐 API Endpoints

### Public
- `GET /` - API info
- `GET /health` - Health check

### Authentication
- `POST /api/auth/verify-token` - Verify token
- `GET /api/auth/me` - Get user profile
- `POST /api/auth/set-role/{uid}` - Set role (admin)

### Protected
- `GET /api/dashboard` - Dashboard data
- `GET /api/student/games` - Available games (student+)
- `GET /api/student/progress` - Progress (student+)
- `GET /api/teacher/students` - Students list (teacher+)
- `GET /api/teacher/assignments` - Assignments (teacher+)
- `GET /api/admin/users` - All users (admin)
- `GET /api/admin/stats` - Statistics (admin)

## 🔒 Security

- ✅ Firebase ID token authentication
- ✅ Backend token verification on all protected routes
- ✅ Role-based authorization with hierarchy
- ✅ CORS protection
- ✅ Environment variable configuration
- ✅ Secure credential storage

## 🎨 Screenshots

### Home Page
Modern landing page with authentication options

### Login Page
Clean login form with email/password and Google sign-in

### Dashboard
Role-specific dashboard with quick links

### Protected Pages
Student games, teacher panel, admin interface

## 🐛 Troubleshooting

### Backend not starting?
- Check Python version: `python --version`
- Verify virtual environment is activated
- Reinstall dependencies: `pip install -r requirements.txt`

### Frontend not starting?
- Check Node version: `node --version`
- Delete node_modules: `rm -rf node_modules && npm install`
- Clear cache: `npm cache clean --force`

### Authentication not working?
- Verify Firebase configuration in `.env` files
- Check Firebase Console authentication methods are enabled
- Ensure both servers are running

**See [SETUP_GUIDE.md](SETUP_GUIDE.md) for detailed troubleshooting**

## 📈 Next Steps

The authentication is complete! Now you can:

1. **Implement the Balance Scale Game**
   - Create game components
   - Add visual balance scale
   - Implement scoring logic

2. **Add Database Integration**
   - Store user progress
   - Save game scores
   - Track student performance

3. **Enhance Features**
   - Assignment creation UI
   - Progress reports
   - Analytics dashboard

## 🛠️ Technology Stack

**Frontend:**
- Vue.js 3 (Composition API)
- Vue Router 4
- Pinia (State Management)
- Firebase JS SDK
- Axios
- Vite

**Backend:**
- FastAPI
- Firebase Admin SDK
- Uvicorn
- Python 3.8+

## 📝 Environment Variables

### Backend (.env)
```env
FIREBASE_PROJECT_ID=solesync-38630
FIREBASE_PRIVATE_KEY=<your-key>
FIREBASE_CLIENT_EMAIL=<your-email>
FIREBASE_DATABASE_URL=<your-url>
JWT_SECRET=<your-secret>
```

### Frontend (.env)
```env
VITE_FIREBASE_API_KEY=<your-key>
VITE_FIREBASE_AUTH_DOMAIN=<your-domain>
VITE_FIREBASE_PROJECT_ID=solesync-38630
VITE_FIREBASE_STORAGE_BUCKET=<your-bucket>
VITE_FIREBASE_MESSAGING_SENDER_ID=<your-id>
VITE_FIREBASE_APP_ID=<your-app-id>
VITE_API_URL=http://localhost:8000
```

## 🤝 Contributing

This is a complete authentication system ready for the game implementation phase.

## 📄 License

Educational project for Balance Scale Addition Game

---

## ⭐ Status

**Authentication System: ✅ COMPLETE**

All authentication, authorization, and role-based access control features are fully implemented, tested, and production-ready!

**Ready for:** Game implementation, database integration, and feature enhancement.

**Need Help?** Check [SETUP_GUIDE.md](SETUP_GUIDE.md) for detailed instructions and troubleshooting.

---

Made with ❤️ for educational purposes

