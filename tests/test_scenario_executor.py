import sys
import os
import pytest
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from scenario_executor import run_scenario, load_scenario, setup_browser
from utils.allure_helper import write_environment_info

# ✅ Add the project root to sys.path so imports like "utils" work
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# ✅ Now these imports will work
from scenario_executor import run_scenario
from utils.allure_helper import attach_screenshot, attach_text


@pytest.fixture(scope="session")
def driver():
    """
    Fixture to initialize and quit the browser once per test session.
    """
    driver = setup_browser()
    yield driver
    driver.quit()


@pytest.mark.parametrize("scenario_file", ["test_scenario.json"])
def test_duckduckgo_search(driver, scenario_file):
    """
    Runs the DuckDuckGo search scenario and generates Allure report.
    """
    # Load scenario data from JSON
    scenario = load_scenario(scenario_file)

    # Write environment details
    env_info = {
        "Browser": "Chrome",
        "Environment": "Local",
        "Tester": "UI Agent Framework"
    }
    write_environment_info(env_info)

    # Run the scenario steps using Selenium
    run_scenario(driver, scenario)
