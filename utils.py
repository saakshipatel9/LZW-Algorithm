# Saakshi Patel (801361041)

import os

def has_extension(file_path, target_extension):
    """Checks a file extension against a given extension."""
    _, file_extension = os.path.splitext(file_path)
    return file_extension.lower() == target_extension.lower()
