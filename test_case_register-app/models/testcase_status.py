from enum import Enum

class TestCaseStatus(Enum):
    NOT_RUN = "Not run"
    PASSED = "Passed"
    FAILED = "Failed"
    BLOCKED = "Blocked"