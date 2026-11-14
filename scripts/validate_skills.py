#!/usr/bin/env python3
"""
AI Agent Skills Repository Validator
Validates skill structure, frontmatter schemas, and catalog synchronization.
"""

import os
import sys
import re
import json

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS_DIR = os.path.join(REPO_ROOT, "skills")
CATALOG_FILE = os.path.join(REPO_ROOT, "catalog.json")

def validate():
    print(f"Scanning skills in {SKILLS_DIR}...")
    errors = []
    warnings = []
    seen_ids = {}
    total_skills = 0

    if not os.path.isdir(SKILLS_DIR):
        print("ERROR: skills directory not found!")
        sys.exit(1)

    domains = [d for d in sorted(os.listdir(SKILLS_DIR)) if os.path.isdir(os.path.join(SKILLS_DIR, d))]
    print(f"Discovered domains: {', '.join(domains)}")

    for domain in domains:
        domain_path = os.path.join(SKILLS_DIR, domain)
        skill_dirs = [s for s in sorted(os.listdir(domain_path)) if os.path.isdir(os.path.join(domain_path, s))]

        for skill_name in skill_dirs:
            total_skills += 1
            skill_path = os.path.join(domain_path, skill_name)
            skill_file = os.path.join(skill_path, "SKILL.md")

            if not os.path.isfile(skill_file):
                errors.append(f"[{domain}/{skill_name}] Missing SKILL.md file")
                continue

            # Check uniqueness
            if skill_name in seen_ids:
                errors.append(f"[{domain}/{skill_name}] Duplicate skill ID already defined in {seen_ids[skill_name]}")
            seen_ids[skill_name] = domain

            # Read content
            with open(skill_file, "r", encoding="utf-8") as f:
                content = f.read()

            # Frontmatter check
            fm_match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n(.*)$", content, re.DOTALL)
            if not fm_match:
                errors.append(f"[{domain}/{skill_name}] Missing or malformed YAML frontmatter (must start with ---)")
                continue

            fm_text = fm_match.group(1)
            body_text = fm_match.group(2).strip()

            # Name check
            name_match = re.search(r"(?m)^name:\s*(.+)$", fm_text)
            if not name_match:
                errors.append(f"[{domain}/{skill_name}] Missing 'name' in frontmatter")
            else:
                name_val = name_match.group(1).strip()
                if name_val != skill_name:
                    errors.append(f"[{domain}/{skill_name}] Frontmatter name '{name_val}' does not match directory '{skill_name}'")

            # Description check
            desc_match = re.search(r"(?s)(?m)^description:\s*(.*?)(?=\n[a-zA-Z0-9_-]+:|\Z)", fm_text)
            if not desc_match:
                errors.append(f"[{domain}/{skill_name}] Missing 'description' in frontmatter")
            else:
                desc_val = desc_match.group(1).strip()
                # Clean YAML multi-line folded block scalar markers
                desc_val = re.sub(r"^[>|-]\s*", "", desc_val).strip()
                if not desc_val:
                    errors.append(f"[{domain}/{skill_name}] 'description' is empty")
                elif len(desc_val) > 600:
                    warnings.append(f"[{domain}/{skill_name}] Description is long ({len(desc_val)} chars > 600 chars)")

            # Body check
            if not body_text:
                errors.append(f"[{domain}/{skill_name}] SKILL.md body is empty")

    # Catalog check
    if os.path.isfile(CATALOG_FILE):
        try:
            with open(CATALOG_FILE, "r", encoding="utf-8") as f:
                catalog_data = json.load(f)
            catalog_count = catalog_data.get("total_skills", 0)
            if catalog_count != total_skills:
                warnings.append(f"catalog.json count ({catalog_count}) does not match scanned skills ({total_skills})")
        except Exception as e:
            errors.append(f"catalog.json is invalid JSON: {e}")
    else:
        warnings.append("catalog.json is missing")

    # Summary
    print("-" * 60)
    print(f"Validation Summary: {total_skills} skills scanned across {len(domains)} domain(s).")

    if warnings:
        print(f"\n[!] {len(warnings)} Warning(s):")
        for w in warnings:
            print(f"  * {w}")

    if errors:
        print(f"\n[X] {len(errors)} Error(s) Found:")
        for e in errors:
            print(f"  * {e}")
        sys.exit(1)
    else:
        print("\n[OK] All skills passed validation successfully with 0 errors!")
        sys.exit(0)

if __name__ == "__main__":
    validate()
