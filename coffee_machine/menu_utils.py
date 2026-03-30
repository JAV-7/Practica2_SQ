
# menu_utils.py

"""
Menu input utilities for main.py.

Centralize validations and small UI helpers.
"""

from collections.abc import Iterable


def read_option(prompt: str, valid: Iterable[str]) -> str:
    """
    Read a user option and validate it against a set of valid options.

    Parameters
    ----------
    prompt : str
        The message to show to the user before reading input.
    valid : Iterable[str]
        The allowed values for the option.

    Returns
    -------
    str
        The validated option, normalized as a string.
    """
    valid_set = {str(v) for v in valid}
    while True:
        choice = input(prompt).strip()
        if choice in valid_set:
            return choice
        print(f"Invalid choice. Please select one of::"
              f"{', '.join(sorted(valid_set))}.")


def press_enter_to_continue(msg: str = "PRESS ENTER to continue...") -> None:
    """
    Wait for the user to press Enter, showing an optional message.

    Parameters
    ----------
    msg : str, optional
        The message to display before waiting for input, by default
        "PRESS ENTER to continue...".

    Returns
    -------
    None
    """
    try:
        input(f"\n{msg}")
    except KeyboardInterrupt:
        print()
