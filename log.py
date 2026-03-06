import os
import sys
from datetime import datetime

LOG_FILE = "daily_log.md"


def get_today_date():
    # FORMAT: 03 March 2026
    return datetime.today().strftime("%d %B %Y")


def ensure_log_file():
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            f.write(
                "# 📘 Daily DSA Log\n\n"
                "Track your daily problem-solving journey 🚀\n\n"
                "---\n\n"
            )


def add_entry(date, problem, topic):
    entry_header = f"## 📅 {date}"
    entry_line = f"- {problem} ({topic})"

    with open(LOG_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    found_date = False

    i = 0
    while i < len(lines):
        line = lines[i]
        new_lines.append(line)

        if line.strip() == entry_header:
            found_date = True
            i += 1

            # Insert new entry just after date header
            new_lines.append(entry_line + "\n")

            # Copy remaining lines of that section
            while i < len(lines) and not lines[i].startswith("## 📅"):
                new_lines.append(lines[i])
                i += 1
            continue

        i += 1

    if not found_date:
        new_lines.append(f"\n{entry_header}\n")
        new_lines.append(entry_line + "\n")

    with open(LOG_FILE, "w", encoding="utf-8") as f:
        f.writelines(new_lines)


def prompt(tty, message):
    sys.stderr.write(message)
    sys.stderr.flush()
    return tty.readline().rstrip("\n").strip()


def main():
    ensure_log_file()

    # Open terminal directly — works even when stdin is piped (e.g. git hooks)
    # Open read-only (not r+) since CON/CONIN$ are not seekable on Windows
    try:
        tty = open("CONIN$", "r", buffering=1)  # Windows
    except OSError:
        try:
            tty = open("/dev/tty", "r", buffering=1)  # Linux/macOS
        except OSError:
            print("❌ Could not open terminal for input. Run `python log.py` manually.")
            sys.exit(0)

    print("\n📘 Daily DSA Logger\n")

    skip = prompt(tty, "Log a DSA problem? (y/n): ")
    if skip.lower() != "y":
        print("⏭️  Skipping DSA log. Pushing as-is...")
        tty.close()
        sys.exit(0)

    use_today = prompt(tty, "Use today's date? (y/n): ")
    if use_today.lower() == "y":
        date = get_today_date()
    else:
        print("Enter date in format: DD Month YYYY (e.g., 03 March 2026)")
        date = prompt(tty, "Date: ")

    problem = prompt(tty, "Enter problem name: ")
    topic = prompt(tty, "Enter topic (Array/DP/Graph...): ")

    tty.close()

    if not problem or not topic:
        print("❌ Problem name and topic cannot be empty.")
        sys.exit(1)

    add_entry(date, problem, topic)

    print("\n✅ daily_log.md updated!")

    # Commit the log entry so it's included in the push
    os.system("git add daily_log.md")
    os.system('git commit -m "📘 DSA log: {}" --no-verify'.format(f"{problem} ({topic})"))


if __name__ == "__main__":
    main()