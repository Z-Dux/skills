#!/usr/bin/env python3
"""
Regenerates catalog.json from all skills across all domains in the repository.
"""

import os
import re
import json

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS_DIR = os.path.join(REPO_ROOT, "skills")
DOCS_DIR = os.path.join(REPO_ROOT, "docs")
CATALOG_FILE = os.path.join(REPO_ROOT, "catalog.json")

def generate_catalog():
    catalog = []
    domains = [d for d in sorted(os.listdir(SKILLS_DIR)) if os.path.isdir(os.path.join(SKILLS_DIR, d))]
    
    # Category mappings from docs if available
    category_map = {}
    if os.path.isdir(DOCS_DIR):
        for domain in os.listdir(DOCS_DIR):
            dom_docs = os.path.join(DOCS_DIR, domain)
            if os.path.isdir(dom_docs):
                for sub in os.listdir(dom_docs):
                    sub_path = os.path.join(dom_docs, sub)
                    if os.path.isdir(sub_path):
                        for f in os.listdir(sub_path):
                            if f.endswith(".md"):
                                category_map[f[:-3]] = sub

    for domain in domains:
        domain_dir = os.path.join(SKILLS_DIR, domain)
        skill_dirs = [s for s in sorted(os.listdir(domain_dir)) if os.path.isdir(os.path.join(domain_dir, s))]

        for skill_name in skill_dirs:
            skill_path = os.path.join(domain_dir, skill_name, "SKILL.md")
            if not os.path.isfile(skill_path):
                continue

            with open(skill_path, "r", encoding="utf-8") as f:
                content = f.read()

            desc_match = re.search(r"(?s)^---\n.*?description:\s*(.*?)\n(?:---|\w+:)", content)
            title_match = re.search(r"(?m)^#\s+(.+)$", content)

            desc = desc_match.group(1).strip() if desc_match else ""
            desc = re.sub(r"^[>|-]\s*", "", desc).strip()
            title = title_match.group(1).strip() if title_match else skill_name

            catalog.append({
                "id": skill_name,
                "name": title,
                "domain": domain,
                "category": category_map.get(skill_name, "general"),
                "description": desc,
                "path": f"skills/{domain}/{skill_name}/SKILL.md"
            })

    data = {
        "version": "1.0.0",
        "total_skills": len(catalog),
        "domains": domains,
        "skills": catalog
    }

    with open(CATALOG_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print(f"Successfully generated catalog.json with {len(catalog)} skills across {len(domains)} domain(s).")

if __name__ == "__main__":
    generate_catalog()
