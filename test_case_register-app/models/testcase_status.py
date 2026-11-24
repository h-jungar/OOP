from enum import Enum

class TestCaseStatus(Enum):
    __test__ = False

    NOT_RUN = "Not run"
    PASSED = "Passed"
    FAILED = "Failed"
    BLOCKED = "Blocked"