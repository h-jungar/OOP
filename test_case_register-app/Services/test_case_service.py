"""
Ansvarar för programmets logik och hantering av testfall.

Attribut	Datatyp	        Beskrivning
test_cases	list[TestCase]	Lista över registrerade testfall

Metod	                    Parametrar	            Returtyp	    Ansvar
add_test_case()	            self, title,
                            description,
                            expected_result	        TestCaseResult	Kontrollerar och registrerar testfall
get_test_cases()	        Inga	                list[TestCase]	Hämtar samtliga testfall
find_test_cases_by_title()	title: str	            list[TestCase]	Hittar testfall med samma titel, skiftlägesokänsligt
generate_test_case_id()	    Inga	                str	            Genererar nästa ID, exempelvis TC-001
"""

from models.test_case import TestCase
from models.test_case_result import TestCaseResult
from models.test_status import TestStatus

class TestCaseService:
    def __init__(self):
        self._test_cases: list[TestCase] = []


    def validate_test_case(self, title: str, description: str, expected_result: str) -> TestCaseResult:
        if not title.strip():
            return TestCaseResult(False, "Test case title is required", None)
        if not description.strip():
            return TestCaseResult(False, "Test case description is required.", None)
        if not expected_result.strip():
            return TestCaseResult(False, "Test case expected result is required.", None)
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


    def update_test_case_status(self, test_case_id: str, new_status: TestStatus) -> TestCaseResult:
        for test_case in self._test_cases:
            if test_case.id == test_case_id:
                test_case.status = new_status
                return TestCaseResult(True, f"Test case with ID {test_case.id} updated status to {test_case.status.value}.", test_case)
        else:
            return TestCaseResult(False, f"Test case with ID {test_case_id} does not exist.", None)