from models.test_status import TestStatus

class TestCase:
    def __init__(self, id: str, title: str, description: str, expected_result: str):
        self.id = id
        self.title = title
        self.description = description
        self.expected_result = expected_result
        self.status = TestStatus.NOT_RUN
