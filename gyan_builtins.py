import os 

def handle_cd(parts):
    target_dir = parts[1] if len(parts) > 1 else os.path.expanduser("~")
    os.chdir(target_dir)

def handle_exit():
    print("Hasta la Vista, Baby")

