from browser import BrowserWrapper
import json

def run_scenario(file_path):
    with open(file_path, "r") as f:
        scenario = json.load(f)

    browser = BrowserWrapper()

    for step in scenario["steps"]:
        action = step["action"]
        print(f"Running step: {action}")

        if action == "go":
            browser.go(step["url"])
        elif action == "click":
            browser.click(step["selector"])
        elif action == "type":
            browser.type(step["selector"], step["text"])
        elif action == "press_enter":
            from selenium.webdriver.common.keys import Keys
            elem = browser.driver.find_element("css selector", step["selector"])
            elem.send_keys(Keys.RETURN)
        elif action == "screenshot":
            browser.screenshot(step["path"])
        else:
            print(f"Unknown action: {action}")

    browser.close()

if __name__ == "__main__":
    run_scenario("test_scenario.json")
