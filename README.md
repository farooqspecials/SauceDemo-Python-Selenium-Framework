# SauceDemo Python Selenium Automation Framework

A UI Test Automation Framework built using **Python**, **Selenium WebDriver**, and **Pytest**, following the **Page Object Model (POM)** design pattern.

This project automates key user workflows of the SauceDemo web application while demonstrating industry-standard automation framework design and best practices.

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
- Git & GitHub

---

# Project Structure

```
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
│   ├── test_login.py
│   ├── test_login_parameterized.py
│   ├── test_cart.py
│   ├── test_remove_cart.py
│   ├── test_checkout.py
│   ├── test_logout.py
│
├── utils/
│   └── json_reader.py
│
├── screenshots/
│
├── reports/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── report.html
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
- Automatic Screenshot Capture on Test Failure
- HTML Test Reports
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

Generate a professional HTML report using:

```bash
python -m pytest -v --html=report.html --self-contained-html
```

Open the generated report:

```
report.html
```

The report includes:

- Test Results
- Passed Tests
- Failed Tests
- Execution Time
- Test Duration

---

## Automatic Screenshots

Whenever a test fails, a screenshot is automatically captured and stored in:

```
screenshots/
```

This makes debugging much easier.

---

# Data-Driven Testing

Login credentials are stored inside a JSON file.

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

Pytest reads the JSON file and executes the same test for every data set.

---

# Design Pattern

This framework follows the **Page Object Model (POM)**.

Each page contains:

- Page Locators
- Page Actions
- Business Methods

Example:

```
Login Page
│
├── Username Locator
├── Password Locator
├── Login Button
└── login() Method
```

Benefits:

- Better Readability
- Code Reusability
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
python -m pytest -v
```

---

## Run a Single Test

```bash
python -m pytest -v tests/test_login.py
```

---

## Run Parameterized Tests

```bash
python -m pytest -v tests/test_login_parameterized.py
```

---

## Generate HTML Report

```bash
python -m pytest -v --html=report.html --self-contained-html
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
- Screenshot on Test Failure
- HTML Reports
- Git Integration
- GitHub Repository

---

# Planned Improvements

The following features are planned for future implementation:

- Python Logging
- Headless Browser Execution
- Cross-Browser Testing (Chrome & Edge)
- Environment Configuration
- Parallel Test Execution (pytest-xdist)
- GitHub Actions CI/CD
- Allure Reporting
- Jenkins Integration
- Docker Support
- Selenium Grid

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
- HTML Reporting
- Screenshot Capture
- Automation Framework Design
- Test Automation Best Practices
- Git & GitHub
- Continuous Integration Concepts

---

# Future Vision

The goal of this project is to evolve into a production-style Selenium Automation Framework by incorporating advanced automation practices such as CI/CD pipelines, parallel execution, cross-browser testing, Docker containers, Selenium Grid, and comprehensive reporting.

---

# Author

**Farooq**

Aspiring QA Automation Engineer building a real-world Selenium Automation Framework using Python, Selenium WebDriver, and Pytest while following industry-standard automation practices.

---

# License

This project is intended for learning and portfolio purposes.