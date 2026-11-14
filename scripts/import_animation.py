import os
import shutil
import re
import json

src_dir = r"C:\Users\aswin\.gemini\config\plugins\animation-principles"
dst_dir = r"D:\skills"

# 1. Target folders
skills_dst = os.path.join(dst_dir, "skills", "animation")
docs_dst = os.path.join(dst_dir, "docs", "animation")
rules_dst = os.path.join(dst_dir, "rules")
agents_dir = os.path.join(dst_dir, ".agents")
agents_rules_dir = os.path.join(agents_dir, "rules")

os.makedirs(skills_dst, exist_ok=True)
os.makedirs(docs_dst, exist_ok=True)
os.makedirs(rules_dst, exist_ok=True)
os.makedirs(agents_rules_dir, exist_ok=True)

# 2. Map categories from docs
category_map = {}
src_docs = os.path.join(src_dir, "docs")
if os.path.exists(src_docs):
    for cat_folder in os.listdir(src_docs):
        cat_path = os.path.join(src_docs, cat_folder)
        if os.path.isdir(cat_path):
            for doc_file in os.listdir(cat_path):
                if doc_file.endswith(".md"):
                    skill_id = doc_file[:-3]
                    category_map[skill_id] = cat_folder

# 3. Copy and normalize skills
src_skills = os.path.join(src_dir, "skills")
skills_count = 0
fixed_names = []
catalog = []

for folder in sorted(os.listdir(src_skills)):
    src_skill_file = os.path.join(src_skills, folder, "SKILL.md")
    if os.path.isfile(src_skill_file):
        dst_skill_dir = os.path.join(skills_dst, folder)
        os.makedirs(dst_skill_dir, exist_ok=True)
        dst_skill_file = os.path.join(dst_skill_dir, "SKILL.md")
        
        with open(src_skill_file, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Parse frontmatter
        name_match = re.search(r"(?m)^name:\s*(.+)$", content)
        desc_match = re.search(r"(?s)^---\n.*?description:\s*(.*?)\n(?:---|\w+:)", content)
        
        name_val = name_match.group(1).strip() if name_match else folder
        desc_val = desc_match.group(1).strip() if desc_match else ""
        
        # Normalize name if mismatched
        if name_val != folder:
            content = re.sub(r"(?m)^name:\s*.+$", f"name: {folder}", content, count=1)
            fixed_names.append((folder, name_val))
            
        with open(dst_skill_file, "w", encoding="utf-8") as f:
            f.write(content)
            
        skills_count += 1
        
        # Extract title
        title_match = re.search(r"(?m)^#\s+(.+)$", content)
        title_val = title_match.group(1).strip() if title_match else folder
        
        catalog.append({
            "id": folder,
            "name": title_val,
            "domain": "animation",
            "category": category_map.get(folder, "general"),
            "description": desc_val,
            "path": f"skills/animation/{folder}/SKILL.md"
        })

print(f"Imported {skills_count} skills into {skills_dst}")
print(f"Fixed {len(fixed_names)} frontmatter name mismatches:")
for orig, prev in fixed_names:
    print(f"  - {orig}: changed from '{prev}' to '{orig}'")

# 4. Copy docs
if os.path.exists(src_docs):
    for item in os.listdir(src_docs):
        s = os.path.join(src_docs, item)
        d = os.path.join(docs_dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)
    print(f"Copied documentation to {docs_dst}")

# 5. Copy rules
src_rules_file = os.path.join(src_dir, "rules", "AGENTS.md")
if os.path.isfile(src_rules_file):
    shutil.copy2(src_rules_file, os.path.join(rules_dst, "AGENTS.md"))
    shutil.copy2(src_rules_file, os.path.join(rules_dst, "animation-principles.md"))
    shutil.copy2(src_rules_file, os.path.join(agents_rules_dir, "AGENTS.md"))
    print("Copied rules to rules/ and .agents/rules/")

# 6. Write catalog.json
catalog_path = os.path.join(dst_dir, "catalog.json")
with open(catalog_path, "w", encoding="utf-8") as f:
    json.dump({
        "version": "1.0.0",
        "total_skills": len(catalog),
        "domains": ["animation"],
        "skills": catalog
    }, f, indent=2)
print(f"Wrote catalog.json with {len(catalog)} entries")
