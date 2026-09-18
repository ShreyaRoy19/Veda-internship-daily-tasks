def safe_calculator():
    """
    Demonstrates robust exception handling in Python by safely managing
    invalid numeric inputs, division by zero, missing values, and other expected runtime errors.
    """
    print("=== Welcome to the Safe Calculator Program ===")
    
    try:
       
        raw_num1 = input("Enter the first number: ")
        raw_num2 = input("Enter the second number: ")
        
        
        if not raw_num1.strip() or not raw_num2.strip():
            raise ValueError("Input value cannot be empty or blank.")

        
        num1 = float(raw_num1)
        num2 = float(raw_num2)

        
        result = num1 / num2

    except ValueError as ve:
        print(f"\n[ValueError Caught]: Invalid input format or empty value -> {ve}")
        print("Hint: Please enter valid integer or decimal numbers.")
    
    except ZeroDivisionError as zde:
        print(f"\n[ZeroDivisionError Caught]: Division error -> {zde}")
        print("Hint: The second number (denominator) cannot be zero.")
    
    except TypeError as te:
        print(f"\n[TypeError Caught]: Data type mismatch -> {te}")
    
    except OverflowError as oe:
        print(f"\n[OverflowError Caught]: Result is too large to represent -> {oe}")
    
    except Exception as e:
       
        print(f"\n[Unexpected Error Caught]: {type(e).__name__} -> {e}")
    
    else:

        print(f"\n[Success]: {num1} divided by {num2} equals {result:.4f}")
    
    finally:
        
        print("\n[Finally Block]: Execution complete. Cleaning up resources...")


if __name__ == "__main__":
    safe_calculator()
