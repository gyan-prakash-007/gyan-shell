import subprocess
import os 

def main():
    while True :
        command = input("gyan-shell>")

        if command.strip() == "":
            continue

        parts = command.split()

        if parts[0] =="exit":
            print("Hasta la Vista")
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
