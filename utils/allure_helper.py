import os
import allure

def start_step(step_name: str):
    """
    Context manager to define a named step in Allure.
    Usage:
        with start_step("Open Website"):
            driver.get("https://example.com")
    """
    return allure.step(step_name)


def attach_screenshot(file_path: str, name: str = "Screenshot"):
    """
    Attach a screenshot image to the Allure report.
    """
    try:
        with open(file_path, "rb") as image_file:
            allure.attach(
                image_file.read(),
                name=name,
                attachment_type=allure.attachment_type.PNG
            )
    except Exception as e:
        allure.attach(
            str(e),
            name="screenshot_error",
            attachment_type=allure.attachment_type.TEXT
        )


def attach_text(name: str, content: str):
    """
    Attach text, logs, or details to the Allure report.
    """
    allure.attach(
        content,
        name=name,
        attachment_type=allure.attachment_type.TEXT
    )


def write_environment_info(env_info: dict):
    """
    Write Allure environment.properties file for display in the report.
    """
    allure_results_dir = "allure-results"
    os.makedirs(allure_results_dir, exist_ok=True)

    env_file_path = os.path.join(allure_results_dir, "environment.properties")

    with open(env_file_path, "w", encoding="utf-8") as f:
        for key, value in env_info.items():
            f.write(f"{key}={value}\n")
