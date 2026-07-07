import subprocess

def handle_pipe(command):
    commands = command.split("|")
    commands = [cmd.strip().split() for cmd in commands]


    processses = []
    previous_stdout = None

    for i, cmd in enumerate(commands):
        if i == len(commands)-1 :
            p = subprocess.Popen(cmd , stdin=previous_stdout)
        else :
            p = subprocess.Popen(cmd, stdin= previous_stdout, stdout=subprocess.PIPE)
            previous_stdout = p.stdout
        processses.append(p)

    for p in processses:
        p.wait()