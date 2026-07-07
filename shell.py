import subprocess
from pipes import handle_pipe
from redirects import handle_redirect_in, handle_redirect_out
from background import handle_background
from gyan_builtins import handle_cd, handle_exit








def main():
    while True :

        command = input("gyan-shell>")

        if command.strip().endswith("&"):
            handle_background(command)
            continue 
       

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
            handle_exit()
            break

        

        try:
            if parts[0] == "cd":
               handle_cd

            else:
             subprocess.run(parts)
        except FileNotFoundError:
            print(f"gyan-shell: command not found or no such file/directory: {command}")
        except Exception as e :
            print(f"gyan-shell: error ({type(e).__name__}):{e}")
         

if __name__ == "__main__":
    main()
