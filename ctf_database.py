import sqlite3
from pathlib import Path
from datetime import datetime
import os

BASE_DIR = Path("/app" if os.path.exists("/app") else "/home/fara/.gemini/antigravity/scratch/telegram_video_bot")
DB_PATH = BASE_DIR / "ctf_platform.db"

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_db() as conn:
        cursor = conn.cursor()
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            first_name TEXT,
            score INTEGER DEFAULT 0,
            solved_count INTEGER DEFAULT 0,
            current_challenge_id INTEGER DEFAULT 1,
            joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS challenges (
            id INTEGER PRIMARY KEY,
            module TEXT,
            title TEXT,
            difficulty TEXT,
            points INTEGER,
            description TEXT,
            hint TEXT,
            flag TEXT UNIQUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS submissions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            challenge_id INTEGER,
            flag TEXT,
            is_correct INTEGER,
            points_awarded INTEGER,
            submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(user_id) REFERENCES users(user_id),
            FOREIGN KEY(challenge_id) REFERENCES challenges(id)
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS hints_used (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            challenge_id INTEGER,
            used_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(user_id, challenge_id)
        );
        """)
        
        conn.commit()

def register_user(user_id: int, username: str, first_name: str):
    with get_db() as conn:
        conn.execute("""
        INSERT INTO users (user_id, username, first_name)
        VALUES (?, ?, ?)
        ON CONFLICT(user_id) DO UPDATE SET
            username=excluded.username,
            first_name=excluded.first_name;
        """, (user_id, username, first_name))
        conn.commit()

def get_user_stats(user_id: int):
    with get_db() as conn:
        return conn.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchone()

def get_leaderboard(limit: int = 10):
    with get_db() as conn:
        return conn.execute("""
        SELECT username, first_name, score, solved_count
        FROM users
        ORDER BY score DESC, solved_count DESC
        LIMIT ?
        """, (limit,)).fetchall()

def verify_flag(user_id: int, submitted_flag: str):
    with get_db() as conn:
        chal = conn.execute("SELECT * FROM challenges WHERE flag = ?", (submitted_flag.strip(),)).fetchone()
        if not chal:
            return {"status": "wrong", "msg": "❌ Noto'g'ri flag! Qaytadan urinib ko'ring."}
        
        already = conn.execute("""
        SELECT * FROM submissions 
        WHERE user_id = ? AND challenge_id = ? AND is_correct = 1
        """, (user_id, chal["id"])).fetchone()
        
        if already:
            return {"status": "already", "msg": f"⚠️ Siz bu topshiriqni (#{chal['id']} - {chal['title']}) allaqachon topshirgansiz!"}
        
        hint_used = conn.execute("""
        SELECT * FROM hints_used WHERE user_id = ? AND challenge_id = ?
        """, (user_id, chal["id"])).fetchone()
        
        points = max(1, chal["points"] - 1) if hint_used else chal["points"]
            
        conn.execute("""
        INSERT INTO submissions (user_id, challenge_id, flag, is_correct, points_awarded)
        VALUES (?, ?, ?, 1, ?)
        """, (user_id, chal["id"], submitted_flag.strip(), points))
        
        conn.execute("""
        UPDATE users 
        SET score = score + ?, solved_count = solved_count + 1
        WHERE user_id = ?
        """, (points, user_id))
        
        conn.commit()
        return {
            "status": "correct",
            "title": chal["title"],
            "points": points,
            "module": chal["module"],
            "msg": f"🎉 <b>TO'G'RI!</b>\n\n📌 <b>Topshiriq:</b> #{chal['id']} — {chal['title']} ({chal['module']})\n🏆 <b>Qo'shilgan ball:</b> +{points} ball!"
        }

if __name__ == "__main__":
    init_db()
