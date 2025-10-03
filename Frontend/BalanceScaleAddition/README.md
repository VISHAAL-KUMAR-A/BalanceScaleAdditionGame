# Balance Scale Addition Game - Frontend

Vue.js frontend with Firebase Authentication for the Balance Scale Addition Game.

## Features

- 🔐 Firebase Authentication (Email/Password & Google Sign-in)
- 🛣️ Vue Router with Protected Routes
- 🏪 Pinia State Management
- 👥 Role-Based Access Control (User, Student, Teacher, Admin)
- 📱 Responsive Design
- 🎨 Modern UI/UX

## Installation

1. Install dependencies:
```bash
npm install
```

2. Configure environment variables:
Create a `.env` file in the root directory with your Firebase configuration (see `.env.example`)

## Development

```bash
# Start development server (usually runs on http://localhost:5173)
npm run dev
```

## Build

```bash
# Build for production
npm run build

# Preview production build
npm run preview
```

## Project Structure

```
src/
├── api/
│   └── axios.js              # Axios instance with auth interceptors
├── config/
│   └── firebase.js           # Firebase configuration
├── router/
│   └── index.js              # Vue Router with navigation guards
├── stores/
│   └── auth.js               # Pinia authentication store
├── views/
│   ├── Home.vue              # Landing page
│   ├── Login.vue             # Login page
│   ├── Register.vue          # Registration page
│   ├── Dashboard.vue         # User dashboard
│   ├── Unauthorized.vue      # Unauthorized access page
│   ├── NotFound.vue          # 404 page
│   ├── student/              # Student-specific pages
│   │   ├── Games.vue
│   │   └── Progress.vue
│   ├── teacher/              # Teacher-specific pages
│   │   ├── Students.vue
│   │   └── Assignments.vue
│   └── admin/                # Admin-specific pages
│       ├── Users.vue
│       └── Stats.vue
├── App.vue                   # Root component
└── main.js                   # Application entry point
```

## Authentication Flow

1. **Registration/Login**: Users can register with email/password or sign in with Google
2. **Token Management**: Firebase ID tokens are automatically added to API requests
3. **Protected Routes**: Navigation guards check authentication and roles before allowing access
4. **Session Management**: Auth state persists across page refreshes

## User Roles & Access

### User (Default)
- Access to basic dashboard
- Limited functionality

### Student
- Access to games
- View personal progress
- Play balance scale addition games

### Teacher
- View and manage students
- Create and manage assignments
- Access student progress

### Admin
- Full system access
- User management
- Role assignment
- System statistics

## Routes

| Route | Access | Description |
|-------|--------|-------------|
| `/` | Public | Home page |
| `/login` | Public | Login page |
| `/register` | Public | Registration page |
| `/dashboard` | Authenticated | User dashboard |
| `/student/games` | Student+ | Available games |
| `/student/progress` | Student+ | Student progress |
| `/teacher/students` | Teacher+ | Student management |
| `/teacher/assignments` | Teacher+ | Assignment management |
| `/admin/users` | Admin | User management |
| `/admin/stats` | Admin | System statistics |

## Environment Variables

Required environment variables (prefix with `VITE_` for Vite):

```
VITE_FIREBASE_API_KEY=your_api_key
VITE_FIREBASE_AUTH_DOMAIN=your_auth_domain
VITE_FIREBASE_PROJECT_ID=your_project_id
VITE_FIREBASE_STORAGE_BUCKET=your_storage_bucket
VITE_FIREBASE_MESSAGING_SENDER_ID=your_sender_id
VITE_FIREBASE_APP_ID=your_app_id
VITE_FIREBASE_DATABASE_URL=your_database_url
VITE_API_URL=http://localhost:8000
```

## API Integration

The frontend communicates with the FastAPI backend at `VITE_API_URL` (default: http://localhost:8000).

All authenticated requests automatically include the Firebase ID token in the Authorization header.

## Testing Accounts

After registration, you can use the admin panel to assign roles to test different access levels.

## Security Notes

- All sensitive routes are protected by authentication guards
- Role-based access is enforced at both router and API levels
- Firebase ID tokens are automatically refreshed
- Tokens are validated by the backend on each request
