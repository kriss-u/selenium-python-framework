import os


def create_directory(dir_path_abs):
    """
    Creates a directory if not created
    :param dir_path_abs: The absolute directory path
    :return: The absolute directory path
    """
    try:
        os.makedirs(dir_path_abs, exist_ok=True)
        return dir_path_abs
    except Exception:
        return None


def setup_screenshots(request):
    """
    Sets up the screenshots directory based on the supplied path
    If the path isn't supplied, the environment SCREENSHOTS_DIR is looked into
    Otherwise, the a screenshots directory is created in the project root

    :param request: Pytest request parameter
    :return: The absolute directory path
    """
    dir_path_arg = request.config.getoption("screenshots_dir")
    dir_path_arg = dir_path_arg and os.path.join(os.getcwd(), dir_path_arg)
    dir_path_default = os.environ.get("SCREENSHOTS_DIR") or "screenshots"
    dir_path = dir_path_arg or (dir_path_default and os.path.join(request.config.rootdir, dir_path_default))
    return create_directory(os.path.abspath(dir_path))
