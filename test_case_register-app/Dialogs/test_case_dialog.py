"""
Ansvarar för användarinteraktionen via terminalen.

Attribut	        Datatyp	            Beskrivning
test_case_service	TestCaseService	    Referens till servicens instans

Metod	          Parametrar	Returtyp	Ansvar
add_test_case()	  Inga	        None	    Samlar in information och hanterar registrering
list_test_cases() Inga	        None	    Visar samtliga registrerade testfall
show_menu()	      Inga          None	    Visar menyn och hanterar användarens val

Dialogen ska även hantera frågan om användaren vill fortsätta registreringen när en möjlig dubblett hittas.

Vi behöver också lägga till en metod för att ändra status:
Metod	                    Parametrar	Returtyp	Ansvar
update_test_case_status()	Inga	    None	    Låter användaren välja testfall och ny status
"""

from utils.console_helper import clear_screen, pause, required_input
from services.test_case_service import TestCaseService

class TestCaseDialog:
    def __init__(self, test_case_service: TestCaseService):
        self._test_case_service: TestCaseService = test_case_service

    def show_menu(self):
        while True:
            clear_screen()

            print("\n###  TEST CASE REGISTER  ###")
            print("1. Add a new test case")
            print("2. Show list of test cases")
            print("3. Update test case status")
            print("0. Exit")

            option = input("Choose an option: ").strip()

            match option:
                case "1":
                    self.add_test_case()
                case "2":
                    self.list_test_cases()
                case "3":
                    self.update_test_case_status()
                case "0":
                    return
                case _:
                    print("Invalid option, try again!")
                    pause()

    def add_test_case(self):
        clear_screen()
        print("\n###  NEW TEST CASE - TEST CASE REGISTER  ###")
        print("To create a new test case enter following information\n")

        while True:
            title = required_input("Title")
            description = required_input("Description")
            expected_result = required_input("Expected result")

            validation_result = self._test_case_service.validate_test_case(title, description, expected_result)

            if validation_result.succeeded:
                break
            else:
                print(validation_result.message)
                print("1. Enter test case details again")
                print("0. Return to main menu")
                
                option = input("Choose an option: ").strip()
                
                match option:
                    case "1":
                        continue
                    case "0":
                        return
                    case _:
                        print("Invalid option, try again!")
                        pause()

        duplicate_test_cases = self._test_case_service.find_test_cases_by_title(title)

        if duplicate_test_cases:
            print("There is one or more existing test cases with the same title:")
            for test_case in duplicate_test_cases:
                print(f"Existing test case: {test_case.id} - {test_case.title}")
                print(f"Description: {test_case.description}")
            print("Do you still want to add the new test case or exit without adding? Choose below:")
            print("1. Continue and add new test case")
            print("0. Exit to main menu without adding test case")
                            
            while True:
                option = input("Choose an option: ").strip()

                match option:
                    case "1":
                        break
                    case "0":
                        return
                    case _:
                        print("Invalid option, try again!")
                        pause()
        
        result = self._test_case_service.add_test_case(title, description, expected_result)
        print(result.message)

        pause()