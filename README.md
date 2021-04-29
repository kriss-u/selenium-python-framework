# selenium-python-framework

A testing framework using selenium in python.
---

## Setup
### Pre-requisites
Python: >= 3.7
### **[Recommended]** Create a virtual environment
* Create a virtual environment using `venv` or `virtualenv`.
* Activate the environment.

Link: https://packaging.python.org/tutorials/installing-packages/#creating-and-using-virtual-environments

### Install dependencies
```bash
python -m pip install -r requirements.txt
```

## Usage
```
usage: pytest [-U BASE_URL] [-E ENV_FILE] [-B BROWSER] [-D DRIVER]
               [-S SCREENSHOTS_DIR]

Run the selenium tests

optional arguments:
  -U URL, --base-url URL     the base URL to test
  -E ENV_FILE, --env-file ENV_FILE
                        the file where environment variables are located
                        (default: .env)
  -B BROWSER, --browser BROWSER
                        the browser to run tests on (must be on the
                        drivers.config[platform][][type])
  -D DRIVER, --driver DRIVER
                        the path of the driver (should contain gecko, chrome,
                        etc. in the filename)
  -S SCREENSHOTS_DIR, --screenshots-dir SCREENSHOTS_DIR
                        the directory path to store screenshots (default:
                        screenshots)

```
