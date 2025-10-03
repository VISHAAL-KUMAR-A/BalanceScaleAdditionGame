from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.core.firebase import initialize_firebase
from app.core.database import init_db
from app.api.routes import auth_db, protected_db, game

# Initialize Firebase (for Google Sign-in only)
initialize_firebase()

# Initialize Database
init_db()

app = FastAPI(
    title="Balance Scale Addition API",
    description="API for Balance Scale Addition Game with PostgreSQL + Firebase Google Auth",
    version="2.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_db.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(protected_db.router, prefix="/api", tags=["Protected Routes"])
app.include_router(game.router, prefix="/api/game", tags=["Balance Scale Game"])


@app.get("/")
async def root():
    return {
        "message": "Balance Scale Addition API",
        "version": "2.0.0",
        "database": "PostgreSQL",
        "auth": "Email/Password + Google Sign-in",
        "docs": "/docs"
    }


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "database": "connected"
    }
