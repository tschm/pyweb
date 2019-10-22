# add this in the conftest.py under tests folder
from selenium.webdriver.chrome.options import Options


def pytest_setup_options():
    options = Options()
    options.add_argument("--disable-extensions")     # disabling extensions
    options.add_argument("--disable-dev-shm-usage")  # overcome limited resource problems
    options.add_argument("--no-sandbox")             # Bypass OS security  model
    options.add_argument("--headless")               # headless?
    return options