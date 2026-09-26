# ==========================================
# 1. GLOBAL SCOPE
# ==========================================
# This variable is declared at the top level of the script.
# It can be read anywhere in this file.
global_var = "I am Global"


def demonstrate_functions(item_name, price, discount=0.10):
    """
    Demonstrates basic function parameters, default values, and local scope.
    """
    # ==========================================
    # 2. LOCAL SCOPE
    # ==========================================
    # 'final_price' and parameters (item_name, price, discount) only exist inside this function.
    savings = price * discount
    final_price = price - savings

    # Accessing global variable inside a function (read-only)
    print(f"[{global_var}] Calculating price for: {item_name}")

    # Returning multiple values as a tuple
    return final_price, savings


def demonstrate_scope():
    """
    Demonstrates Enclosing (Nonlocal) vs. Local Scope and the 'global' keyword.
    """
    # ==========================================
    # 3. ENCLOSING SCOPE
    # ==========================================
    counter = 10  # Outer function variable

    def inner_function():
        # ==========================================
        # 4. LOCAL SCOPE (Inner)
        # ==========================================
        # 'nonlocal' allows us to modify the variable in the enclosing scope
        nonlocal counter
        counter += 5
        print(f"Counter inside inner_function (modified): {counter}")

    inner_function()
    print(f"Counter in demonstrate_scope (after inner call): {counter}")


def modify_global():
    """
    Demonstrates using the 'global' keyword to modify a global variable.
    """
    global global_var
    global_var = "I am Global (Modified!)"


# ==========================================
# EXECUTION / TESTING THE CODE
# ==========================================
if __name__ == "__main__":
    print("--- 1. Function Call & Local Scope ---")
    # Positional and default arguments
    total, saved = demonstrate_functions("Laptop", 1000)
    print(f"Final Price: ${total:.2f} (Saved: ${saved:.2f})\n")

    # Keyword arguments (overriding default discount)
    total_custom, saved_custom = demonstrate_functions(
        item_name="Phone", price=500, discount=0.20
    )
    print(f"Custom Price: ${total_custom:.2f} (Saved: ${saved_custom:.2f})\n")

    print("--- 2. Enclosing Scope & Nonlocal Keyword ---")
    demonstrate_scope()
    print()

    print("--- 3. Modifying Global Scope ---")
    print(f"Before function: {global_var}")
    modify_global()
    print(f"After function:  {global_var}")