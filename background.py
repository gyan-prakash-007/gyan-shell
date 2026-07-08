import subprocess

def handle_background(command):
    command = command.strip().rstrip("&").strip()
    parts = command.split()


    p = subprocess.Popen(parts)
    print(f"[Background job startd] PID : {p.pid}")


