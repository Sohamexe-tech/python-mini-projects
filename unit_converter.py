def convert_value(value, factor):
    """Performs the conversion: value * factor."""
    return value * factor

# A dictionary storing the conversion factor for 1 unit of the 'from' measure 
# to the 'to' measure.
# Example: 1 kilogram = 2.20462 pounds
CONVERSIONS = {
    # Key: (From Unit, To Unit) : Factor
    ("kg", "lb"): 2.20462,
    ("lb", "kg"): 0.453592,
    ("km", "mi"): 0.621371,
    ("mi", "km"): 1.60934,
    ("C", "F"): lambda x: (x * 9/5) + 32, # Lambda for Celsius to Fahrenheit
    ("F", "C"): lambda x: (x - 32) * 5/9  # Lambda for Fahrenheit to Celsius
}

def main():
    """Runs the main conversion loop."""
    print("--- Basic Unit Converter ---")
    print("Available Conversions: kg<->lb, km<->mi, C<->F")
    
    while True:
        try:
            # Get conversion type
            conversion_type = input("\nEnter conversion (e.g., kg to lb, C to F) or 'q' to quit: ").strip().lower()
            
            if conversion_type == 'q':
                break
            
            # Parse input, expecting "unit1 to unit2"
            parts = conversion_type.split(' to ')
            if len(parts) != 2:
                print("Invalid format. Use 'UNIT1 to UNIT2' (e.g., 'km to mi').")
                continue
                
            from_unit, to_unit = parts[0].strip(), parts[1].strip()
            
            # Check if the conversion is supported
            conversion_key = (from_unit, to_unit)
            if conversion_key not in CONVERSIONS:
                print(f"Conversion from {from_unit} to {to_unit} is not supported.")
                continue

            # Get the value to convert
            value_input = input(f"Enter the value in {from_unit}: ").strip()
            value = float(value_input)
            
            # Get the conversion factor/function
            converter = CONVERSIONS[conversion_key]
            
            # Perform conversion
            if callable(converter):
                # If it's a lambda function (for temperature)
                result = converter(value)
            else:
                # If it's a simple multiplication factor
                result = convert_value(value, converter)

            # Display the result
            print(f"\n{value} {from_unit} is equal to {result:.4f} {to_unit}.")

        except ValueError:
            print("Invalid value entered. Please enter a valid number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()