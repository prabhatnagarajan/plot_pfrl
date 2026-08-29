import os

def get_top_level_directories(directory_path):
    if not os.path.exists(directory_path):
        print(f"The specified directory '{directory_path}' does not exist.")
        return []

    # Get a list of all entries in the specified directory
    entries = os.listdir(directory_path)

    # Filter out only directories from the entries
    directories = [entry for entry in entries if os.path.isdir(os.path.join(directory_path, entry))]

    return directories

def find_file_fail(filename, directory):
    for root, dirs, files in os.walk(directory):
        if filename in files:
            return os.path.join(root, filename)
    return None

def find_file(filename, directory):
    for root, dirs, files in os.walk(directory):
        if filename in files:
            return os.path.join(root, filename)
    assert False, f"File not found: directory: {directory}, filename: {filename}"

def find_all_files(filename, directory):
    found_files = []
    for root, dirs, files in os.walk(directory):
        if filename in files:
            found_files.append(os.path.join(root, filename))
    return found_files

def insert_space_before_capital(s):
    result = s[0]  # Keep the first character as it is
    for char in s[1:]:
        if char.isupper():
            result += ' ' + char
        else:
            result += char
    return result

def remove_spaces(org_str):
    return org_str.replace(" ", "")
