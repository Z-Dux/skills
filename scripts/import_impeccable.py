import os
import shutil

src_skill = os.path.join(os.environ["TEMP"], "impeccable", ".agents", "skills", "impeccable")
dst_repo = r"D:\skills"

dst_skill = os.path.join(dst_repo, "skills", "frontend-design", "impeccable")
docs_dst = os.path.join(dst_repo, "docs", "frontend-design")
rules_dst = os.path.join(dst_repo, "rules")
agents_rules_dst = os.path.join(dst_repo, ".agents", "rules")

os.makedirs(dst_skill, exist_ok=True)
os.makedirs(docs_dst, exist_ok=True)
os.makedirs(rules_dst, exist_ok=True)
os.makedirs(agents_rules_dst, exist_ok=True)

print(f"Copying impeccable skill from {src_skill} to {dst_skill}...")
shutil.copytree(src_skill, dst_skill, dirs_exist_ok=True)
print("Finished copying impeccable skill package.")

# Copy craft floor to rules
craft_src = os.path.join(src_skill, "reference", "craft-floor.md")
if os.path.isfile(craft_src):
    shutil.copy2(craft_src, os.path.join(rules_dst, "impeccable-craft.md"))
    shutil.copy2(craft_src, os.path.join(agents_rules_dst, "impeccable-craft.md"))
    print("Copied craft floor to rules/ and .agents/rules/")
