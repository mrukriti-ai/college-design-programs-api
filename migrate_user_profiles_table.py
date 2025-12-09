#!/usr/bin/env python3
"""
Migration script to add new columns to user_profiles table
Run this once to update the existing database schema
"""

import sqlite3
import os
from pathlib import Path

# Database path
DB_PATH = Path(__file__).parent / "data" / "app.db"

def migrate_database():
    """Add new columns to user_profiles table"""
    
    if not DB_PATH.exists():
        print(f"❌ Database not found at: {DB_PATH}")
        print("   The database will be created automatically when you run the FastAPI app.")
        return
    
    conn = sqlite3.connect(str(DB_PATH))
    cursor = conn.cursor()
    
    try:
        # Check if columns already exist
        cursor.execute("PRAGMA table_info(user_profiles)")
        columns = [col[1] for col in cursor.fetchall()]
        
        # Add degree_level column if it doesn't exist
        if 'degree_level' not in columns:
            print("Adding degree_level column...")
            cursor.execute("ALTER TABLE user_profiles ADD COLUMN degree_level TEXT")
            print("✅ Added degree_level column")
        else:
            print("✅ degree_level column already exists")
        
        # Add include_international column if it doesn't exist
        if 'include_international' not in columns:
            print("Adding include_international column...")
            cursor.execute("ALTER TABLE user_profiles ADD COLUMN include_international TEXT DEFAULT 'true'")
            print("✅ Added include_international column")
        else:
            print("✅ include_international column already exists")
        
        conn.commit()
        print("\n✅ Migration completed successfully!")
        
    except Exception as e:
        print(f"❌ Error during migration: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    print("=" * 60)
    print("🔄 User Profiles Table Migration")
    print("=" * 60)
    print()
    migrate_database()

