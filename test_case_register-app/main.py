"""Detta är programmets startpunkt.

Här har vi ingen klass planerad, utan en funktion:
Funktion	Ansvar
main()	Skapar instanser av service och dialog samt startar programmet

Den kopplar ihop klasserna genom dependency injection:
test_case_service = TestCaseService()
test_case_dialog = TestCaseDialog(test_case_service)
"""