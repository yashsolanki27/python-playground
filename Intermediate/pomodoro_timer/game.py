"""
Pomodoro Timer
A productivity timer using the Pomodoro technique. Learn time management and loops.

How to Play:
1. Set work duration (default 25 min)
2. Work until timer ends
3. Take a short break (5 min)
4. After 4 pomodoros, take a long break (15 min)

Python Concepts:
- time module
- While loops
- Counter tracking
- String formatting
"""

import time
import sys


DEFAULT_WORK = 25 * 60      # 25 minutes
DEFAULT_SHORT_BREAK = 5 * 60  # 5 minutes
DEFAULT_LONG_BREAK = 15 * 60  # 15 minutes


def display_welcome() -> None:
    """Display welcome message."""
    print("\n" + "="*50)
    print("  🍅 POMODORO TIMER")
    print("="*50)
    print("\nBoost your productivity!")
    print("\nPomodoro Technique:")
    print("  1. Work for 25 minutes")
    print("  2. Take a 5-minute break")
    print("  3. After 4 pomodoros, take 15-min break")
    print("\nPython Concepts: time, Loops, Counters")


def get_settings() -> tuple[int, int, int]:
    """Get timer settings from user.
    
    Returns:
        Tuple of (work, short_break, long_break) in seconds
    """
    print("\n  Use default settings? (25/5/15 minutes)")
    choice = input("  (yes/no): ").strip().lower()
    
    if choice in ['no', 'n']:
        try:
            work = int(input("  Work minutes (default 25): ").strip() or "25")
            short = int(input("  Short break minutes (default 5): ").strip() or "5")
            long_break = int(input("  Long break minutes (default 15): ").strip() or "15")
            return work * 60, short * 60, long_break * 60
        except ValueError:
            pass
    
    return DEFAULT_WORK, DEFAULT_SHORT_BREAK, DEFAULT_LONG_BREAK


def display_timer(seconds: int, label: str) -> None:
    """Display countdown timer.
    
    Args:
        seconds: Seconds remaining
        label: Timer label
    """
    mins = seconds // 60
    secs = seconds % 60
    
    # Progress
    total = DEFAULT_WORK if "Work" in label else DEFAULT_SHORT_BREAK
    progress = 1 - (seconds / total) if total > 0 else 1
    bar = "█" * int(progress * 20) + "░" * (20 - int(progress * 20))
    
    sys.stdout.write("\033c")
    sys.stdout.flush()
    
    print("\n" + "="*50)
    print(f"  🍅 {label}")
    print("="*50)
    print(f"\n  Time: {mins:02d}:{secs:02d}")
    print(f"\n  [{bar}]")
    print("\n" + "="*50)
    print("  Press Ctrl+C to skip")
    print("="*50)


def run_timer(seconds: int, label: str) -> bool:
    """Run a countdown timer.
    
    Args:
        seconds: Duration in seconds
        label: Timer label
        
    Returns:
        True if completed, False if interrupted
    """
    try:
        while seconds > 0:
            display_timer(seconds, label)
            time.sleep(1)
            seconds -= 1
        
        # Completion sound
        for _ in range(3):
            print("\a", end="", flush=True)
            time.sleep(0.3)
        
        return True
        
    except KeyboardInterrupt:
        print(f"\n\n  ⏭️  Skipping {label}...")
        return False


def main() -> None:
    """Main Pomodoro loop."""
    display_welcome()
    
    work, short, long_break = get_settings()
    
    pomodoro_count = 0
    total_pomodoros = 0
    
    print(f"\n  Settings: {work//60}min work / {short//60}min short / {long_break//60}min long")
    print("  Press Enter to start...")
    input()
    
    try:
        while True:
            pomodoro_count += 1
            total_pomodoros += 1
            
            print(f"\n  🍅 Pomodoro #{pomodoro_count}")
            
            # Work session
            run_timer(work, f"WORK - Pomodoro #{pomodoro_count}")
            
            # Check if long break needed
            if pomodoro_count % 4 == 0:
                print(f"\n  🎉 Great job! {pomodoro_count} pomodoros done!")
                print("  Time for a long break!")
                run_timer(long_break, "LONG BREAK")
                pomodoro_count = 0
            else:
                print(f"\n  ✅ Pomodoro #{pomodoro_count} complete!")
                print("  Take a short break!")
                run_timer(short, "SHORT BREAK")
            
            # Continue?
            print(f"\n  Total pomodoros completed: {total_pomodoros}")
            choice = input("\n  Start another pomodoro? (yes/no): ").strip().lower()
            if choice not in ['yes', 'y']:
                break
    
    except KeyboardInterrupt:
        print("\n\n  ⏹️  Pomodoro session ended!")
    
    print(f"\n  📊 Session complete!")
    print(f"  Total pomodoros: {total_pomodoros}")
    print(f"  Estimated focus time: {total_pomodoros * work // 60} minutes")
    
    print("\nThanks for using Pomodoro Timer!")
    print("Stay productive! 🍅")


if __name__ == "__main__":
    main()
