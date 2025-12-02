# saucedemo-ui-automation
Test Automation Framework for SauceDemo using Python, Selenium WebDriver, Pytest, and Page Object Model design pattern.
# Python Selenium POM Framework - SauceDemo

## Portfolio Project: UI Automation Framework

This project is a **Test Automation Framework** built from scratch using Python, focused on User Interface (UI) testing for the **SauceDemo (Swag Labs)** e-commerce demonstration application.

The framework is designed to showcase the ability to develop **scalable, maintainable, and readable** test code using industry-standard design patterns.

* **Target Application:** https://www.saucedemo.com/
* **Design Pattern:** Page Object Model (POM)

### Implemented Tests

This framework automates critical business flows:

* **Successful Login:** Verifies successful login using the standard user credentials.
* **Failed Login:** Confirms the appropriate error message for invalid credentials.
* **End-to-End E-commerce Flow:**
    * Product selection and addition to the cart.
    * Complete Checkout process.
    * Verification of order completion confirmation.

***

### Tech Stack

| Tool | Category | Primary Purpose |
| :--- | :--- | :--- |
| **Python 3.x** | Language | Core framework development language. |
| **Selenium WebDriver** | UI Automation | Interaction with browser elements (clicks, inputs, navigation). |
| **Pytest** | Testing Framework | Test execution, assertion handling, and fixture management. |
| **Page Object Model (POM)** | Design Pattern | Structure for code reusability and maintenance. |
| **webdriver-manager** | Utility | Automatic handling and download of Chrome/Gecko Drivers. |
| **pytest-html** | Reporting | Generation of comprehensive, human-readable test reports. |
