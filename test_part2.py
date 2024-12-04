import os
import re
from modules.file_sorter import organize_files
from modules.config import FILE_CATEGORIES, DEFAULT_FOLDER

TEST_DIR = "files"
TEST_FILES = [
    "test.txt",
    "image.jpg",
    "video.mp4",
    "unknown.xyz"
]

def setup_test_environment():
    os.makedirs(TEST_DIR, exist_ok=True)
    for file_name in TEST_FILES:
        with open(os.path.join(TEST_DIR, file_name), "w") as f:
            f.write("Test content")

def test_organize_files():
    setup_test_environment()

    print("Running organize_files...")
    organize_files()

    for file_name in TEST_FILES:
        category = next(
            (cat for cat, patterns in FILE_CATEGORIES.items() if any(re.match(pattern, file_name) for pattern in patterns)),
            DEFAULT_FOLDER
        )
        category_dir = os.path.join(TEST_DIR, "..", category)
        expected_path = os.path.join(category_dir, file_name)

        print(f"DEBUG: Checking file: {file_name}")
        print(f"DEBUG: Expected category: {category}")
        print(f"DEBUG: Expected path: {expected_path}")
        print(f"DEBUG: File exists: {os.path.exists(expected_path)}")

        assert os.path.exists(expected_path), f"{file_name} was not moved to {category_dir}"

    print("All tests passed.")

if __name__ == "__main__":
    test_organize_files()
