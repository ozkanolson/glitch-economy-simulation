#!/usr/bin/env python3
"""
Convert all project files into a single .txt file.
"""

import os
from pathlib import Path

# Configuration
PROJECT_ROOT = Path(__file__).parent
OUTPUT_FILE = PROJECT_ROOT / "project_combined.txt"
SKIP_DIRS = {".git", "__pycache__", "txt_output", ".venv", "node_modules"}
SKIP_FILES = {".DS_Store", ".gitkeep", "convert_to_txt.py", "project_combined.txt"}


def convert_to_txt():
    """Combine all files into a single txt file."""
    all_content = []
    file_count = 0

    for root, dirs, files in os.walk(PROJECT_ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        root_path = Path(root)

        for filename in sorted(files):
            if filename in SKIP_FILES:
                continue

            source_file = root_path / filename
            relative_path = source_file.relative_to(PROJECT_ROOT)

            try:
                with open(source_file, "r", encoding="utf-8") as f:
                    content = f.read()

                all_content.append(f"{'=' * 60}")
                all_content.append(f"FILE: {relative_path}")
                all_content.append(f"{'=' * 60}\n")
                all_content.append(content)
                all_content.append("\n")

                file_count += 1
                print(f"Added: {relative_path}")

            except UnicodeDecodeError:
                print(f"Skipped (binary): {relative_path}")
            except Exception as e:
                print(f"Error: {relative_path} - {e}")

    # Write combined file
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(all_content))

    print(f"\nDone! Combined {file_count} files into {OUTPUT_FILE.name}")


if __name__ == "__main__":
    convert_to_txt()
