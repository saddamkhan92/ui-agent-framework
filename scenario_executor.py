import json
import time
import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils.allure_helper import start_step, attach_screenshot, attach_text, write_environment_info


def load_scenario(file_path="test_scenario.json"):
    """
    Load a JSON test scenario file.
    """
    with open(file_path, "r") as f:
        return json.load(f)


def setup_browser():
    """
    Initialize Selenium WebDriver (Chrome).
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    return driver


def run_scenario(driver, scenario):
    """
    Execute steps defined in the scenario.
    """
    steps = scenario.get("steps", [])

    for step in steps:
        action = step.get("action")
        description = f"Performing action: {action}"

        with start_step(description):
            try:
                if action == "go":
                    url = step["url"]
                    driver.get(url)
                    attach_text("Navigated URL", f"Opened: {url}")

                elif action == "type":
                    selector = step["selector"]
                    text = step["text"]
                    element = driver.find_element(By.CSS_SELECTOR, selector)
                    element.send_keys(text)
                    attach_text("Typed Text", f"Typed '{text}' into {selector}")

                elif action == "press_enter":
                    selector = step["selector"]
                    element = driver.find_element(By.CSS_SELECTOR, selector)
                    element.send_keys(Keys.RETURN)
                    attach_text("Action", f"Pressed Enter on {selector}")
                    time.sleep(2)

                elif action == "screenshot":
                    path = step.get("path", "output/screenshot.png")
                    os.makedirs(os.path.dirname(path), exist_ok=True)
                    driver.save_screenshot(path)
                    attach_screenshot(path, name=f"Screenshot - {os.path.basename(path)}")

                else:
                    attach_text("Unknown Step", f"Unknown action: {action}")

            except Exception as e:
                attach_text("Error", f"Error during step '{action}': {str(e)}")
                raise


@pytest.fixture(scope="session")
def driver():
    """
    Pytest fixture to initialize and close the browser.
    """
    driver = setup_browser()
    yield driver
    driver.quit()


def test_run_ui_scenario(driver):
    """
    Main pytest test that runs the scenario and generates Allure report data.
    """
    scenario = load_scenario("test_scenario.json")
    env_info = {
        "Browser": "Chrome",
        "Environment": "Local",
        "Tester": "UI Agent Framework",
    }
    write_environment_info(env_info)

    run_scenario(driver, scenario)
