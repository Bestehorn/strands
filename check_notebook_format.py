import os

# Check the format of existing notebooks
notebook_path = 'notebooks/01_getting_started.ipynb'

# Read the first few lines
with open(notebook_path, 'r', encoding='utf-8') as f:
    content = f.read()
    
# Print the first 500 characters
print("First 500 characters of the notebook:")
print(content[:500])
print("\n" + "="*50 + "\n")

# Check if it's JSON
try:
    import json
    json_content = json.loads(content)
    print("The notebook is valid JSON format")
    print(f"Keys in JSON: {list(json_content.keys())}")
except:
    print("The notebook is NOT JSON format")
    
# Check first character
print(f"\nFirst character: '{content[0]}' (ASCII: {ord(content[0])})")
