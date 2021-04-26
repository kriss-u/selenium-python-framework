import os
import traceback


def create_directory(dir_path_abs):
    """
    Creates a directory if not created
    :param dir_path_abs: The absolute directory path
    :return: The absolute directory path
    """
    try:
        if not os.path.isdir(dir_path_abs):
            print("Directory not found, creating one for you.")
        else:
            print("Directory found, using it for screenshots.")
        os.makedirs(dir_path_abs, exist_ok=True)
        return dir_path_abs
    except Exception:
        traceback.print_exc()
        print("Directory creation failed."
              "Cannot use screenshots")
        return None


def setup_screenshots(dir_path):
    """
    Sets up the screenshots directory based on the supplied path
    If the path isn't supplied, the environment SCREENSHOTS_DIR is looked into
    Otherwise, the a screenshots directory is created in the project root

    :param dir_path: directory path supplied by user (can be relative or absolute)
    :return: The absolute directory path
    """
    if dir_path is None or dir_path == "":
        if "SCREENSHOTS_DIR" in os.environ:
            dir_path_env = os.environ["SCREENSHOTS_DIR"]
            if dir_path_env != "":
                dir_path_env = os.path.abspath(dir_path_env)
                return create_directory(dir_path_env)
            else:
                dir_path_local = os.path.abspath(os.path.join(os.path.dirname(__file__), "screenshots"))
                return create_directory(dir_path_local)

    dir_path_abs = os.path.abspath(dir_path)
    return create_directory(dir_path_abs)
