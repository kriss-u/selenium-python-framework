import time

from screenshots import setup_screenshots
from setup import load_env, parse_arguments, load_driver

if __name__ == '__main__':
    args = parse_arguments()
    load_env(args.env_file)
    dirname = setup_screenshots(args.screenshots_dir)
    print(f"Directory for screenshots: {dirname}")
    driver = load_driver(args.driver, args.browser)
    time.sleep(5)
    driver.quit()
