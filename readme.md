# Integration Test Suite for Smart Light Bulbs Web App
## Overview
This integration test suite is designed to ensure the reliability and correctness of the web application that manages smart light bulbs in a home network. The application offers various functionalities such as listing devices, connecting to devices, changing device properties, and performing automation tasks.

### Directory Structure
The test suite is organized into the following directories and files:
```
tests/
│
├── __init__.py
├── conftest.py
├── settings.py
├── api_client/
│   ├── __init__.py
│   └── device_api_client.py
├── device_settings/
│   └── settings.py
├── models/
│   └── response_models.py
├── integration_tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_automation_task.py
│   ├── test_connect_device.py
│   ├── test_device_state.py
│   ├── test_disconnect.py
│   ├── test_list_devices.py
│   └── test_set_device_properties.py
├── random_data/
│   └── random_data.py
├── test_helpers/
│   └── test_helpers.py
├── utils/
│    ├── __init__.py
│    └── utils.py
├── logs/
└── reports/  
```

## Test Implementation
### Fixtures and Configuration
- conftest.py: Contains common fixtures and logging configurations used across the test suite. This file sets up fixtures for capturing logs, writing test logs to specific directories for better traceability. It also helps in naming proper report files with date time for pytest-html.
- integration_tests/conftest.py: Contains common fixtures used across the test suite. This file sets up fixtures to provide reusable components for testing, including:

    - Client Fixture: Initializes the DeviceAPIClient for interacting with the device API, ensuring a clean state by disconnecting the device after each test function.
    - Random Data Fixture: Provides an instance of RandomDataGenerator to generate random data for tests, facilitating diverse test scenarios.

### API Client
- api_client/device_api_client.py: Implements the API client for interacting with the application's endpoints. This client is used to abstract the details of making HTTP requests.
### Integration Tests
The integration tests are located in the integration_tests directory and cover the main functionalities of the application:

- test_automation_task.py: Tests the automation task that adjusts the brightness of a connected device.
- test_connect_device.py: Tests the ability to connect to a device in the network.
- test_device_state.py: Tests retrieving the state of a connected device.
- test_disconnect.py: Tests disconnecting from a device.
- test_list_devices.py: Tests listing all available devices in the network.
- test_set_device_properties.py: Tests setting the properties (name, brightness, color) of a connected device.
### Utilities and Helpers
- random_data/random_data.py: Generates random data for use in tests to ensure variability and robustness.
- test_helpers/test_helpers.py: Contains helper functions to assist with common test operations.
- utils/utils.py: Provides additional utility functions that support the tests.
- models/response_models.py: Provides the functionality of checking response object types
### Reports and Logs
- reports: Test result report generated with Pytest-html. 
- logs: API requests and response logs arranged according to the tests hierarchy

### Benefits of the Test Suite
- Modularity: 
The test suite is modular, with each test file focusing on specific functionalities, making it easier to maintain and extend.
- Reusability: Fixtures and helper functions are designed for reusability across different tests, reducing code duplication.
- Isolation: Tests are isolated from each other, ensuring that they do not interfere with one another and providing reliable test results.
- Logging and Debugging: All APIs requests and responses are logged for better debuggin purpose

- Dockerization: Two docker containers are used for test execution. One to have light bulb web server and another to execute the tests. 

- Reporting: Reporting with pytest-html generates comprehensive HTML reports with detailed test information, provides a user-friendly visual representation of test results, allows inclusion of additional information in the report, links test cases with specific issues or requirements, and enables storage and analysis of historical test results.

- Marker: One test marker SMOKE is introduced for running the smoke tests.

## Points for discussion:

- POST /name API: Name param should accept only fixed length strings. Currently it accepts string, numbers, etc. Tests have been implemented for these checks and they are failing.

- POST /color API: Color param should accept 6 hex digits. Currently it accepts invalid hex digits also. Tests have been implemented for these checks and they are failing.

- POST /chilltime API: Chilltime API should mentions how the brightness will decrease untill it reaches the 30% in the specs.

### Bugs and Testcases
- 5 Bugs are reported in bugs.md file
- Testcases are in testcases.md file

## Running the Tests
To run the test suite, use the following command:

```
docker compose build
docker compose up
```

Currently only the 16 smoke tests will run. To run all the 70 tests remove `-m smoke` from the docker compose file and run the above commands. To see the reports go to `/tests/reports/` directory.

## Additional Testing Techniques
- Load Testing: Ensure the application can handle a large number of requests and connected devices simultaneously.
- Security Testing: Verify that the application is secure against common vulnerabilities such as SQL injection, XSS, etc. Also list of naughty strings can be used to check the edge cases.
- End-to-End Testing: Simulate real user interactions with the application to ensure the entire workflow functions correctly.
