# SauceDemo Python Selenium Automation Framework

A UI Test Automation Framework built using **Python**, **Selenium WebDriver**, and **Pytest**, following the **Page Object Model (POM)** design pattern.

This project automates the complete purchase flow of the SauceDemo web application while demonstrating industry-standard automation framework practices.

---

# Tech Stack

- Python 3.11+
- Selenium WebDriver
- Pytest
- WebDriver Manager
- Page Object Model (POM)
- Git & GitHub

---

# Project Structure

```
SauceDemoFramework/
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
│
├── utilities/
├── config/
├── reports/
├── screenshots/
├── logs/
├── test_data/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

# Framework Features

- Page Object Model (POM)
- Pytest Test Runner
- Reusable Base Page
- Shared WebDriver Fixture
- Cross-platform execution
- Clean project structure
- Git version control

---

# Automated Test Scenarios

## Login

- Successful Login

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

- Logout Automation *(Currently Under Development)*

---

# How to Run

## Clone Repository

```bash
git clone <repository-url>
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Environment

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

## Run Single Test

```bash
python -m pytest -v tests/test_login.py
```

---

# Design Pattern

This project follows the **Page Object Model (POM)**.

Each application page has its own Python class containing:

- Locators
- Actions
- Business methods

Benefits:

- Reusable code
- Easy maintenance
- Better readability
- Reduced duplication

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
- End-to-End Purchase Flow
- Git Integration

---

# Planned Features

The following features will be added as the framework grows:

- Logout Automation
- Negative Login Tests
- Parameterized Tests
- Explicit Waits
- Improved BasePage Utilities
- JSON Test Data
- Logging
- Screenshot on Test Failure
- HTML Reports
- Headless Browser Execution
- Cross-Browser Testing (Chrome & Edge)
- GitHub Actions CI/CD
- Parallel Test Execution
- Allure Reports
- Environment Configuration
- Jenkins Integration
- Docker Support
- Selenium Grid

---

# Learning Objectives

This project is designed to practice:

- Selenium WebDriver
- Python Automation
- Pytest
- Page Object Model
- Framework Design
- Test Automation Best Practices
- Git & GitHub
- Continuous Integration

---

# Author

**Farooq**

Learning Test Automation using Python, Selenium, and Pytest while building a real-world automation framework.