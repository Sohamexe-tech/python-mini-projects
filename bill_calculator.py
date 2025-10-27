def calculate_tip():
    """Prompts the user for bill details and calculates the tip and total."""
    
    print("--- Simple Tip Calculator ---")

    try:
        # 1. Get Bill Amount
        bill_amount = float(input("Enter the total bill amount: $"))
        
        # 2. Get Tip Percentage
        tip_percentage = float(input("Enter the tip percentage (e.g., 15 for 15%): "))
        
        # 3. Calculate Tip and Total
        tip_amount = bill_amount * (tip_percentage / 100)
        total_amount = bill_amount + tip_amount
        
        # 4. Display Core Results
        print("\n" + "=" * 30)
        print("CALCULATION SUMMARY")
        print("-" * 30)
        print(f"Bill Amount:   ${bill_amount:.2f}")
        print(f"Tip Percentage: {tip_percentage:.0f}%")
        print(f"Tip Amount:    ${tip_amount:.2f}")
        print(f"Total Due:     ${total_amount:.2f}")
        print("-" * 30)
        
        # --- Optional Splitting ---
        
        # 5. Ask to Split the Bill
        people = input("How many people are splitting the bill? (Enter 1 if not splitting): ")
        
        try:
            num_people = int(people)
        except ValueError:
            num_people = 1
        
        if num_people > 1:
            per_person = total_amount / num_people
            print(f"Each person pays: ${per_person:.2f}")
            print("=" * 30)
            
    except ValueError:
        print("\nError: Please enter a valid number for the bill amount and tip percentage.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    calculate_tip()