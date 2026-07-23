import os 
import glob

def handle_cd(parts):
    target_dir = parts[1] if len(parts) > 1 else os.path.expanduser("~")
    os.chdir(target_dir)

def handle_exit():
    print("Hasta la Vista, Baby")

def print_gyan():
    print("=" * 70)
    print("Gyan Prakash")
    print("CS student | Fitness enthusiast")
    print("Building gyan-shell to understand how a real shell works under the hood.")
    print("GitHub: github.com/gyan-prakash-007")
    print("Fun fact: I also have an Instagram — come say hi! @grindwith.gp")
    print("=" * 70)

command_history = []

def add_to_history(command):
    command_history.append(command)

def print_history():
    for i, cmd in enumerate(command_history, start=1):
        print(f"{i} {cmd}")


