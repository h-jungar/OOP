"""
Representerar vilka statusar ett testfall kan ha.
Vi diskuterade att använda en Python Enum.

Värden:
Värde	Betydelse
NOT_RUN	Testfallet har inte genomförts
PASSED	Testet godkändes
FAILED	Testet underkändes
BLOCKED	Testet kunde inte genomföras

Detta är egentligen inte en vanlig klass med attribut och metoder, utan en uppräkningstyp (Enum).
"""

from enum import Enum

class TestStatus(Enum):
    NOT_RUN = "Not run"
    PASSED = "Passed"
    FAILED = "Failed"
    BLOCKED = "Blocked"