import os
import allure
import traceback


class StepError(Exception):
    """Custom exception to wrap step-level errors."""
    pass


class start_step:
    """
    Context manager to define a named step in Allure reports.
    Usage:
        with start_step("Open website"):
            driver.get("https://example.com")
    """

    def __init__(self, step_name, browser=None):
        self.step_name = step_name
        self.browser = browser

    def __enter__(self):
        self.allure_step = allure.step(self.step_name)
        self.allure_step.__enter__()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # If there’s an error inside this step, capture screenshot + traceback
        if exc_type is not None:
            if self.browser:
                try:
                    screenshot_path = "allure-results/error_screenshot.png"
                    self.browser.save_screenshot(screenshot_path)
                    attach_screenshot(screenshot_path, name=f"Error - {self.step_name}")
                except Exception as e:
                    allure.attach(
                        str(e),
                        name="screenshot_capture_failed",
                        attachment_type=allure.attachment_type.TEXT
                    )

            tb = "".join(traceback.format_exception(exc_type, exc_val, exc_tb))
            attach_text("Exception Traceback", tb)
            self.allure_step.__exit__(exc_type, exc_val, exc_tb)
            raise StepError(f"Step failed: {self.step_name}") from exc_val

        self.allure_step.__exit__(exc_type, exc_val, exc_tb)
        return False  # Do not suppress exceptions


def attach_screenshot(file_path: str, name: str = "Screenshot"):
    """Attach a screenshot to the Allure report."""
    try:
        with open(file_path, "rb") as image_file:
            allure.attach(
                image_file.read(),
                name=name,
                attachment_type=allure.attachment_type.PNG
            )
    except Exception as e:
        allure.attach(
            f"Failed to attach screenshot: {e}",
            name="screenshot_error",
            attachment_type=allure.attachment_type.TEXT
        )


def attach_text(name: str, content: str):
    """Attach text/logs to the Allure report."""
    allure.attach(
        content,
        name=name,
        attachment_type=allure.attachment_type.TEXT
    )


def write_environment_info(env_info: dict):
    """Write Allure environment.properties file for display in report."""
    allure_results_dir = "allure-results"
    os.makedirs(allure_results_dir, exist_ok=True)

    env_file_path = os.path.join(allure_results_dir, "environment.properties")

    with open(env_file_path, "w", encoding="utf-8") as f:
        for key, value in env_info.items():
            f.write(f"{key}={value}\n")
