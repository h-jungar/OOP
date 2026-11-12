"""
Representerar resultatet av en operation, exempelvis när ett testfall registreras.

Attribut:
Attribut	Datatyp	Beskrivning
succeeded	bool	Om operationen lyckades
message	str	Meddelande om resultatet
test_case	TestCase \| None	Testfallet som berörs, om tillämpligt

Metoder:

- Konstruktor (__init__).
"""
from models.test_case import TestCase

class TestCaseResult:
    def __init__(self, succeeded : bool, message : str, test_case : TestCase | None):
        self.succeeded = succeeded
        self.message = message
        self.test_case = test_case