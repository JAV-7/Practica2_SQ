# machine_operations.py

"""Base file for machine operations."""

# ATM password
import sys

PASSWORD = "1234"


# Set amount with input validation, for any resource
def set_amount(prompt: str) -> int:
    """
    Read a non-negative integer amount from user input.

    Parameters
    ----------
    prompt : str
        The prompt message to display to the user.

    Returns
    -------
    int
        The validated non-negative integer provided by the user.

    Notes
    -----
    The function keeps prompting until a valid non-negative integer is entered.
    """
    while True:
        try:
            amount = int(input(prompt))
            if amount < 0:
                print("Please enter a non-negative integer.")
                continue
            return amount
        except ValueError:
            print("Invalid input. Please enter a non-negative integer.")
            continue


def withdraw_money(password: str, machine_state: dict) -> None:
    """
    Withdraw money from the machine if the password is correct.

    Parameters
    ----------
    password : str
        The password to authorize withdrawal.
    machine_state : dict
        The current state of the machine, including its money.

    Returns
    -------
    None

    Notes
    -----
    Offers an option to send the withdrawn money to charity.
    """
    if password != PASSWORD:
        print("Incorrect password. Access denied.")
        return
    amount = set_amount("Insert desired quantity of money to withdraw : ")
    if amount > machine_state["money"]:
        print("Cannot withdraw more than available"
              "(${machine_state['money']}). Withdrawing all available money.")
        amount = machine_state["money"]

    while True:
        purpose = input("Do you want to send charity? (yes/no): ")
        purpose = purpose.strip().lower()
        if purpose == "yes":
            print(f"Sending ${amount} to charity. Thank you!")
            machine_state["money"] -= amount
            break
        elif purpose == "no":
            print(f"Withdrawing ${amount}.")
            machine_state["money"] -= amount
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


def deposit_money(password: str, machine_state: dict) -> None:
    """
    Allow users to deposit money into the machine.

    Parameters
    ----------
    password : str
        The password to authorize the deposit.
    machine_state : dict
        The current state of the machine, including its money.

    Returns
    -------
    None
    """
    if password != PASSWORD:
        print("Incorrect password. Access denied.")
        return
    amount = set_amount("Insert amount of money to deposit: $")
    machine_state["money"] += amount
    print(f"Deposited ${amount}. Total money in machine: "
          f"${machine_state['money']}")


def exit_program() -> None:
    """Exit the program gracefully."""
    print("Exiting the program. Goodbye!")
    sys.exit()
