# conftest.py
import sys
import os
import pytest
import allure
from scenario_executor import setup_browser, load_scenario
from utils.allure_helper import write_environment_info

# Add project root to sys.path so imports work
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


@pytest.fixture(scope="session")
def driver():
    """Initialize Chrome driver once per test session."""
    driver = setup_browser()
    yield driver
    driver.quit()


@pytest.fixture(scope="session", autouse=True)
def environment_info():
    """Write Allure environment info once per session."""
    env_info = {
        "Browser": "Chrome",
        "Environment": "Local",
        "Tester": "UI Agent Framework"
    }
    write_environment_info(env_info)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to attach screenshot to Allure report if test fails
    or to attach screenshots taken manually in the scenario.
    """
    outcome = yield
    rep = outcome.get_result()

    # Only act after the test has finished
    if rep.when == "call":
        driver = item.funcargs.get("driver")
        # Attach a full-page screenshot after test
        if driver:
            screenshot_path = os.path.join(PROJECT_ROOT, "output", f"{item.name}.png")
