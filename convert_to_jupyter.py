import json
import os

def create_jupyter_notebook(markdown_content, output_path):
    """Convert markdown content to Jupyter notebook format"""
    
    # Split content into sections based on headers and code blocks
    lines = markdown_content.split('\n')
    cells = []
    current_cell = []
    in_code_block = False
    code_language = None
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Check for code block start
        if line.strip().startswith('```'):
            if in_code_block:
                # End of code block
                code_content = '\n'.join(current_cell)
                cells.append({
                    "cell_type": "code",
                    "execution_count": None,
                    "metadata": {},
                    "outputs": [],
                    "source": code_content.split('\n')
                })
                current_cell = []
                in_code_block = False
            else:
                # Start of code block
                if current_cell:
                    # Save previous markdown cell
                    markdown_content = '\n'.join(current_cell)
                    if markdown_content.strip():
                        cells.append({
                            "cell_type": "markdown",
                            "metadata": {},
                            "source": markdown_content.split('\n')
                        })
                current_cell = []
                in_code_block = True
                # Extract language if specified
                code_language = line.strip()[3:].strip()
        else:
            current_cell.append(line)
        
        i += 1
    
    # Add any remaining content
    if current_cell:
        content = '\n'.join(current_cell)
        if content.strip():
            if in_code_block:
                cells.append({
                    "cell_type": "code",
                    "execution_count": None,
                    "metadata": {},
                    "outputs": [],
                    "source": content.split('\n')
                })
            else:
                cells.append({
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": content.split('\n')
                })
    
    # Create the notebook structure
    notebook = {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {
                    "name": "ipython",
                    "version": 3
                },
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.8.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }
    
    # Write the notebook
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1, ensure_ascii=False)
    
    print(f"Created Jupyter notebook: {output_path}")

# Read the markdown content
with open('notebooks/17_swarm_fundamentals.ipynb', 'r', encoding='utf-8') as f:
    markdown_content = f.read()

# Convert to Jupyter format
create_jupyter_notebook(markdown_content, 'notebooks/17_swarm_fundamentals_proper.ipynb')

# Test if it's valid JSON
with open('notebooks/17_swarm_fundamentals_proper.ipynb', 'r') as f:
    try:
        nb = json.load(f)
        print(f"✅ Valid Jupyter notebook created with {len(nb['cells'])} cells")
    except Exception as e:
        print(f"❌ Error: {e}")
