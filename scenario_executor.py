# scenario_executor.py
import json
import os
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import allure
from utils.allure_helper import start_step, attach_screenshot, attach_text, write_environment_info


def setup_browser():
    """Initialize and return a Selenium Chrome WebDriver."""
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions")

    service = Service()  # Add path to chromedriver if needed
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver


def load_scenario(file_path):
    """Load a scenario JSON file and return it as a dictionary."""
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def clear_previous_results():
    """
    Clean up old screenshots and Allure result files before a new run.
    This keeps 'output/' and 'allure-results/' folders tidy.
    """
    folders_to_clear = ["output", "allure-results"]
    for folder in folders_to_clear:
        if os.path.exists(folder):
            try:
                shutil.rmtree(folder)
                print(f"[INFO] Cleared previous files in: {folder}")
            except Exception as e:
                print(f"[WARNING] Could not clear {folder}: {e}")
        os.makedirs(folder, exist_ok=True)


@allure.feature("Scenario Execution")
def run_scenario(driver, scenario_data):
    """
    Execute scenario steps from a scenario dictionary.
    scenario_data: dict with 'steps' key containing a list of steps
    """
    # --- Clean up old data before each test run ---
    clear_previous_results()

    # --- Write environment info for Allure ---
    write_environment_info({
        "Browser": "Chrome",
        "Framework": "Selenium",
        "Report": "Allure"
    })

    steps = scenario_data.get("steps", [])

    for i, step in enumerate(steps, start=1):
        action = step.get("action")
        step_name = f"Step {i}: {action.upper()}"
        screenshot_path = os.path.join("output", f"screenshot_step_{i}.png")

        with start_step(step_name):
            try:
                if action == "go":
                    url = step.get("url")
                    if url:
                        driver.get(url)
                        attach_text("URL", url)

                elif action == "click":
                    selector = step.get("selector")
                    if selector:
                        driver.find_element(By.CSS_SELECTOR, selector).click()
                        attach_text("Clicked element", selector)

                elif action == "type":
                    selector = step.get("selector")
                    text = step.get("text", "")
                    if selector:
                        driver.find_element(By.CSS_SELECTOR, selector).send_keys(text)
                        attach_text("Typed text", f"{text} → {selector}")

                elif action == "press_enter":
                    selector = step.get("selector")
                    if selector:
                        element = driver.find_element(By.CSS_SELECTOR, selector)
                        element.send_keys(Keys.ENTER)
                        attach_text("Pressed Enter", selector)

                elif action == "screenshot":
                    path = step.get("path", screenshot_path)
                    driver.save_screenshot(path)
                    attach_screenshot(path)

                else:
                    print(f"[WARNING] Unknown action: {action}")
                    attach_text("Warning", f"Unknown action: {action}")

                # Automatically capture a screenshot after each step
                driver.save_screenshot(screenshot_path)
                attach_screenshot(screenshot_path, name=f"After {action}")

            except Exception as e:
                error_msg = f"Error in {action}: {str(e)}"
                attach_text("Error", error_msg)
                driver.save_screenshot(screenshot_path)
                attach_screenshot(screenshot_path, name=f"Error - {action}")
                raise


if __name__ == "__main__":
    scenario_file = "test_scenario.json"  # Use your scenario file
    driver = setup_browser()

    try:
        scenario_data = load_scenario(scenario_file)
        run_scenario(driver, scenario_data)
    finally:
        driver.quit()
