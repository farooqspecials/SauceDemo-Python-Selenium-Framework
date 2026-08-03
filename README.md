# SauceDemo Python Selenium Automation Framework

A production-style UI Test Automation Framework built using **Python**, **Selenium WebDriver**, and **Pytest**, following the **Page Object Model (POM)** design pattern.

This framework automates the core user workflows of the SauceDemo web application while demonstrating industry-standard automation practices, Continuous Integration (CI), Docker containerization, and cross-browser testing.

---

# Project Highlights

- Selenium WebDriver with Python
- Page Object Model (POM)
- Data-Driven Testing using JSON
- Parameterized Testing
- Cross-Browser Testing (Chrome & Firefox)
- Dockerized Test Execution
- Jenkins CI Pipeline
- GitHub Actions CI Pipeline
- HTML Test Reports
- Automatic Screenshot Capture on Test Failure
- Clean & Scalable Framework Structure

---

# Tech Stack

- Python 3.11+
- Selenium WebDriver
- Pytest
- WebDriver Manager
- Page Object Model (POM)
- Explicit Waits
- JSON Test Data
- pytest-html
- Docker
- Jenkins
- GitHub Actions
- Git & GitHub

---

# Project Structure

```text
SauceDemoFramework/
│
├── data/
│   └── login_data.json
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── checkout_overview_page.py
│   └── menu_page.py
│
├── tests/
│   ├── test_cart.py
│   ├── test_cart_page.py
│   ├── test_checkout.py
│   ├── test_finish_order.py
│   ├── test_launch.py
│   ├── test_login.py
│   ├── test_login_json.py
│   ├── test_login_parameterized.py
│   ├── test_logout.py
│   └── test_remove_cart.py
│
├── utils/
│   └── json_reader.py
│
├── reports/
├── screenshots/
│
├── .github/
│   └── workflows/
│       └── selenium.yml
│
├── Dockerfile
├── Jenkinsfile
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

# Framework Features

- Page Object Model (POM)
- Reusable BasePage
- Shared WebDriver Fixture
- Explicit Waits
- Data-Driven Testing using JSON
- Parameterized Tests
- Cross-Browser Execution (Chrome & Firefox)
- Automatic Screenshot Capture on Test Failure
- HTML Test Reports
- Docker Support
- Jenkins Continuous Integration
- GitHub Actions Continuous Integration
- Clean Project Structure
- Git Version Control

---

# Implemented Test Scenarios

## Login

- Successful Login
- Data-Driven Login
- Parameterized Login Tests

---

## Inventory

- Verify Inventory Page
- Add Backpack to Cart
- Remove Backpack from Cart

---

## Cart

- Verify Product Appears in Cart

---

## Checkout

- Enter Customer Information
- Verify Checkout Overview
- Complete Purchase

---

## Order Completion

- Verify Successful Order Placement

---

## Logout

- Verify Successful Logout

---

# Reporting

## HTML Reports

Generate an HTML report using:

```bash
pytest --html=report.html --self-contained-html
```

Reports include:

- Passed Tests
- Failed Tests
- Execution Time
- Test Duration

---

## Automatic Screenshots

Whenever a test fails, a screenshot is automatically captured inside:

```text
screenshots/
```

This helps simplify debugging and failure analysis.

---

# Data-Driven Testing

Login credentials are stored in a JSON file.

Example:

```json
[
  {
    "username": "standard_user",
    "password": "secret_sauce"
  },
  {
    "username": "problem_user",
    "password": "secret_sauce"
  }
]
```

The framework reads the JSON data and executes the same test for every dataset.

---

# Cross-Browser Testing

The framework currently supports:

- Google Chrome
- Mozilla Firefox

Run Chrome tests:

```bash
pytest --browser chrome
```

Run Firefox tests:

```bash
pytest --browser firefox
```

---

# Continuous Integration

## GitHub Actions

GitHub Actions automatically performs the following on every push and pull request:

- Checkout source code
- Install Python dependencies
- Launch headless Chrome
- Execute the complete Pytest suite
- Generate HTML reports
- Upload reports as workflow artifacts

This ensures the framework is continuously validated after every code change.

---

## Jenkins Pipeline

A Jenkins Declarative Pipeline has been implemented to automate framework execution.

The Jenkins pipeline performs the following steps:

- Checkout source code from GitHub
- Verify the execution environment
- Create a Python virtual environment
- Install project dependencies
- Execute Selenium tests
- Generate browser-specific HTML reports
- Archive reports as Jenkins build artifacts

Current Jenkins execution supports:

- Chrome
- Firefox

Microsoft Edge support is planned as the next enhancement.

---

# Docker Support

The framework includes a Dockerfile that creates a reusable automation environment.

The Docker image installs:

- Python
- Google Chrome
- Mozilla Firefox
- ChromeDriver
- GeckoDriver
- Project dependencies

This ensures consistent execution across different systems without requiring manual setup.

---

# Design Pattern

This project follows the **Page Object Model (POM)**.

Each page object contains:

- Page Locators
- Page Actions
- Business Methods

Example:

```text
Login Page

├── Username Locator
├── Password Locator
├── Login Button
└── login() Method
```

Benefits:

- Better Readability
- Reusable Code
- Easy Maintenance
- Reduced Code Duplication

---

# How to Run

## Clone Repository

```bash
git clone <repository-url>
```

---

## Navigate to Project

```bash
cd SauceDemoFramework
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run All Tests

```bash
pytest
```

---

## Run Chrome Tests

```bash
pytest --browser chrome
```

---

## Run Firefox Tests

```bash
pytest --browser firefox
```

---

## Generate HTML Report

```bash
pytest --html=report.html --self-contained-html
```

---

# Current Progress

## Completed

- Project Setup
- Selenium Configuration
- Pytest Configuration
- Base Page
- Login Page
- Inventory Page
- Cart Page
- Checkout Page
- Checkout Overview Page
- Menu Page
- End-to-End Purchase Flow
- Logout Automation
- Explicit Waits
- Parameterized Tests
- JSON Data-Driven Testing
- Screenshot Capture on Test Failure
- HTML Reporting
- Cross-Browser Testing (Chrome & Firefox)
- Docker Configuration
- Jenkins CI Pipeline
- GitHub Actions CI Pipeline
- Git Integration
- GitHub Repository

---

# Planned Improvements

The following enhancements are planned:

- Microsoft Edge Execution
- Selenium Grid
- Parallel Test Execution (pytest-xdist)
- Allure Reporting
- Python Logging
- Environment Configuration

---

# Learning Objectives

This project demonstrates practical experience with:

- Selenium WebDriver
- Python Automation
- Pytest Framework
- Page Object Model (POM)
- Explicit Waits
- Data-Driven Testing
- Parameterized Testing
- Cross-Browser Automation
- HTML Reporting
- Screenshot Capture
- Docker Containerization
- Jenkins Pipelines
- GitHub Actions CI
- Automation Framework Design
- Git & GitHub
- Continuous Integration (CI)

---

# Future Vision

The goal of this project is to continue evolving into a production-ready Selenium Automation Framework by incorporating advanced automation practices such as Microsoft Edge execution, Selenium Grid, parallel execution, advanced reporting, logging, and scalable cross-browser execution.

---

# Author

**Farooq**

Aspiring QA Automation Engineer passionate about building production-ready UI Automation Frameworks using Python, Selenium WebDriver, Pytest, Docker, Jenkins, and GitHub Actions while following industry-standard automation best practices.

---

# License

This project is intended for learning, demonstration, and portfolio purposes.