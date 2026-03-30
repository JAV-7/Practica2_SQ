
# coffee_machine.py

"""
Coffee machine module.

Manage resources and coffee making.
"""

from machine_operations import set_amount

# Resource maximums
MAX_BEANS = 200
MAX_CUPS = 10
MAX_WATER = 2500
MAX_MILK = 1000

# Menu definitions
MENU = {
    "espresso": {"water": 250, "milk": 0, "beans": 16, "price": 4},
    "latte": {"water": 350, "milk": 75, "beans": 20, "price": 7},
    "cappuccino": {"water": 200, "milk": 100, "beans": 12, "price": 6}
}


def create_coffee_machine() -> dict:
    """
    Return a coffee machine with max resources and 100 money.

    Returns
    -------
    dict
        Dictionary with initial resources and starting money.
    """
    return {
    "beans": MAX_BEANS,
    "cups": MAX_CUPS,
    "water": MAX_WATER,
    "milk": MAX_MILK,
    "money": 100
    }


def show_data(machine: dict) -> None:
    """
    Display the current state of the coffee machine.

    Parameters
    ----------
    machine : dict
        The current state of the machine.
    """
    print(f"The coffee machine has:\n"
          f"\t* {machine['beans']} g of beans\n"
          f"\t* {machine['cups']} units of cups\n"
          f"\t* {machine['water']} ml of water\n"
          f"\t* {machine['milk']} ml of milk\n"
          f"\t* ${machine['money']} of money\n")


# Check if the machine is empty
def is_empty(machine: dict) -> bool:
    """
    Determine whether the machine has any resource at zero.

    Parameters
    ----------
    machine : dict
        The current state of the machine.

    Returns
    -------
    bool
        True if any resource is zero; otherwise, False.
    """
    if (machine['beans'] == 0 or machine['cups'] == 0 or machine['water'] == 0
        or machine['milk'] == 0):
        print("One, or more, ingredients are missing.")
        return True
    return False


# Check if the machine is full
def is_full(machine: dict) -> bool:
    """
    Determine whether the machine is at maximum capacity for all resources.

    Parameters
    ----------
    machine : dict
        The current state of the machine.

    Returns
    -------
    bool
        True if all resources are at maximum capacity; otherwise, False.
    """
    if (machine['beans'] == MAX_BEANS and machine['cups'] == MAX_CUPS and
        machine['water'] == MAX_WATER and machine['milk'] == MAX_MILK):
        print("The machine is already full.")
        return True
    return False


# Fill the machine with resources
def fill_the_machine(machine: dict) -> None:
    """
    Prompt the user to add resources to the machine, without exceeding limits.

    Parameters
    ----------
    machine : dict
        The current state of the machine.

    Returns
    -------
    None
    """
    if is_full(machine):
        return

    show_data(machine)

    # Helper function to check for overflow
    def check_overflow(current: int,
                       maximum: int,
                       resource_name: str,
                       unit: str = "") -> int:
        if current > maximum:
            print(f"The amount of {resource_name}{unit} cannot exceed"
                  f"{maximum}{unit}. Setting {resource_name}"
                   f" to {maximum}{unit}.")
            return maximum
        return current

    machine['beans'] += set_amount("Insert g of beans: ")
    machine['beans'] = check_overflow(machine['beans'], MAX_BEANS, "beans",
                                      "g")

    machine['water'] += set_amount("Insert ml of water: ")
    machine['water'] = check_overflow(machine['water'], MAX_WATER, "water",
                                      "ml")

    machine['milk'] += set_amount("Insert ml of milk: ")
    machine['milk'] = check_overflow(machine['milk'], MAX_MILK, "milk", "ml")

    machine['cups'] += set_amount("Insert number of cups: ")
    machine['cups'] = check_overflow(machine['cups'], MAX_CUPS, "cups")

    print("Machine filled successfully.")


# Display menu options
def show_menu() -> None:
    """
    Display the coffee menu with prices and ingredients.

    Returns
    -------
    None
    """
    print("\n--- Coffee Menu ---")
    for coffee, details in MENU.items():
        print(f"{coffee.capitalize()}: ${details['price']}"
              f"- Water: {details['water']}ml, Milk: {details['milk']}ml,"
              f"Beans: {details['beans']}g")


# Make coffee based on user choice
def make_coffee(machine: dict) -> None:
    """
    Make coffee based on the user's selection and process the payment.

    Parameters
    ----------
    machine : dict
        The current state of the machine.

    Returns
    -------
    None
    """
    if is_empty(machine):
        return

    show_menu()

    while True:
        choice = input("\nSelect your coffee (espresso/latte/cappuccino) or "
                       "'back' to return: ").strip().lower()

        if choice == 'back':
            return

        if choice not in MENU:
            print("Invalid choice. Please select from the menu.")
            continue

        coffee_recipe = MENU[choice]

        # Check if machine has enough resources
        if (machine['water'] < coffee_recipe['water'] or
            machine['milk'] < coffee_recipe['milk'] or
            machine['beans'] < coffee_recipe['beans'] or
            machine['cups'] < 1):
            print(f"Sorry, not enough resources to make {choice}.")
            return

        print(f"\n{choice.capitalize()} costs ${coffee_recipe['price']}")
        print(f"Available money in machine: ${machine['money']}")

        # Ask for payment
        payment = set_amount("Insert money: $")

        if payment < coffee_recipe['price']:
            print(f"Insufficient payment. {choice.capitalize()} costs"
                  f"${coffee_recipe['price']}. Money returned.")
            return

        # Calculate change
        change = payment - coffee_recipe['price']
        if change > 0:
            print(f"Here is your change: ${change}")

        # Deduct resources and add money
        machine['water'] -= coffee_recipe['water']
        machine['milk'] -= coffee_recipe['milk']
        machine['beans'] -= coffee_recipe['beans']
        machine['cups'] -= 1
        machine['money'] += coffee_recipe['price']

        print(f"Here is your {choice}! Enjoy!")
        return
