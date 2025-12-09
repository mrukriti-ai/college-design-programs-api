#!/usr/bin/env python3
"""
Database Viewer Script for College Design Programs App
View all records in the SQLite database
"""

import sqlite3
import os
from pathlib import Path
import pandas as pd

# Database path
DB_PATH = Path(__file__).parent / "data" / "app.db"

def connect_db():
    """Connect to the database"""
    if not DB_PATH.exists():
        print(f"❌ Database not found at: {DB_PATH}")
        print("   The database will be created when you first run the FastAPI app.")
        return None
    return sqlite3.connect(str(DB_PATH))

def show_tables(conn):
    """Show all tables in the database"""
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    return [table[0] for table in tables]

def view_colleges(conn, limit=50):
    """View colleges table"""
    query = f"""
    SELECT 
        id, name, location_city, location_country, 
        program_name, program_type, degree_level,
        tuition_min, tuition_max, website_url
    FROM colleges
    LIMIT {limit}
    """
    df = pd.read_sql_query(query, conn)
    return df

def view_user_profiles(conn):
    """View user profiles table"""
    query = """
    SELECT 
        id, name, email, education_level,
        program_interest, budget_range, location_preference,
        degree_level, include_international,
        created_at
    FROM user_profiles
    """
    df = pd.read_sql_query(query, conn)
    return df

def view_favorites(conn):
    """View user favorites table"""
    query = """
    SELECT 
        uf.id, uf.user_email, uf.college_id,
        c.name as college_name, c.program_name,
        uf.created_at
    FROM user_favorites uf
    LEFT JOIN colleges c ON uf.college_id = c.id
    """
    df = pd.read_sql_query(query, conn)
    return df

def get_table_count(conn, table_name):
    """Get count of records in a table"""
    cursor = conn.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    return cursor.fetchone()[0]

def main():
    """Main function to display database contents"""
    print("=" * 80)
    print("📊 College Design Programs - Database Viewer")
    print("=" * 80)
    print()
    
    conn = connect_db()
    if not conn:
        return
    
    print(f"✅ Database found: {DB_PATH}")
    print()
    
    # Show all tables
    tables = show_tables(conn)
    print(f"📋 Available tables: {', '.join(tables) if tables else 'No tables found'}")
    print()
    
    # View each table
    for table in tables:
        count = get_table_count(conn, table)
        print(f"\n{'='*80}")
        print(f"📊 Table: {table} ({count} records)")
        print('='*80)
        
        if table == 'colleges':
            df = view_colleges(conn)
            if not df.empty:
                print(df.to_string(index=False))
            else:
                print("   No records found.")
        
        elif table == 'user_profiles':
            df = view_user_profiles(conn)
            if not df.empty:
                print(df.to_string(index=False))
            else:
                print("   No records found.")
        
        elif table == 'user_favorites':
            df = view_favorites(conn)
            if not df.empty:
                print(df.to_string(index=False))
            else:
                print("   No records found.")
        
        else:
            # Generic view for other tables
            query = f"SELECT * FROM {table} LIMIT 20"
            try:
                df = pd.read_sql_query(query, conn)
                if not df.empty:
                    print(df.to_string(index=False))
                else:
                    print("   No records found.")
            except Exception as e:
                print(f"   Error viewing table: {e}")
    
    conn.close()
    print()
    print("=" * 80)
    print("✅ Database viewing complete!")
    print("=" * 80)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()

