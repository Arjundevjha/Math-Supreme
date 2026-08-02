import re

with open('Tests/test_circle.py', 'r') as f:
    content = f.read()

# Remove imports
content = re.sub(r'import os\nimport sys\n', '', content)

# Remove sys.path block
sys_path_block = """# Fix imports
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
math_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Math"))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)
if math_dir not in sys.path:
    sys.path.insert(0, math_dir)

"""
content = content.replace(sys_path_block, '')

with open('Tests/test_circle.py', 'w') as f:
    f.write(content)
