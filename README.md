# SauceDemo QA Assignment

This repository contains a few basic Selenium test cases created for the SauceDemo website.

## What is covered

The automation currently verifies:

1. Successful login using valid credentials
2. Add a product to the cart and complete checkout
3. Verify the error message for a locked-out user

## Tools Used

* Python
* Selenium WebDriver
* PyTest
* WebDriver Manager

## Setup

Install the required packages:

pip install -r requirements.txt

## Running the Tests

Run all tests:

pytest -v

## Notes

I kept the framework intentionally simple and focused on the core user flows requested in the assignment.

The goal was to automate the most important customer journeys rather than build a large testing framework.

Website tested:
https://www.saucedemo.com
