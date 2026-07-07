import subprocess

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
