import os


def get_file_content(working_directory: str, file_path: str) -> str:

    try:
        base = os.path.abspath(working_directory)
        target = os.path.abspath(os.path.join(working_directory, file_path))
        if not target.startswith(base):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        MAX_CHARS = 10000
        with open(target, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            # After reading the first MAX_CHARS...
            if f.read(1):
                file_content_string += (
                    f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                )

    except Exception as e:
        return f"Error: {e}"
    return file_content_string
