#!/usr/bin/env python3
import sys
import os
import sqlite3
from pathlib import Path

DB_PATH = Path("/home/fara/.gemini/antigravity/scratch/telegram_video_bot/ctf_platform.db")

# ANSI Color Codes
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"
MAGENTA = "\033[95m"
RESET = "\033[0m"

BANNER = f"""{CYAN}{BOLD}
   ██████╗██╗   ██╗██████╗ ███████╗██████╗      ██████╗████████╗███████╗
  ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗    ██╔════╝╚══██╔══╝██╔════╝
  ██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝    ██║        ██║   █████╗  
  ██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗    ██║        ██║   ██╔══╝  
  ╚██████╗   ██║   ██████╔╝███████╗██║  ██║    ╚██████╗   ██║   ██║     
   ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝     ╚═════╝   ╚═╝   ╚═╝     
{RESET}{YELLOW}   ⚡ ADVANCED LINUX SECURITY & DEV-OPS TRAINING PLATFORM ⚡{RESET}
"""

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def get_current_user_id():
    user = os.environ.get("USER", "student")
    if user.startswith("user_"):
        try:
            return int(user.split("_")[1])
        except:
            return 6895259303
    return 6895259303

def cmd_banner():
    print(BANNER)
    user_id = get_current_user_id()
    conn = get_conn()
    user = conn.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchone()
    score = user["score"] if user else 0
    solved = user["solved_count"] if user else 0
    
    print(f"{BOLD}👤 OPERATOR:{RESET} {GREEN}{os.environ.get('USER', 'student')}{RESET} | {BOLD}⭐ SCORE:{RESET} {YELLOW}{score} pts{RESET} | {BOLD}🚩 SOLVED:{RESET} {CYAN}{solved}{RESET}")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"{BOLD}Buyruqlar:{RESET}")
    print(f"  {CYAN}ctf list{RESET}         — Barcha topshiriqlar ro'yxatini ko'rish")
    print(f"  {CYAN}ctf info <id>{RESET}    — Topshiriqning batafsil sharti va vazifasi")
    print(f"  {CYAN}ctf hint <id>{RESET}    — Kichik yo'naltiruvchi maslahat (Hint) olish")
    print(f"  {CYAN}ctf submit <flag>{RESET}— Topilgan flagni tekshirish (HD{{...}})")
    print(f"  {CYAN}ctf rank{RESET}         — Eng kuchli ishtirokchilar reytingi (Leaderboard)")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")

def cmd_list():
    user_id = get_current_user_id()
    conn = get_conn()
    chals = conn.execute("SELECT * FROM challenges ORDER BY id ASC").fetchall()
    subs = {row["challenge_id"]: row for row in conn.execute("SELECT * FROM submissions WHERE user_id = ? AND is_correct = 1", (user_id,)).fetchall()}
    
    print(f"\n{BOLD}{CYAN}📋 MAVJUD CTF TOPSHIRIQLARI (HARD / MEDIUM):{RESET}\n")
    print(f"{'ID':<4} | {'MODUL':<32} | {'NOMI':<42} | {'QIYINLIK':<10} | {'BALL':<6} | {'HOLAT'}")
    print("─" * 115)
    
    for c in chals:
        is_solved = c["id"] in subs
        status = f"{GREEN}✅ SOLVED{RESET}" if is_solved else f"{YELLOW}⏳ OPEN{RESET}"
        diff_color = RED if c["difficulty"] == "Hard" else YELLOW
        diff = f"{diff_color}{c['difficulty']}{RESET}"
        
        print(f"#{c['id']:<3} | {c['module']:<32} | {c['title'][:40]:<42} | {diff:<18} | {c['points']:<4} pt | {status}")
    print("\n👉 Batafsil ko'rish uchun: `ctf info <id>` (Masalan: `ctf info 1`)\n")

def cmd_info(chal_id: int):
    conn = get_conn()
    c = conn.execute("SELECT * FROM challenges WHERE id = ?", (chal_id,)).fetchone()
    if not c:
        print(f"{RED}❌ Topshiriq #{chal_id} topilmadi! 'ctf list' qiling.{RESET}")
        return
        
    diff_color = RED if c["difficulty"] == "Hard" else YELLOW
    print(f"\n{BOLD}{CYAN}══════════════════════════════════════════════════════════════════════{RESET}")
    print(f"🎯 {BOLD}TOPSHIRQ #{c['id']}: {c['title']}{RESET}")
    print(f"{BOLD}{CYAN}══════════════════════════════════════════════════════════════════════{RESET}")
    print(f"📂 {BOLD}Modul:{RESET}     {c['module']}")
    print(f"⚡ {BOLD}Qiyinlik:{RESET}  {diff_color}{c['difficulty']}{RESET}")
    print(f"⭐ {BOLD}Ball:{RESET}      {YELLOW}{c['points']} ball{RESET}\n")
    print(f"{BOLD}📝 VAZIFA VA SENARIY:{RESET}")
    print(f"{c['description']}\n")
    print(f"💡 {BOLD}Hint kerakmi?{RESET} `ctf hint {c['id']}` buyrug'ini bering.")
    print(f"🚩 {BOLD}Flag topshirish:{RESET} `ctf submit HD{{...}}`\n")

