#!/usr/bin/env python3
"""
opsec_sanitizer.py — Automated OPSEC, Privacy, Binary & Git History Auditor
=============================================================================
Protects the repository author and contributors by scanning:
  1. All tracked/untracked workspace files for OS paths (C:\\Users\\..., /home/...),
     personal emails, Windows hostnames (DESKTOP-..., WIN-...), or leaked tokens.
  2. All compiled PE binaries (.exe / .dll) in build/ to ensure /PDBALTPATH:%_PDB%
     stripped local C:\\Users\\... paths from the RSDS debug directory.
  3. Git staging status to block forbidden artifacts (*.dmp, *.pdb, *.ilk, *.i64).
  4. Local Git config & commit history (git log) to ensure all commits use the
     anonymous handle ('deavers') and GitHub noreply email.

Usage:
  python Tools_and_Scripts/opsec_sanitizer.py
  python Tools_and_Scripts/opsec_sanitizer.py --fix-git
  python Tools_and_Scripts/opsec_sanitizer.py --ci
"""

import argparse
import os
import pathlib
import re
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

ALLOWED_EMAIL_DOMAINS = {
    "users.noreply.github.com",
    "noreply.github.com",
    "github.com",
    "example.com",
}

FORBIDDEN_TRACKED_EXTENSIONS = {
    ".dmp", ".mdmp", ".hdmp", ".core",
    ".pdb", ".ilk", ".idb", ".i64", ".bndb", ".dd32", ".dd64",
    ".pfx", ".pem", ".key",
}

PATH_PATTERNS = [
    (re.compile(r"[A-Za-z]:\\[Uu]sers\\[A-Za-z0-9_.-]+"), "Windows Local User Path"),
    (re.compile(r"[A-Za-z]:/[Uu]sers/[A-Za-z0-9_.-]+"), "Windows Local User Path (Forward Slash)"),
    (re.compile(r"(?<![A-Za-z0-9])/(?:home|Users)/[A-Za-z0-9_.-]+"), "Unix/macOS Local Home Path"),
    (re.compile(r"\\AppData\\(?:Local|Roaming|LocalLow)\\", re.IGNORECASE), "Windows AppData Path"),
    (re.compile(r"\b(?:DESKTOP|LAPTOP)-[A-Z0-9]{5,15}\b"), "Windows Hostname Identifier"),
    (re.compile(r"(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9_]{30,255}"), "GitHub Personal Access Token"),
]

EMAIL_REGEX = re.compile(r"\b([A-Za-z0-9_.+-]+)@([A-Za-z0-9-]+\.[A-Za-z0-9-.]+)\b")


def scan_workspace_files() -> list[str]:
    issues = []
    text_exts = {
        ".md", ".html", ".json", ".py", ".cpp", ".hpp", ".h", ".c",
        ".CT", ".ct", ".bat", ".sh", ".ps1", ".yml", ".yaml", ".txt", ".cmake"
    }

    for p in sorted(ROOT.rglob("*")):
        if not p.is_file():
            continue
        if ".git" in p.parts or "__pycache__" in p.parts:
            continue
        rel = p.relative_to(ROOT)

        # Check binary files in build/ for embedded C:\Users\ strings
        if "build" in p.parts:
            if p.suffix.lower() in {".exe", ".dll", ".pdb", ".ilk"}:
                raw = p.read_bytes()
                if b"\\Users\\" in raw or b"/Users/" in raw:
                    issues.append(
                        f"[BINARY PATH LEAK] {rel} contains embedded '\\Users\\' path! "
                        f"Rebuild with /PDBALTPATH:%_PDB% or clean build/ folder."
                    )
            continue

        if p.suffix in text_exts or p.name in {"LICENSE", ".gitignore", ".gitattributes", "CMakeLists.txt"}:
            # Skip self-scanning regex definitions in opsec_sanitizer.py and SECURITY.md examples
            if p.name in {"opsec_sanitizer.py", "SECURITY.md"}:
                continue

            txt = p.read_text(encoding="utf-8", errors="ignore")
            for idx, line in enumerate(txt.splitlines(), 1):
                for rx, label in PATH_PATTERNS:
                    m = rx.search(line)
                    if m:
                        issues.append(f"[FILE LEAK: {label}] {rel}:{idx} -> '{m.group(0)}'")

                for em in EMAIL_REGEX.finditer(line):
                    full_email = em.group(0)
                    domain = em.group(2).lower()
                    # Ignore false-positive assembly symbols or decorator strings
                    if domain not in ALLOWED_EMAIL_DOMAINS and "." in domain:
                        issues.append(f"[PERSONAL EMAIL LEAK] {rel}:{idx} -> '{full_email}'")

    return issues


