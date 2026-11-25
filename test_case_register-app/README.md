# Test Case Register

## Project Description
Test Case Register is a console-based application developed in Python. The purpose of the application is to register and manage test cases.

Each test case contains a title, a description and an expected result. The application allows users to add new test cases, view registered test cases, and update the status of existing test cases.

Test cases are stored in memory while the application is running and are not persisted between sessions.


## Project Structure
The application is organized into separate modules and packages, each with its own responsibility.

```text
test_case_register-app/
│
├── dialogs/
│   └── testcase_dialog.py
│
├── models/
│   ├── testcase.py
│   ├── testcase_status.py
│   └── testcase_result.py
│
├── services/
│   └── testcase_service.py
│
├── tests/
│   └── test_testcase_service.py
│
├── utils/
│   └── console_helper.py
│
├── main.py
├── tc_activity_diagram.puml
├── tc_class_diagram.puml
├── tc_sequence_diagram.puml
└── README.md
```

### Main components
- `main.py`: Entry point of the application. Starts the program and manages the main application flow.
- `dialogs`: Handles communication with the user through the console.
- `models`: Contains the classes that represent test cases, their statuses and operation results.
- `services`: Contains the application logic, including validation, registration, duplicate checking and updating test cases.
- `tests`: Contains unit tests for the application logic.
- `utils`: Contains reusable helper functions for console interaction.


## Installation

### Prerequisites
- Python 3.10 or later
- Git

### Setup

1. Clone the repository:
```bash
git clone https://github.com/h-jungar/OOP.git
```

2. Navigate to the project directory:
```bash
cd OOP/test_case_register-app
```

3. Create a virtual environment:
```bash
python3 -m venv .venv
```

4. Activate the virtual environment:
```bash
source .venv/bin/activate
```

5. Install pytest to run the unit tests:
```bash
python3 -m pip install pytest
```


## Usage

### Run the application
Start the application from the project root directory:
```bash
python3 main.py
```
Follow the instructions in the console menu to register, view and manage test cases.

### Run the unit tests
To run the unit tests, execute:
```bash
python3 -m pytest -v
```

The tests verify the application's core functionality, including test case registration, input validation, ID generation, duplicate detection, retrieving test cases and updating test case statuses.


## Design Reflection

### UML and Implementation
The implementation follows the design and structure established during the planning phase. The class diagram, activity diagram and sequence diagram were used as a foundation for the application. Some minor adjustments were made during implementation, including changes to class, file and method names. For example, the module name was changed from test_case.py to testcase.py to avoid unintended test discovery by pytest. The UML diagrams were also updated to reflect the final implementation. However, the overall functionality and application flow remain as originally planned.

One important design decision was to separate input validation, duplicate checking and test case creation into distinct steps. The `validate_test_case()` method is used to validate the user's input before the registration process continues. The input validation takes place in a loop that allows the user to correct invalid information or cancel the registration.

Once the input is valid, the validation loop ends. The application then uses `find_test_cases_by_title()` to check whether test cases with the same title already exist. If matches are found, they are presented to the user, who can choose whether to continue with the registration or cancel it. This helps prevent unnecessary duplicates while still allowing test cases with the same title when they describe different scenarios.

The `TestCase` object is not created until the user has decided to proceed with the registration. This avoids creating unnecessary objects when a registration is cancelled because of duplicate test cases. Only when the registration is approved does the application call `add_test_case()`, which generates a unique ID by calling the service's internal `_generate_test_case_id()` method before creating and registering the test case.

The `add_test_case()` method also performs its own validation before creating and registering a test case. This ensures that the service does not rely on another part of the application having already validated the input. It also makes the method more robust and reusable if the application is extended in the future, for example, with a graphical user interface that calls the method directly instead of using the current terminal interface.

### Readability and Maintainability
The application is divided into separate modules and classes with clearly defined responsibilities. `TestCaseDialog` handles user interaction, while `TestCaseService` is responsible for the application logic, such as validation, duplicate checks, ID generation and registration.

`TestCase` represents an individual test case, while `TestCaseResult` provides feedback on whether an operation was successful.

This separation of responsibilities makes the code easier to understand and maintain. Changes to the user interaction can be made without directly affecting the application logic, and new functionality can be added without having to modify unrelated parts of the application.

Each registered test case is assigned a unique ID by `TestCaseService`, using the format TC-001, TC-002 and so on. The ID is generated only when a test case is ready to be registered, ensuring that cancelled registrations do not use up IDs.

### Testability
Separating the application logic from user interaction makes the application easier to test. Since the main functionality is handled by `TestCaseService`, its methods can be tested independently without having to interact with the console or simulate user input.

Unit tests have been created using pytest to verify the application's central functionality, including test case registration, input validation, ID generation, duplicate detection, retrieving test cases and updating test case statuses.

By keeping the business logic separate from the console interaction, the application becomes easier to test, debug and further develop.