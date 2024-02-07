# ToDo App API Test Suite
[![Run tests and publish the report](https://github.com/software-ace/todo-API-test-framework/actions/workflows/python-app.yml/badge.svg)](https://github.com/software-ace/todo-API-test-framework/actions/workflows/python-app.yml)
[![Python Version](https://img.shields.io/badge/Python-3.12-blue)](https://www.python.org/downloads/release/python-312/)
[![Pytest Version](https://img.shields.io/badge/pytest-8.0.0-blue)](https://docs.pytest.org/en/stable/)
[![Requests Version](https://img.shields.io/badge/requests-2.31.0-blue)](https://docs.python-requests.org/en/latest/)
[![Faker Version](https://img.shields.io/badge/faker-22.6.0-blue)](https://faker.readthedocs.io/en/master/)

This repository contains a Python test suite for a ToDo app API [here is the API documentation](https://todo.pixegami.io/docs).
The tests are written using pytest and utilize 
the requests library for API interactions and faker for generating fake data.

## Setup

Before running the tests, ensure you have Python installed on your machine. You can set up a virtual environment and install the required dependencies using the following commands:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use "venv\Scripts\activate"
pip install --upgrade pip
pip install pytest==8.0.0 pytest-html==4.1.1 faker==22.6.0 requests==2.31.0
```
## Running Tests

To run the tests, execute the following command:

```bash
pytest --html=testing_results/report.html
```
This will run the tests and generate an HTML report in the `testing_results` directory.

## Test Dependencies

   - pytest: A testing framework for Python.
   - pytest-html: A plugin for pytest that produces an HTML report for test results.
   - requests: A Python library for making HTTP requests.
   - faker: A Python library for generating fake data.

## Test Report

After running the tests, you can view the detailed test report by opening the generated HTML file in a web browser. 
The report is located at `testing_results/report.html`.

## View Latest Deployment

[![View Latest Deployment](https://img.shields.io/badge/View-Latest%20Deployment-blue)](http://softwareace.xyz/todo-API-test-framework/)
