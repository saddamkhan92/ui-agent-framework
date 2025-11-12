# tests/test_scenario_executor.py
import os
import pytest
from scenario_executor import setup_browser, load_scenario, run_scenario
from utils.allure_helper import write_environment_info, start_step, attach_screenshot

@pytest.fixture
def driver():
    """Setup and teardown of the browser driver."""
    driver = setup_browser()
    yield driver
    driver.quit()

@pytest.mark.parametrize("scenario_file", ["test_scenario.json"])
def test_duckduckgo_search(driver, scenario_file):
    """
    Run DuckDuckGo search scenario and generate Allure report.
    """
    # --- Allure environment info ---
    env_info = {
        "Browser": "Chrome",
        "Framework": "Selenium + Pytest + Allure",
        "Scenario": scenario_file
    }
    write_environment_info(env_info)

    # --- Ensure output directory exists ---
    os.makedirs("output", exist_ok=True)

    # --- Load and run scenario ---
    with start_step(f"Load scenario: {scenario_file}"):
        scenario_data = load_scenario(scenario_file)

    with start_step("Execute scenario actions"):
        run_scenario(driver, scenario_data)

    # --- Attach final screenshot to Allure report ---
    screenshot_path = "output/final_state.png"
    driver.save_screenshot(screenshot_path)
    attach_screenshot(screenshot_path, "Final Screenshot")
