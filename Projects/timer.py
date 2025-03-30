from playsound import playsound
import time

CLEAR = "\033[2J"  # basically cleans the screen
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    """
    Function to play an alarm sound after a specified number of seconds.
    
    Args:
        seconds (int): The number of seconds to wait before playing the alarm sound.
    """
    time_elapsed = 0 # variable to keep track of the elapsed time
    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)  # it means wait for 1 second
        time_elapsed += 1
        
        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60
        print(f"{CLEAR_AND_RETURN}{minutes_left:02}:{seconds_left:02d}")

    
    playsound("Projects/alarm.mp3")

minutes = int(input("Enter the number of minutes: "))
seconds = int(input("Enter the number of seconds: "))
total_seconds = (minutes * 60) + seconds
alarm(total_seconds)
