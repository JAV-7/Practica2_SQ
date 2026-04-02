# test_random_coffee_machine.py
"""
Randomized test suite for the coffee machine module.

This module runs several random scenarios to validate machine behavior:
viewing status, filling resources, purchases, payment handling, admin
operations, and resource limits.
"""

import random
import sys
from io import StringIO
from unittest.mock import patch

from machine_operations import PASSWORD, deposit_money, withdraw_money

from src import (
    MENU,
    create_coffee_machine,
    fill_the_machine,
    make_coffee,
    show_data,
)


def capture_output(func: callable, *args: tuple, **kwargs: dict) -> tuple:
    """Capture stdout output from a function call."""
    old_stdout = sys.stdout
    sys.stdout = captured_output = StringIO()
    try:
        result = func(*args, **kwargs)
        output = captured_output.getvalue()
        return result, output
    finally:
        sys.stdout = old_stdout


def random_test_case_1_view_status() -> dict:
    """Random Test Case1: View machine status with random initial resources."""
    print("=== RANDOM TEST CASE 1: View Machine Status ===")
    machine = create_coffee_machine()

    # Randomly modify initial resources for variety
    machine['beans'] = random.randint(0, 200)
    machine['water'] = random.randint(0, 2500)
    machine['milk'] = random.randint(0, 1000)
    machine['cups'] = random.randint(0, 10)
    machine['money'] = random.randint(0, 100)

    print("Random initial state generated:")
    _, output = capture_output(show_data, machine)
    print(output)
    return machine


def random_test_case_2_fill_machine() -> dict:
    """Random Test Case 2: Fill machine with random amounts."""
    print("=== RANDOM TEST CASE 2: Fill Machine with Random Amounts ===")
    machine = create_coffee_machine()

    # Start with random depleted resources
    machine['beans'] = random.randint(0, 100)
    machine['water'] = random.randint(0, 1500)
    machine['milk'] = random.randint(0, 500)
    machine['cups'] = random.randint(0, 5)

    print("Machine status before filling:")
    show_data(machine)

    # Generate random fill amounts
    beans_to_add = random.randint(10, 150)
    water_to_add = random.randint(100, 1000)
    milk_to_add = random.randint(50, 500)
    cups_to_add = random.randint(1, 8)

    print(f"Random inputs: {beans_to_add}g beans, {water_to_add}ml water,"
           "{milk_to_add}ml milk, {cups_to_add} cups")

    with patch('builtins.input',
               side_effect=[
                   str(beans_to_add),
                   str(water_to_add),
                   str(milk_to_add),
                   str(cups_to_add)
                   ]):
        _, output = capture_output(fill_the_machine, machine)

    print("Fill operation output:")
    print(output)
    print("Machine status after filling:")
    show_data(machine)
    return machine


def random_test_case_3_successful_purchase() -> dict:
    """Random Test Case 3: Random successful coffee purchase."""
    print("=== RANDOM TEST CASE 3: Random Successful Coffee Purchase ===")
    machine = create_coffee_machine()

    # Ensure machine has enough resources
    machine['beans'] = 200
    machine['water'] = 2500
    machine['milk'] = 1000
    machine['cups'] = 10

    # Random coffee selection
    coffee_choices = list(MENU.keys())
    selected_coffee = random.choice(coffee_choices)
    coffee_price = MENU[selected_coffee]['price']

    # Random payment (exact or slightly over)
    payment_options = [coffee_price, coffee_price + random.randint(1, 5)]
    payment = random.choice(payment_options)

    print(f"Random selection: {selected_coffee} (${coffee_price})")
    print(f"Random payment: ${payment}")

    with patch('builtins.input', side_effect=[selected_coffee, str(payment)]):
        _, output = capture_output(make_coffee, machine)

    print("Coffee purchase output:")
    print(output)
    print("Machine status after purchase:")
    show_data(machine)
    return machine


def random_test_case_4_insufficient_payment() -> dict:
    """Random Test Case 4: Random insufficient payment scenario."""
    print("=== RANDOM TEST CASE 4: Random Insufficient Payment ===")
    machine = create_coffee_machine()

    coffee_choices = list(MENU.keys())
    selected_coffee = random.choice(coffee_choices)
    coffee_price = MENU[selected_coffee]['price']

    # Random insufficient payment (1 to price-1)
    insufficient_payment = random.randint(1, max(1, coffee_price - 1))

    print(f"Random selection: {selected_coffee} (${coffee_price})")
    print(f"Random insufficient payment: ${insufficient_payment}")

    with patch('builtins.input',
               side_effect=[
                   selected_coffee,
                   str(insufficient_payment)
                   ]):
        _, output = capture_output(make_coffee, machine)

    print("Coffee purchase output:")
    print(output)
    print("Machine status after failed purchase:")
    show_data(machine)
    return machine


