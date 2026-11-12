"""
Representerar ett enskilt testfall.

Attribut:
Attribut	Datatyp	Beskrivning
id	str	Unikt ID, exempelvis TC-001
title	str	Testfallets titel
description	str	Beskrivning av vad som ska testas
expected_result	str	Förväntat resultat
status	TestStatus	Testfallets aktuella status

"""
from models.test_status import TestStatus

class TestCase:
    def __init__(self, id: str, title: str, description: str, expected_result: str):
        self.id = id
        self.title = title
        self.description = description
        self.expected_result = expected_result
        self.status = TestStatus.NOT_RUN
