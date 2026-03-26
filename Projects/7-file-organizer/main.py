import os


def get_unique_name(folder_path, desired_name):
    """Return a non-conflicting filename inside folder_path."""
    base, ext = os.path.splitext(desired_name)
    candidate = desired_name
    count = 1

    while os.path.exists(os.path.join(folder_path, candidate)):
        candidate = f"{base}-{count}{ext}"
        count += 1

    return candidate


def arrange_file(folder_path, ext):
    if not os.path.isdir(folder_path):
        print(f"Folder not found: {folder_path}")
        return

    files = os.listdir(folder_path)
    file_with_ext = [f for f in files if f.lower().endswith(ext.lower())]

    for i, file_name in enumerate(file_with_ext):
        old_path = os.path.join(folder_path, file_name)
        desired_name = f"photo-{i}{ext}"
        new_name = get_unique_name(folder_path, desired_name)
        new_path = os.path.join(folder_path, new_name)

        os.rename(old_path, new_path)
        print(f"Renamed: {file_name} -> {new_name}")


if __name__ == "__main__":
    target_folder = r"F:\CODE PLAYGROUND\PYTHON\Projects\7-file-organizer"
    arrange_file(target_folder, ".jpg")