from services.test_case_service import TestCaseService
from dialogs.test_case_dialog import TestCaseDialog
from utils.console_helper import clear_screen, pause

def main() -> None:
    test_case_service = TestCaseService()
    test_case_dialog = TestCaseDialog(test_case_service)

    while True:
        clear_screen()

        print("\n###  MAIN MENU   ###")
        print("1. Test case register")
        print("0. Exit")

        option = input("Choose an option: ").strip()

        match option:
            case "1":
                test_case_dialog.show_menu()
            case "0":
                return
            case _:
                print("Invalid option, try again!")
                pause()

if __name__ == "__main__":
    main()