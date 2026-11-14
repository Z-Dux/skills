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

DESIGN_ENG_CATEGORIES = {
    "animate": "motion-implementation",
    "animate-expo": "mobile-motion",
    "choreograph": "motion-implementation",
    "gestures": "motion-implementation",
    "animation-performance": "performance",
    "emil-design-eng": "design-philosophy",
    "learn-taste": "design-philosophy",
    "apple-design": "design-philosophy",
    "review-animations": "audit-review",
    "improve-animations": "audit-review",
    "find-animation-opportunities": "audit-review",
    "remove-animations": "audit-review",
    "break-ui": "testing-iteration",
    "prototype": "testing-iteration",
    "pick-ui-library": "libraries-stack",
    "ask-sonner": "libraries-stack",
    "mobile-native": "platform-native",
    "write-swift": "platform-native",
    "animation-vocabulary": "reference"
}

FRONTEND_DESIGN_CATEGORIES = {
    "design-taste-frontend": "anti-slop-web-design",
    "impeccable": "design-vocabulary-review"
}

SPECIAL_TITLES = {
    "impeccable": "Impeccable Design Vocabulary",
    "design-taste-frontend": "Taste Skill (tasteskill 2.5)"
}

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
            desc = desc.strip('"\'')
            
            if skill_name in SPECIAL_TITLES:
                title = SPECIAL_TITLES[skill_name]
            elif title_match:
                title = title_match.group(1).strip()
            else:
                title = skill_name

            category = category_map.get(skill_name)
            if not category and domain == "design-engineering":
                category = DESIGN_ENG_CATEGORIES.get(skill_name, "general")
            elif not category and domain == "frontend-design":
                category = FRONTEND_DESIGN_CATEGORIES.get(skill_name, "frontend-design")
            elif not category:
                category = "general"

            catalog.append({
                "id": skill_name,
                "name": title,
                "domain": domain,
                "category": category,
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

    print(f"Successfully generated catalog.json with {len(catalog)} skills across {len(domains)} domain(s): {', '.join(domains)}.")

if __name__ == "__main__":
    generate_catalog()
