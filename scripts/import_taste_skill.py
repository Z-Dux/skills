import os
import shutil

src_skill = os.path.join(os.environ["TEMP"], "taste-skill", "skills", "taste-skill")
dst_repo = r"D:\skills"

dst_skill = os.path.join(dst_repo, "skills", "frontend-design", "design-taste-frontend")
docs_dst = os.path.join(dst_repo, "docs", "frontend-design")
rules_dst = os.path.join(dst_repo, "rules")
agents_rules_dst = os.path.join(dst_repo, ".agents", "rules")

os.makedirs(dst_skill, exist_ok=True)
os.makedirs(docs_dst, exist_ok=True)
os.makedirs(rules_dst, exist_ok=True)
os.makedirs(agents_rules_dst, exist_ok=True)

print(f"Copying taste-skill from {src_skill} to {dst_skill}...")
shutil.copytree(src_skill, dst_skill, dirs_exist_ok=True)
print("Finished copying taste-skill package.")
