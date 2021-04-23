def split(*receipts: dict):
    """
    Compute equalization payments between roommates.
    All names listed for a given receipt will be considered to be financially responsible.
    The most efficient repayment scheme is computed for all receipts.

    Args:
        *receipts: Dictionaries of payment history.
    """

    # Make sure at least one receipt was passed
    if not receipts:
        print("ERROR: Please provide at least one receipt to the split function.")
        exit()

    # Type check
    for receipt in receipts:
        for name, price in receipt.items():
            if not isinstance(name, str):
                print(f"ERROR: Name {name} is not a valid string.")
                exit()
            if not isinstance(price, (float, int)):
                print(f"ERROR: Price {price} is not a valid float/int.")
                exit()

    # Track overall payments 
