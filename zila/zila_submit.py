#!/usr/bin/env python3
"""zila-submit (prototype). Requires git + GitHub CLI (`gh auth login`).
Run from inside the cloned internship repo."""
import subprocess, datetime, pathlib, sys

def run(*cmd):
    return subprocess.run(cmd, check=True, text=True, capture_output=True).stdout.strip()

user = run("gh", "api", "user", "--jq", ".login")
today = datetime.date.today().isoformat()

# 1. Daily PR limit
n = int(run("gh", "pr", "list", "--author", user, "--state", "all",
            "--search", f"created:>={today}", "--json", "number", "--jq", "length"))
if n >= 2:
    sys.exit("You have already made 2 PRs today. Try again tomorrow.")

# 2. Ask for details
level      = input("Level (beginner/intermediate/advanced): ").strip()
module     = input("Module (e.g. 1_python): ").strip()
day        = input("Day number: ").strip()
summary    = input("Summary of what you did: ").strip()
challenges = input("Challenges: ").strip()
repo_url   = input("Project GitHub repo URL: ").strip()
deploy     = input("Deployment URL (optional): ").strip() or "n/a"

# 3. Prepare exercise.md from template
folder = pathlib.Path("contributors") / user / level / module / f"day_{day}"
folder.mkdir(parents=True, exist_ok=True)
ex = folder / "exercise.md"
if not ex.exists():
    tpl = pathlib.Path("templates/exercise.md").read_text()
    values = {"DAY": day, "MODULE": module, "GITHUB_USERNAME": user, "DATE": today,
              "SUMMARY": summary, "CHALLENGES": challenges, "REPO": repo_url, "DEPLOY": deploy}
    for k, v in values.items():
        tpl = tpl.replace("{{%s}}" % k, v)
    ex.write_text(tpl)
input(f"Add your work files to {folder}/ now, then press Enter...")

# 4. Branch, commit, push, PR (all automatic)
branch = f"{module}/{user}/day_{day}"
run("git", "checkout", "-B", branch)
run("git", "add", str(folder))
run("git", "commit", "-m", f"{user}: {module} day {day}")
run("git", "push", "-u", "origin", branch, "--force-with-lease")
url = run("gh", "pr", "create", "--base", "main", "--head", branch,
          "--title", f"[{module}] {user} - Day {day}",
          "--body", f"Module: {module}\nDay: {day}\nIntern: {user}\n\n{summary}")
print("PR created:", url)
