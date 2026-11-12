"""
Ansvarar för programmets logik och hantering av testfall.

Attribut	Datatyp	        Beskrivning
test_cases	list[TestCase]	Lista över registrerade testfall

Metod	                    Parametrar	            Returtyp	    Ansvar
add_test_case()	            test_case: TestCase	    TestCaseResult	Kontrollerar och registrerar testfall
get_test_cases()	        Inga	                list[TestCase]	Hämtar samtliga testfall
find_test_cases_by_title()	title: str	            list[TestCase]	Hittar testfall med samma titel, skiftlägesokänsligt
generate_test_case_id()	    Inga	                str	            Genererar nästa ID, exempelvis TC-001

Viktigt: add_test_case() ska använda find_test_cases_by_title() för att hitta möjliga dubbletter. Om en matchning hittas ska dialogen kunna visa det befintliga testfallet och fråga användaren om det nya ändå ska registreras.
ID ska genereras först när användaren faktiskt väljer att registrera testfallet.
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
            return TestCaseResult(False, "Test case excpected result is required.", None)
        return TestCaseResult(True, "Test case validated", None)


    def add_test_case(self, title: str, description: str, expected_result: str) -> TestCaseResult:
        validation_result = self.validate_test_case(title, description, expected_result)

        if not validation_result.succeeded:
            return validation_result

        "call generate_test_case_id() and create test_case : TestCase"
        id = self.generate_test_case_id()

        test_case = TestCase(id, title, description, expected_result)

        self._test_cases.append(test_case)
        return TestCaseResult(True, f"Test case with title {test_case.title} added successfully.", test_case)


    def generate_test_case_id(self) -> str:
        "generate ID:s in format TC001, TC002 etc"
        sequential_number = len(self._test_cases) + 1
        test_case_id = f"TC-{sequential_number:03d}"
        return test_case_id


    def get_test_cases(self) -> list[TestCase]:
        return self._test_cases.copy()


    def find_test_cases_by_title(self, title: str) -> list[TestCase]:
        "Find test cases by title to look for duplicates"