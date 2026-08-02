with open("Tests/test_circle.py", "r", encoding="utf-8") as f:
    content = f.read()

import re

# Remove the specific block if it exists
block = """# Fix imports
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
math_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Math"))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)
if math_dir not in sys.path:
    sys.path.insert(0, math_dir)
"""

if block in content:
    content = content.replace(block, "")

# Remove imports that might only be needed for sys.path modification
lines = content.split('\n')
new_lines = []
for line in lines:
    if line.strip() == 'import os':
        continue
    if line.strip() == 'import sys':
        continue
    new_lines.append(line)

# Handle double empty lines created by removal
import re
content = '\n'.join(new_lines)
content = re.sub(r'\n\n\n+', '\n\n', content)

with open("Tests/test_circle.py", "w", encoding="utf-8") as f:
    f.write(content.strip() + "\n")
print("Tests/test_circle.py processed")
