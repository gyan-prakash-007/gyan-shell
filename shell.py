import subprocess
import os 


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


def handle_redirect_out(command):
    patrs = command.split(">")
    cmd_parts = patrs[0].strip().split()
    filename = patrs[1].strip()

    with open(filename,"w") as f:
        subprocess.run(cmd_parts, stdout=f)


def handle_redirect_in(command):
    parts = command.split("<")
    cmd_parts = parts[0].strip().split()
    filename = parts[1].strip()

    with open(filename, "r") as f:
        subprocess.run(cmd_parts,stdin=f)



def main():
    while True :
        command = input("gyan-shell>")

        if command.strip() == "":
            continue

        parts = command.split()

        if "|" in command:
            handle_pipe(command)
            continue

        if ">" in command:
            handle_redirect_out(command)
            continue

        if "<" in command :
            handle_redirect_in(command)
            continue

        if parts[0] =="exit":
            print("Hasta la Vista, Baby")
            break

        

        try:
            if parts[0] == "cd":
                target_dir = parts[1] if len(parts) >1 else os.path.expanduser("~")
                os.chdir(target_dir)

            else:
             subprocess.run(parts)
        except FileNotFoundError:
            print(f"gyan-shell: command not found or no such file/directory: {command}")
        except Exception as e :
            print(f"gyan-shell: error ({type(e).__name__}):{e}")
         

if __name__ == "__main__":
    main()
