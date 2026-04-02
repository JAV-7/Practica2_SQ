
# test_runner.py

"""
Wrapper to run the random tests from `test_random_coffee_machine.py`.

This avoids running the test module on import and provides a single function
that `main.py` can call safely.
"""

try:
    # Import the test entry point if available.
    from test_random_coffee_machine import (
        run_random_tests,  # type: ignore[attr-defined]
    )
except ImportError:
    def run_random_tests() -> list:
        """
        Fallback function used when the random test suite cannot be imported.

        Returns
        -------
        list
            An empty list, signaling that no tests were executed.
        """
        print(
            "'run_random_tests' could not be imported from "
            "test_random_coffee_machine.py."
        )
        return []


def run_random_tests_from_main() -> None:
    """
    Execute the random tests and present a short summary for the main menu.

    Returns
    -------
    None
    """
    print("\n=== RUN RANDOM TESTS ===")
    results = run_random_tests()
    total = len(results)
    ok = sum(1 for r in results if r is not None)
    print("\nTest summarys:")
    print(f"  - Tests runs: {total}")
    print(f"  - Successful tests:  {ok}")
    print("===================================\n")
