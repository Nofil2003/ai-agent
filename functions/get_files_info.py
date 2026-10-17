import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        working_directory_abs = os.path.abspath(working_directory)

        target_dir = os.path.normpath(os.path.join(working_directory_abs, directory))

        valid_target_dir = (
            os.path.commonpath([working_directory_abs, target_dir])
            == working_directory_abs
        )

        if valid_target_dir:
            if not os.path.isdir(target_dir):
                return f'Error: "{directory}" is not a directory'
            result = []
            dir_list = os.listdir(target_dir)
            for d in dir_list:
                full_path = os.path.join(target_dir, d)
                is_dir = os.path.isdir(full_path)
                size = os.path.getsize(full_path)
                res = f"\t- {d}: file_size={size} bytes, is_dir={is_dir}"
                result.append(res)
            combined_result = "\n".join(result)
            return combined_result
        else:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    except Exception as e:
        return f"Error: {e}"
