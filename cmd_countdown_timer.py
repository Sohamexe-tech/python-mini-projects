import time
import os

def clear_screen():
    """Clears the console screen for continuous display updates."""
    # Check operating system and use the appropriate command
    os.system('cls' if os.name == 'nt' else 'clear')

def format_time(seconds):
    """Converts a total number of seconds into HH:MM:SS format."""
    # divmod(a, b) returns the tuple (a // b, a % b)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    
    # Format the time components to always have two digits (e.g., 05)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

def countdown_timer():
    """Main function to run the timer logic."""
    print("--- Simple Countdown Timer ---")
    
    while True:
        try:
            # Get the duration from the user
            duration_input = input("Enter duration in seconds (e.g., 600 for 10 minutes) or 'q' to quit: ")
            
            if duration_input.lower() == 'q':
                return

            total_seconds = int(duration_input)
            
            if total_seconds <= 0:
                print("Please enter a positive duration.")
                continue

            break
        except ValueError:
            print("Invalid input. Please enter a whole number for the duration.")
    
    # Start the countdown
    while total_seconds >= 0:
        clear_screen()
        
        # Display the remaining time
        time_display = format_time(total_seconds)
        print("\n\n" + " " * 10 + "⏰ COUNTDOWN ⏰")
        print("=" * 30)
        print(f"    Time Remaining: {time_display}")
        print("=" * 30)
        
        # Pause execution for 1 second
        time.sleep(1)
        
        # Decrement the counter
        total_seconds -= 1
    
    # Final message
    clear_screen()
    print("\n\n" + " " * 10 + "🚨 TIME'S UP! 🚨")
    print("-" * 30)
    print("The countdown has reached zero.")
    print("-" * 30)


if __name__ == "__main__":
    countdown_timer()