# Cheapest Flights Within K Stops

This is a Python console application that finds the cheapest flight path between two cities with a maximum of k stops. It reads flight data and search parameters from an input.json file and outputs the result to the terminal.

## Features

-   Finds cheapest flight price with stop limit.
-   Input via input.json.
-   Console output.
-   Includes unit tests.

## Prerequisites

-   **Python 3.9+** (preferably 3.11/3.12).
-   **Visual Studio Code (VS Code)** with **Python Extension**.
-   **For macOS:** Homebrew & Xcode Command Line Tools.
-   **For Windows:** A standard Python installation (from python.org or Anaconda).

## Getting Started (Quick Setup)

First, navigate to your project folder in your terminal (e.g., cd CheapestFlightsApp).

### macOS Setup

1.  Install Xcode Command Line Tools:
    run in terminal: xcode-select --install
2.  Install Homebrew: (If not installed, run the command from https://brew.sh)
    run in terminal: /bin/bash -c "$(curl -fsSL ...)"
3.  Install Python 3.11:
    run in terminal: brew install python@3.11
4.  Create & Activate Virtual Environment:
    run in terminal: /opt/homebrew/opt/python@3.11/bin/python3.11 -m venv .venvsource ./.venv/bin/activate
5.  **Configure VS Code:** Open project in VS Code, click the Python version in the bottom-left status bar, select the (.venv) interpreter, and Reload Window.

### Windows Setup

1.  **Install Python 3.11:** Download and run the installer from [python.org](https://www.python.org/downloads/windows/). Ensure you check "Add Python to PATH" during installation.
2.  **Install VS Code** and the **Python Extension** if you haven't already.
3.  Create & Activate Virtual Environment:
    Open Command Prompt (cmd) or PowerShell in your project folder.
    run: python -m venv .venv
    Then, to activate: run :
    .venv\\Scripts\\activate # For Command Prompt (cmd)
    or PowerShell
    .\\.venv\\Scripts\\Activate.ps1 # For PowerShell
4.  **Configure VS Code:** Open project in VS Code, click the Python version in the bottom-left status bar, select the (.venv) interpreter, and Reload Window.

## How to Run the Application

1.  **Edit input_example\*.json** with your desired flight parameters.
2.  **Run app.py:**
    -   **In VS Code:** Open app.py and click the green "Run" triangle.
    -   **In Terminal (with venv active):** python app.py

## How to Run Tests

1.  **Configure Tests in VS Code:** Go to Command Palette (Cmd+Shift+P), select Python: Configure Tests, choose unittest, root directory ., and pattern test\*.py.
2.  **Run Tests:** Go to the "Testing" view (beaker icon in sidebar) and click the "Run Tests" play button.
