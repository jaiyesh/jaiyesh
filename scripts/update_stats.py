import re
import os

week    = os.environ["WEEK"]
month   = os.environ["MONTH"]
year    = os.environ["YEAR"]
updated = os.environ["UPDATED"]

block = (
    "<!-- COMMIT_STATS_START -->\n"
    "| Period | Commits |\n"
    "|--------|---------|\n"
    "| Last 7 days | **" + week + "** |\n"
    "| Last 30 days | **" + month + "** |\n"
    "| Last 365 days | **" + year + "** |\n"
    "\n"
    "<sub>Auto-updated every Sunday · " + updated + "</sub>\n"
    "<!-- COMMIT_STATS_END -->"
)

with open("README.md", "r") as f:
    content = f.read()

content = re.sub(
    r"<!-- COMMIT_STATS_START -->.*?<!-- COMMIT_STATS_END -->",
    block,
    content,
    flags=re.DOTALL
)

with open("README.md", "w") as f:
    f.write(content)

print("README updated successfully")
