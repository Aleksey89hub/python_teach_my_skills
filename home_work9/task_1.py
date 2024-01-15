import os
import platform
import shutil

print("Operation system name is: ", platform.system())
print("Print current directory: ", os.getcwd())


def get_os_name() -> str:
    return platform.system()


def get_current_folder_path() -> str:
    return os.getcwd()


def sort_file_by_extension(folder_path: str) -> dict:
    extension_mapping = {}
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()
            if file_extension not in extension_mapping:
                extension_mapping[file_extension] = []
            extension_mapping[file_extension].append(file_path)

        return extension_mapping


def move_file_to_subdirectories(extension_mapping: dict) -> dict:
    for extension, files in extension_mapping.items():
        sub_dir = os.path.join(os.getcwd(), extension[1:])
        os.makedirs(sub_dir, exist_ok=True)
        for file_path in files:
            shutil.move(file_path, sub_dir)
    return extension_mapping


if __name__ == "main":
    os_name = get_os_name()
    current_folder_path = get_current_folder_path()

    print(f"Operation system name is: {os_name}")
    print(f"Print current directory: {current_folder_path}")

    extension_mapping = sort_file_by_extension(current_folder_path)
    move_files_count = move_file_to_subdirectories(extension_mapping)