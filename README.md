# selenium-python-framework

A testing framework using selenium in python.
---

## Setup
### Pre-requisites
Python: >= 3.5
### **[Recommended]** Create a virtual environment *[Optional]*
* Create a virtual environment using `venv` or `virtualenv`.
* Activate the environment.

Link: https://packaging.python.org/tutorials/installing-packages/#creating-and-using-virtual-environments

### Install dependencies
```bash
python -m pip install -r requirements.txt
```

## Usage
```
usage: main.py [-h] [-u URL] [-e ENV_FILE] [-d DRIVER] [-s SCREENSHOTS_DIR]

Run the selenium tests

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     the URL to test
  -e ENV_FILE, --env-file ENV_FILE
                        the file where environment variables are located (default: .env)
  -d DRIVER, --driver DRIVER
                        the path of the driver (should contain gecko, chrome, etc. in the filename)
  -s SCREENSHOTS_DIR, --screenshots-dir SCREENSHOTS_DIR
                        the directory path to store screenshots (default: screenshots)

```