def cmd_hint(chal_id: int):
    user_id = get_current_user_id()
    conn = get_conn()
    c = conn.execute("SELECT * FROM challenges WHERE id = ?", (chal_id,)).fetchone()
    if not c:
        print(f"{RED}❌ Topshiriq #{chal_id} topilmadi!{RESET}")
        return
        
    conn.execute("INSERT OR IGNORE INTO hints_used (user_id, challenge_id) VALUES (?, ?)", (user_id, chal_id))
    conn.commit()
    
    print(f"\n{YELLOW}{BOLD}💡 TOPSHIRIQ #{chal_id} UCHUN HINT:{RESET}")
    print(f"{c['hint']}\n")
    print(f"{CYAN}ℹ️ Eslatma: Hint olingani sababli topshiriqdan 1 ball kamroq beriladi.{RESET}\n")

def cmd_submit(flag: str):
    user_id = get_current_user_id()
    conn = get_conn()
    
    chal = conn.execute("SELECT * FROM challenges WHERE flag = ?", (flag.strip(),)).fetchone()
    if not chal:
        print(f"\n{RED}❌ NOTO'G'RI FLAG! Qaytadan tekshirib ko'ring.{RESET}\n")
        return
        
    already = conn.execute("SELECT * FROM submissions WHERE user_id = ? AND challenge_id = ? AND is_correct = 1", (user_id, chal["id"])).fetchone()
    if already:
        print(f"\n{YELLOW}⚠️ Siz bu topshiriqni (#{chal['id']} - {chal['title']}) allaqachon topshirgansiz!{RESET}\n")
        return
        
    hint_used = conn.execute("SELECT * FROM hints_used WHERE user_id = ? AND challenge_id = ?", (user_id, chal["id"])).fetchone()
    pts = max(1, chal["points"] - 1) if hint_used else chal["points"]
    
    conn.execute("INSERT INTO submissions (user_id, challenge_id, flag, is_correct, points_awarded) VALUES (?, ?, ?, 1, ?)", (user_id, chal["id"], flag.strip(), pts))
    conn.execute("UPDATE users SET score = score + ?, solved_count = solved_count + 1 WHERE user_id = ?", (pts, user_id))
    conn.commit()
    
    print(f"\n{GREEN}{BOLD}🎉🎉🎉 TABRIKLAYMIZ! FLAG TO'G'RI! 🎉🎉🎉{RESET}")
    print(f"📌 {BOLD}Topshiriq:{RESET} #{chal['id']} — {chal['title']}")
    print(f"⭐ {BOLD}Qo'shilgan ball:{RESET} {YELLOW}+{pts} ball{RESET}")
    print(f"🚀 Keyingi topshiriqni ochish uchun: {CYAN}ctf list{RESET}\n")

def cmd_rank():
    conn = get_conn()
    leaders = conn.execute("SELECT username, first_name, score, solved_count FROM users ORDER BY score DESC, solved_count DESC LIMIT 10").fetchall()
    
    print(f"\n{BOLD}{CYAN}🏆 TOP-10 CYBER CTF LEADERBOARD:{RESET}\n")
    print(f"{'O\'RIN':<6} | {'TALABA':<25} | {'BALL':<10} | {'YECHILGAN'}")
    print("─" * 55)
    
    medals = ["🥇 1", "🥈 2", "🥉 3", "4", "5", "6", "7", "8", "9", "10"]
    for i, r in enumerate(leaders):
        m = medals[i] if i < len(medals) else str(i+1)
        name = r["first_name"] or r["username"]
        print(f"{m:<6} | {name:<25} | {r['score']:<10} | {r['solved_count']} ta")
    print()

def main():
    if len(sys.argv) < 2:
        cmd_banner()
        return
        
    action = sys.argv[1].lower()
    if action in ["list", "ls", "all"]:
        cmd_list()
    elif action in ["info", "show", "cat"]:
        if len(sys.argv) < 3:
            print("Ishlatish: ctf info <id> (Masalan: ctf info 1)")
            return
        cmd_info(int(sys.argv[2]))
    elif action in ["hint", "help"]:
        if len(sys.argv) < 3:
            print("Ishlatish: ctf hint <id> (Masalan: ctf hint 1)")
            return
        cmd_hint(int(sys.argv[2]))
    elif action in ["submit", "flag", "verify"]:
        if len(sys.argv) < 3:
            print("Ishlatish: ctf submit <FLAG> (Masalan: ctf submit HD{...})")
            return
        cmd_submit(sys.argv[2])
    elif action in ["rank", "top", "leaderboard"]:
        cmd_rank()
    else:
        cmd_banner()

if __name__ == "__main__":
    main()
