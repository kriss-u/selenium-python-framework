from setup import load_env, parse_arguments, load_driver

if __name__ == '__main__':
    args = parse_arguments()
    load_env(args.env_file)
    driver = load_driver(args.driver)
    driver.quit()
