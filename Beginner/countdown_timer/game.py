"""
Countdown Timer
A visual countdown timer to learn time modules and loops.

How to Play:
1. Set hours, minutes, and seconds
2. Watch the countdown
3. Get notified when time's up!

Python Concepts:
- time module
- While loops
- String formatting
- System sounds
"""

import time
import sys


def display_welcome() -> None:
    """Display welcome message."""
    print("\n" + "="*50)
    print("  COUNTDOWN TIMER")
    print("="*50)
    print("\nSet a timer and watch it count down!")
    print("\nPython Concepts: time module, Loops, Formatting")


def get_time_values() -> tuple[int, int, int]:
    """Get time values from user.
    
    Returns:
        Tuple of (hours, minutes, seconds)
    """
    while True:
        try:
            hours = int(input("\nEnter hours (0-23): ").strip())
            minutes = int(input("Enter minutes (0-59): ").strip())
            seconds = int(input("Enter seconds (0-59): ").strip())
            
            if 0 <= hours <= 23 and 0 <= minutes <= 59 and 0 <= seconds <= 59:
                if hours + minutes + seconds > 0:
                    return hours, minutes, seconds
                print("Please set a time greater than 0!")
            else:
                print("Invalid time values. Please try again.")
        except ValueError:
            print("Invalid input. Please enter numbers.")


def format_time(hours: int, minutes: int, seconds: int) -> str:
    """Format time as HH:MM:SS.
    
    Args:
        hours: Hours
        minutes: Minutes
        seconds: Seconds
        
    Returns:
        Formatted time string
    """
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def display_timer(hours: int, minutes: int, seconds: int, total_seconds: int) -> None:
    """Display the countdown timer.
    
    Args:
        hours: Hours remaining
        minutes: Minutes remaining
        seconds: Seconds remaining
        total_seconds: Total seconds for progress
    """
    time_str = format_time(hours, minutes, seconds)
    
    # Progress bar
    elapsed = total_seconds - (hours * 3600 + minutes * 60 + seconds)
    progress = elapsed / total_seconds if total_seconds > 0 else 0
    bar_length = 30
    filled = int(bar_length * progress)
    bar = "█" * filled + "░" * (bar_length - filled)
    
    # Clear screen and display
    sys.stdout.write("\033c")  # Clear terminal
    sys.stdout.flush()
    
    print("\n" + "="*50)
    print("  ⏱️  COUNTDOWN TIMER")
    print("="*50)
    print(f"\n  Time Remaining: {time_str}")
    print(f"\n  [{bar}] {progress*100:.1f}%")
    print("\n" + "="*50)
    print("  Press Ctrl+C to stop")
    print("="*50)


def run_timer(hours: int, minutes: int, seconds: int) -> None:
    """Run the countdown timer.
    
    Args:
        hours: Hours to count down
        minutes: Minutes to count down
        seconds: Seconds to count down
    """
    total_seconds = hours * 3600 + minutes * 60 + seconds
    
    try:
        while total_seconds > 0:
            h = total_seconds // 3600
            m = (total_seconds % 3600) // 60
            s = total_seconds % 60
            
            display_timer(h, m, s, hours * 3600 + minutes * 60 + seconds)
            
            time.sleep(1)
            total_seconds -= 1
        
        # Timer complete
        sys.stdout.write("\033c")
        sys.stdout.flush()
        
        print("\n" + "="*50)
        print("  🔔 TIME'S UP!")
        print("="*50)
        print("\n  Your countdown has finished!")
        print("="*50)
        
        # Beep sound (works on most systems)
        for _ in range(3):
            print("\a", end="", flush=True)
            time.sleep(0.3)
        
    except KeyboardInterrupt:
        print("\n\n  ⏹️  Timer stopped!")
        remaining = format_time(total_seconds // 3600, (total_seconds % 3600) // 60, total_seconds % 60)
        print(f"  Time remaining: {remaining}")


def main() -> None:
    """Main timer loop."""
    display_welcome()
    
    while True:
        hours, minutes, seconds = get_time_values()
        
        total = hours * 3600 + minutes * 60 + seconds
        print(f"\n  Starting timer for {format_time(hours, minutes, seconds)}")
        print("  Press Enter to start...")
        input()
        
        run_timer(hours, minutes, seconds)
        
        again = input("\nSet another timer? (yes/no): ").strip().lower()
        if again not in ['yes', 'y']:
            break
    
    print("\nThanks for using Countdown Timer!")
    print("See you next time!")


if __name__ == "__main__":
    main()