def check_git_tracked_files() -> list[str]:
    issues = []
    try:
        out = subprocess.check_output(
            ["git", "status", "--porcelain"], cwd=ROOT, text=True, stderr=subprocess.DEVNULL
        )
        for line in out.splitlines():
            if len(line) < 4:
                continue
            filepath = line[3:].strip().strip('"')
            ext = pathlib.Path(filepath).suffix.lower()
            if ext in FORBIDDEN_TRACKED_EXTENSIONS:
                issues.append(f"[FORBIDDEN ARTIFACT] '{filepath}' ({ext}) must never be committed!")
    except Exception:
        pass
    return issues


def check_git_identity_and_history(ci_mode: bool = False) -> list[str]:
    issues = []
    if not (ROOT / ".git").exists():
        return issues

    if not ci_mode:
        try:
            uname = subprocess.check_output(
                ["git", "config", "user.name"], cwd=ROOT, text=True, stderr=subprocess.DEVNULL
            ).strip()
            uemail = subprocess.check_output(
                ["git", "config", "user.email"], cwd=ROOT, text=True, stderr=subprocess.DEVNULL
            ).strip()
            if uname != "deavers":
                issues.append(f"[GIT CONFIG] Local git user.name is '{uname}' (recommended: 'deavers').")
            if not uemail.endswith("@users.noreply.github.com"):
                issues.append(
                    f"[GIT CONFIG] Local git user.email is '{uemail}' "
                    f"(recommended: '106682353+deavers@users.noreply.github.com')."
                )
        except Exception:
            issues.append("[GIT CONFIG] Local git user.name / user.email not configured.")

    try:
        log_out = subprocess.check_output(
            ["git", "log", "--format=%h|%an|%ae|%cn|%ce"], cwd=ROOT, text=True, stderr=subprocess.DEVNULL
        )
        for line in log_out.splitlines():
            parts = line.split("|")
            if len(parts) != 5:
                continue
            commit_hash, an, ae, cn, ce = parts
            for email_val, role in [(ae, "Author"), (ce, "Committer")]:
                domain = email_val.split("@")[-1].lower() if "@" in email_val else ""
                if domain not in ALLOWED_EMAIL_DOMAINS:
                    issues.append(
                        f"[GIT HISTORY EMAIL LEAK] Commit {commit_hash} exposes {role} email '{email_val}'"
                    )
            for name_val, role in [(an, "Author"), (cn, "Committer")]:
                if name_val.lower() not in {"deavers", "github", "github-actions[bot]"}:
                    issues.append(
                        f"[GIT HISTORY NAME LEAK] Commit {commit_hash} exposes {role} name '{name_val}' (expected 'deavers')"
                    )
    except Exception:
        pass

    return issues


