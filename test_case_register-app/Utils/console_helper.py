import os
import subprocess

def clear_screen():
    if os.name == "nt":
        subprocess.run(["cmd", "/c", "cls"], check=False)
    else:
        subprocess.run(["clear"], check=False)

def pause():
    input("\nPress enter to continue...")

def required_input(prompt: str) -> str:
    while True:
        value = input(f"{prompt}: ").strip()

        if value:
            return value
        print("This field is required, try again.\n")