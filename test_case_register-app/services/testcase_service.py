from models.testcase import TestCase
from models.testcase_result import TestCaseResult
from models.testcase_status import TestCaseStatus

class TestCaseService:
    def __init__(self):
        self._test_cases: list[TestCase] = []


    def validate_test_case(self, title: str, description: str, expected_result: str) -> TestCaseResult:
        validation_errors = []

        if not title.strip():
            validation_errors.append("Test case title is required.")
        if not description.strip():
            validation_errors.append("Test case description is required.")
        if not expected_result.strip():
            validation_errors.append("Test case expected result is required.")

        if validation_errors:
            error_message = "\n".join(validation_errors)
            return TestCaseResult(False, "\n" + error_message + "\n", None)
        return TestCaseResult(True, "Test case validated", None)


    def add_test_case(self, title: str, description: str, expected_result: str) -> TestCaseResult:
        validation_result = self.validate_test_case(title, description, expected_result)

        if not validation_result.succeeded:
            return validation_result

        test_case_id = self._generate_test_case_id()

        test_case = TestCase(test_case_id, title, description, expected_result)

        self._test_cases.append(test_case)
        return TestCaseResult(True, f"Test case with title {test_case.title} added successfully.", test_case)


    def _generate_test_case_id(self) -> str:
        sequential_number = len(self._test_cases) + 1
        test_case_id = f"TC-{sequential_number:03d}"
        return test_case_id


    def get_test_cases(self) -> list[TestCase]:
        return self._test_cases.copy()


    def find_test_cases_by_title(self, title: str) -> list[TestCase]:
        duplicate_title_list = [x for x in self._test_cases if title.strip().lower() == x.title.strip().lower()]
        return duplicate_title_list


    def update_test_case_status(self, test_case_id: str, new_status: TestCaseStatus) -> TestCaseResult:
        for test_case in self._test_cases:
            if test_case.id == test_case_id:
                test_case.status = new_status
                return TestCaseResult(True, f"Test case with ID {test_case.id} updated status to {test_case.status.value}.", test_case)
        else:
            return TestCaseResult(False, f"Test case with ID {test_case_id} does not exist.", None)