# main.py

"""
Entry point for coffee machine practice.

Execute this file to test the entire project.
"""

from machine_operations import deposit_money, exit_program, withdraw_money
from menu_utils import press_enter_to_continue, read_option
from test_runner import run_random_tests_from_main

from coffee_machine import (
    create_coffee_machine,
    fill_the_machine,
    make_coffee,
    show_data,
)


def main() -> None:
    """Docstring for main."""
    print("=== Welcome to the Coffee Machine ===")
    machine = create_coffee_machine()

    while True:
        print("\n--- Main Menu ---")
        print("1. View machine status")
        print("2. Fill machine")
        print("3. Buy coffee")
        print("4. Deposit money (Admin)")
        print("5. Withdraw money (Admin)")
        print("6. Exit")
        print("7. Run random tests")

        # Lectura validada de opciones (1-7)
        choice = read_option("\nSelect an option (1-7): ",
                             valid=["1", "2", "3", "4", "5", "6", "7"])

        if choice == '1':
            show_data(machine)

        elif choice == '2':
            fill_the_machine(machine)

        elif choice == '3':
            make_coffee(machine)

        elif choice == '4':
            password = input("Enter admin password: ")
            deposit_money(password, machine)

        elif choice == '5':
            password = input("Enter admin password: ")
            withdraw_money(password, machine)

        elif choice == '6':
            exit_program()

        elif choice == '7':
            run_random_tests_from_main()
            press_enter_to_continue()


if __name__ == "__main__":
    main()