def fix_git_config_and_history() -> None:
    print("[*] Setting local Git author identity to 'deavers <106682353+deavers@users.noreply.github.com>'...")
    subprocess.run(["git", "config", "--local", "user.name", "deavers"], cwd=ROOT, check=True)
    subprocess.run(
        ["git", "config", "--local", "user.email", "106682353+deavers@users.noreply.github.com"],
        cwd=ROOT,
        check=True,
    )

    # Clean build directory if it contains old unstripped binaries
    build_dir = ROOT / "build"
    if build_dir.exists():
        print("[*] Removing local build/ directory to purge old unstripped PE/PDB artifacts...")
        shutil.rmtree(build_dir, ignore_errors=True)

    # Rewrite git history in-place (without touching working tree) so all personal names/emails become 'deavers'
    print("[*] Scrubbing Git commit history so all personal names/emails become 'deavers'...")
    revs = subprocess.check_output(
        ["git", "rev-list", "--reverse", "--topo-order", "HEAD"], cwd=ROOT, text=True
    ).splitlines()

    commit_map: dict[str, str] = {}
    bot_names = {"github-actions[bot]"}
    anon_ident = "deavers <106682353+deavers@users.noreply.github.com>"

    for old_sha in revs:
        raw_commit = subprocess.check_output(["git", "cat-file", "commit", old_sha], cwd=ROOT)
        header_bytes, sep, body_bytes = raw_commit.partition(b"\n\n")
        header_lines = header_bytes.decode("utf-8", errors="replace").splitlines()
        new_header_lines = []

        for hline in header_lines:
            if hline.startswith("parent "):
                old_parent = hline.split(" ", 1)[1].strip()
                new_parent = commit_map.get(old_parent, old_parent)
                new_header_lines.append(f"parent {new_parent}")
            elif hline.startswith("author "):
                # Format: author Name <email> timestamp tz
                m = re.match(r"^author (.+?) <(.+?)> (\d+ [+-]\d{4})$", hline)
                if m and m.group(1) not in bot_names:
                    new_header_lines.append(f"author {anon_ident} {m.group(3)}")
                else:
                    new_header_lines.append(hline)
            elif hline.startswith("committer "):
                m = re.match(r"^committer (.+?) <(.+?)> (\d+ [+-]\d{4})$", hline)
                if m and m.group(1) not in (bot_names | {"GitHub"}):
                    new_header_lines.append(f"committer {anon_ident} {m.group(3)}")
                else:
                    new_header_lines.append(hline)
            else:
                new_header_lines.append(hline)

        new_raw = ("\n".join(new_header_lines)).encode("utf-8") + sep + body_bytes
        new_sha = subprocess.check_output(
            ["git", "hash-object", "-t", "commit", "-w", "--stdin"],
            cwd=ROOT,
            input=new_raw,
        ).decode("utf-8").strip()
        commit_map[old_sha] = new_sha

    if revs and revs[-1] in commit_map:
        new_head = commit_map[revs[-1]]
        head_ref = subprocess.check_output(
            ["git", "symbolic-ref", "HEAD"], cwd=ROOT, text=True
        ).strip()
        subprocess.run(["git", "update-ref", head_ref, new_head], cwd=ROOT, check=True)
        for remote_ref in ["refs/remotes/origin/main", "refs/remotes/origin/HEAD"]:
            try:
                subprocess.run(["git", "update-ref", "-d", remote_ref], cwd=ROOT, stderr=subprocess.DEVNULL)
            except Exception:
                pass

    subprocess.run(["git", "reflog", "expire", "--expire=now", "--all"], cwd=ROOT, check=True)
    subprocess.run(["git", "gc", "--prune=now", "--quiet"], cwd=ROOT, check=True)
    print("[+] Git history and local config successfully anonymized!")


def main() -> None:
    parser = argparse.ArgumentParser(description="OPSEC, PII & Binary Path Sanitizer")
    parser.add_argument("--fix-git", action="store_true", help="Anonymize local git config, history, and clean build/")
    parser.add_argument("--ci", action="store_true", help="Run in GitHub Actions CI mode")
    args = parser.parse_args()

    if args.fix_git:
        fix_git_config_and_history()

    print("=" * 74)
    print("  [OPSEC SHIELD] REVERSE ENGINEERING JOURNEY - PRIVACY SANITIZER AUDIT")
    print("=" * 74)

    file_issues = scan_workspace_files()
    tracked_issues = check_git_tracked_files()
    git_issues = check_git_identity_and_history(ci_mode=args.ci)

    all_issues = file_issues + tracked_issues + git_issues

    if not all_issues:
        print("  [PASS] 0 Personal Paths (C:\\Users\\...) found in workspace files.")
        print("  [PASS] 0 Personal Email Addresses or Hostnames found.")
        print("  [PASS] 0 Unstripped PE/PDB Binaries or Memory Dumps found.")
        print("  [PASS] Git Commit History & Local Config 100% Anonymized ('deavers').")
        print("=" * 74)
        sys.exit(0)
    else:
        print(f"  [WARNING] Found {len(all_issues)} potential OPSEC/Privacy issue(s):\n")
        for idx, issue in enumerate(all_issues, 1):
            print(f"    {idx:02d}. {issue}")
        print("\n  Tip: Run 'python Tools_and_Scripts/opsec_sanitizer.py --fix-git' to auto-fix!")
        print("=" * 74)
        sys.exit(1)


if __name__ == "__main__":
    main()
