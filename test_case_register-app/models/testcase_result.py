from models.testcase import TestCase

class TestCaseResult:
    def __init__(self, succeeded : bool, message : str, test_case : TestCase | None):
        self.succeeded = succeeded
        self.message = message
        self.test_case = test_case