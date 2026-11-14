import os
import shutil

src_repo = os.path.join(os.environ["TEMP"], "emilkowalski-skills")
dst_repo = r"D:\skills"

# 1. Target folders
skills_src = os.path.join(src_repo, "skills")
skills_dst = os.path.join(dst_repo, "skills", "design-engineering")
docs_dst = os.path.join(dst_repo, "docs", "design-engineering")
rules_dst = os.path.join(dst_repo, "rules")
agents_rules_dst = os.path.join(dst_repo, ".agents", "rules")

os.makedirs(skills_dst, exist_ok=True)
os.makedirs(docs_dst, exist_ok=True)
os.makedirs(rules_dst, exist_ok=True)
os.makedirs(agents_rules_dst, exist_ok=True)

# 2. Copy all skill folders with companion files
count = 0
for folder in sorted(os.listdir(skills_src)):
    s_path = os.path.join(skills_src, folder)
    d_path = os.path.join(skills_dst, folder)
    if os.path.isdir(s_path):
        shutil.copytree(s_path, d_path, dirs_exist_ok=True)
        count += 1
        print(f"Copied skill: {folder}")

print(f"Successfully copied {count} skills to {skills_dst}")

# 3. Copy cheatsheets to docs/design-engineering
perf_src = os.path.join(src_repo, "performance-cheatsheet.md")
ui_src = os.path.join(src_repo, "ui-cheatsheet.md")
readme_src = os.path.join(src_repo, "README.md")

if os.path.isfile(perf_src):
    shutil.copy2(perf_src, os.path.join(docs_dst, "performance-cheatsheet.md"))
if os.path.isfile(ui_src):
    shutil.copy2(ui_src, os.path.join(docs_dst, "ui-cheatsheet.md"))
print("Copied cheatsheets to docs/design-engineering/")

# 4. Copy standards to rules
standards_src = os.path.join(src_repo, "skills", "review-animations", "STANDARDS.md")
if os.path.isfile(standards_src):
    shutil.copy2(standards_src, os.path.join(rules_dst, "design-engineering.md"))
    shutil.copy2(standards_src, os.path.join(agents_rules_dst, "design-engineering.md"))
    print("Copied animation standards to rules/ and .agents/rules/")
