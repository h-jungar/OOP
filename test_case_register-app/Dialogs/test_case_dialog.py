"""
Ansvarar för användarinteraktionen via terminalen.

Attribut:
Attribut	Datatyp	Beskrivning
test_case_service	TestCaseService	Referens till servicens instans

Metoder:
Metod	Parametrar	Returtyp	Ansvar
add_test_case()	Inga	None	Samlar in information och hanterar registrering
list_test_cases()	Inga	None	Visar samtliga registrerade testfall
show_menu()	Inga	None	Visar menyn och hanterar användarens val

Dialogen ska även hantera frågan om användaren vill fortsätta registreringen när en möjlig dubblett hittas.

Vi behöver också lägga till en metod för att ändra status:
Metod	Parametrar	Returtyp	Ansvar
update_test_case_status()	Inga	None	Låter användaren välja testfall och ny status
"""