def random_test_case_5_admin_operations() -> dict:
    """Random Test Case 5: Random admin operations."""
    print("=== RANDOM TEST CASE 5: Random Admin Operations ===")
    machine = create_coffee_machine()

    # Start with random money amount
    initial_money = random.randint(20, 100)
    machine['money'] = initial_money

    print(f"Initial machine money: ${machine['money']}")

    # Random deposit amount
    deposit_amount = random.randint(10, 50)
    print(f"Random deposit amount: ${deposit_amount}")

    with patch('builtins.input', side_effect=[str(deposit_amount)]):
        _, output1 = capture_output(deposit_money, PASSWORD, machine)
    print("Deposit operation output:")
    print(output1)

    # Random withdraw amount (ensuring it doesn't exceed available money)
    max_withdraw = min(machine['money'], random.randint(5, 40))
    charity_choice = random.choice(['yes', 'no'])

    print(f"Random withdraw amount: ${max_withdraw}")
    print(f"Random charity choice: {charity_choice}")

    with patch('builtins.input',
               side_effect=[
                   str(max_withdraw),
                   charity_choice
                   ]):
        _, output2 = capture_output(withdraw_money, "1234", machine)
    print("Withdraw operation output:")
    print(output2)

    print("Final machine status:")
    show_data(machine)
    return machine


def random_test_case_6_resource_limits() -> dict:
    """Run 6 random test cases."""
    print("=== RANDOM TEST CASE 6: Random Resource Limits Test ===")
    machine = create_coffee_machine()

    # Create a scenario with random low resources for coffees
    machine['beans'] = random.randint(0, 30)  # Possibly not enough for some
    machine['water'] = random.randint(0, 300)  # Possibly not enough
    machine['milk'] = random.randint(0, 150)   # Possibly not enough
    machine['cups'] = random.randint(0, 2)     # Possibly not enough

    print("Machine with random low resources:")
    show_data(machine)

    # Try to make a random coffee
    coffee_choices = list(MENU.keys())
    selected_coffee = random.choice(coffee_choices)
    coffee_price = MENU[selected_coffee]['price']
    payment = coffee_price + random.randint(0, 3)  # Sufficient payment

    print(f"Attempting to make: {selected_coffee}")
    print(f"Required resources: {MENU[selected_coffee]}")
    print(f"Payment: ${payment}")

    with patch('builtins.input', side_effect=[selected_coffee, str(payment)]):
        _, output = capture_output(make_coffee, machine)

    print("Coffee attempt output:")
    print(output)
    print("Final machine status:")
    show_data(machine)
    return machine


def run_random_tests() -> list:
    """Run 6 random test cases."""
    print("RUNNING RANDOM COFFEE MACHINE TESTS")
    print(f"Random seed: {random.seed()}")  # For reproducibility if needed
    print("=" * 50)

    test_cases = [
        random_test_case_1_view_status,
        random_test_case_2_fill_machine,
        random_test_case_3_successful_purchase,
        random_test_case_4_insufficient_payment,
        random_test_case_5_admin_operations,
        random_test_case_6_resource_limits
    ]

    # Shuffle test cases for variety
    random.shuffle(test_cases)

    results = []
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n{'=' * 10} EXECUTING RANDOM TEST {i}/6 {'=' * 10}")
        try:
            result = test_case()
            results.append(result)
            print(f"{'=' * 10} TEST {i} COMPLETED {'=' * 10}")
        except Exception as e:  # noqa: BLE001  # Broad catch to keep randomized test loop running
            print(f"Error in test {i}: {e}")
            results.append(None)

    print(f"\n{'=' * 50}")
    print("ALL RANDOM TESTS COMPLETED!")
    print(f"Successful tests: {sum(1 for r in results if r is not None)}/6")
    return results


if __name__ == "__main__":
    # Set different random seed each time for true randomness
    import time
    random.seed(int(time.time()))
    run_random_tests()
