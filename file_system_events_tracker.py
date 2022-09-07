from asyncio import events
from importlib.resources import path
import sys
from this import d
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


from_dir = r"C:/Users/tomas/Downloads"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}


class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"{event.src_path} ha sido creado")

    def on_modified(self, event):
         print(f"{event.src_path} ha sido modificado")

    def on_moved(self, event):
         print(f"{event.src_path} ha sido movido")

    def on_deleted(self, event):
         print(f"{event.src_path} ha sido eliminado")           

 

                       
event_handler = FileMovementHandler()

observer = Observer()

observer.schedule(event_handler, from_dir, recursive=True)

observer.start()

try:
   while True:
    time.sleep(2)
    print("ejecutando...")
except KeyboardInterrupt:
    print("detenido")
    observer.stop()

    
