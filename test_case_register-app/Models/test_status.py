from enum import Enum

class TestStatus(Enum):
    NOT_RUN = "Not run"
    PASSED = "Passed"
    FAILED = "Failed"
    BLOCKED = "Blocked"