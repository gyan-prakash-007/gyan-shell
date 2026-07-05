import subprocess

def main():
    while True :
        command = input("gyan-shell>")

        if command.strip() == "":
            continue

            parts = command.split()
            subprocesses.run(parts)


if __name__ == "__main__":
    main()