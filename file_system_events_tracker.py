import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/CHH/Downloads"

class FileMovementHandler(FileSystemEventHandler):
    def on_created(self,event):
        print(f"hey, {event.src_path} has been created !")

    def on_deleted(self,event):
        print(f"opps! someone deleted  {event.src_path} !")

    def on_modified(self,event):
        print(f"hey, someone modified {event.src_path} !")

    def on_moved(self,event):
        print(f"hey, someone moved{event.src_path} !")    



    observer=Observer()
    observer.schedule(FileSystemEventHandler,from_dir,recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(2)
            print("running") 
    except KeyboardInterrupt:
        print("stopped!")
        observer.stop
           
