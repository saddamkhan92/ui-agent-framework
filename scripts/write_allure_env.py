"""
Script to write environment information for Allure reports.
Place this in: UI_agent/scripts/write_allure_env.py
"""

import sys
import os
import platform

# Ensure project root is in Python path so utils.allure_helper can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.allure_helper import write_environment_info

def main():
    """
    Gather environment information and write to allure-results/environment.properties
    """
    env = {
        "OS": platform.platform(),
        "Python": platform.python_version(),
        "Browser": os.getenv("BROWSER", "chrome"),
        "Project": "UI Agent Framework",
    }

    write_environment_info(env)
    print("Allure environment information written successfully.")

if __name__ == "__main__":
    main()
