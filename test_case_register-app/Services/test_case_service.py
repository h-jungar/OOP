"""
Ansvarar för programmets logik och hantering av testfall.

Attribut:
Attribut	Datatyp	Beskrivning
test_cases	list[TestCase]	Lista över registrerade testfall

Metoder:
Metod	Parametrar	Returtyp	Ansvar
add_test_case()	test_case: TestCase	TestCaseResult	Kontrollerar och registrerar testfall
get_test_cases()	Inga	list[TestCase]	Hämtar samtliga testfall
find_test_cases_by_title()	title: str	list[TestCase]	Hittar testfall med samma titel, skiftlägesokänsligt
generate_test_case_id()	Inga	str	Genererar nästa ID, exempelvis TC-001

Viktigt: add_test_case() ska använda find_test_cases_by_title() för att hitta möjliga dubbletter. Om en matchning hittas ska dialogen kunna visa det befintliga testfallet och fråga användaren om det nya ändå ska registreras.

Vi har också bestämt att ID ska genereras först när användaren faktiskt väljer att registrera testfallet.
"""

