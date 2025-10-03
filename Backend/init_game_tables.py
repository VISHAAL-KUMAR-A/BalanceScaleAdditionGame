"""
Initialize game-related database tables.
Run this script to create the new GameSession table.
"""
from app.core.database import init_db, engine
from app.models.database_models import Base

def main():
    """Initialize all database tables"""
    print("Creating database tables...")
    try:
        Base.metadata.create_all(bind=engine)
        print("✅ Database tables created successfully!")
        print("   - users table")
        print("   - game_sessions table (new)")
    except Exception as e:
        print(f"❌ Error creating tables: {e}")
        raise

if __name__ == "__main__":
    main()

