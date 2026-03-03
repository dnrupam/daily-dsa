import os
from datetime import datetime

LOG_FILE = "daily_log.md"


def get_today_date():
    # FORMAT: 03 March 2026
    return datetime.today().strftime("%d %B %Y")


def ensure_log_file():
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            f.write(
                "# 📘 Daily DSA Log\n\n"
                "Track your daily problem-solving journey 🚀\n\n"
                "---\n\n"
            )


def add_entry(date, problem, topic):
    entry_header = f"## 📅 {date}"
    entry_line = f"- {problem} ({topic})"

    with open(LOG_FILE, "r") as f:
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

    with open(LOG_FILE, "w") as f:
        f.writelines(new_lines)


def main():
    ensure_log_file()

    print("\n📘 Daily DSA Logger\n")

    # DATE INPUT
    use_today = input("Use today's date? (y/n): ").strip().lower()
    if use_today == "y":
        date = get_today_date()
    else:
        print("Enter date in format: DD Month YYYY (e.g., 03 March 2026)")
        date = input("Date: ")

    # PROBLEM INPUT
    problem = input("Enter problem name: ").strip()
    topic = input("Enter topic (Array/DP/Graph...): ").strip()

    add_entry(date, problem, topic)

    print("\n✅ daily_log.md updated!")

    # Auto add log file
    os.system("git add daily_log.md")


if __name__ == "__main__":
    main()