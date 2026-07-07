# gyan-shell

A command-line shell built from scratch in Python — supports real command execution, pipes, redirects, background processes, and a few personal touches. Built to actually understand how a shell works under the hood, instead of just using one every day without thinking about it.

## Why I built this

I use a terminal every day but never really thought about what's actually happening when I type a command and hit Enter. So I decided to build my own shell from scratch — implementing real process execution, pipes, and redirects myself — to understand how tools like bash and zsh actually work internally.

## Features

- **Real command execution** — runs any actual program available on your system
- **`cd` built-in** — correctly changes the shell's own working directory (a subtle OS-level detail: child processes can't change their parent's directory, so `cd` has to be handled specially)
- **Pipes (`|`)** — chain multiple commands together, e.g. `ls | grep py`
- **Redirects (`>`, `<`)** — write output to a file, or read input from a file
- **Background processes (`&`)** — run something without blocking the shell, e.g. `sleep 10 &`
- **Graceful error handling** — bad commands print a clean message instead of crashing the shell
- **`gyan` command** — a little personal touch, prints my info/bio when you run it

## Usage

```bash
python3 shell.py
```

Example session:

```console
$ python3 shell.py

gyan-shell> ls -la
gyan-shell> ls | grep shell
gyan-shell> ls > output.txt
gyan-shell> sort < output.txt
gyan-shell> sleep 5 &
gyan-shell> cd testfolder
gyan-shell> gyan
gyan-shell> exit
```


## Project Structure

```text
gyan-shell
│
├── shell.py
│   └── Main REPL loop that ties everything together
│
├── gyan_builtins.py
│   └── Built-in commands (`cd`, `exit`, `gyan`)
│
├── pipes.py
│   └── Pipe (`|`) implementation
│
├── redirects.py
│   └── Input/Output redirection (`<`, `>`)
│
├── background.py
│   └── Background process handling (`&`)
│
└── README.md
```

## What I Learned

- How a shell actually launches other programs as separate OS processes
- Why `cd` can't work like a normal command (child processes can't change their parent's directory — a real OS-level boundary)
- How Unix pipes work under the hood — connecting one process's output stream directly to another's input stream
- The difference between `subprocess.run()` (blocking) and `subprocess.Popen()` (non-blocking) — and why background processes need the latter

## Future Improvements

- Command history (↑/↓ to recall previous commands)
- Tab-completion
- Job control (`jobs`, `fg`, `bg`, `kill`)
- Combined pipes + redirects in a single command
- Proper signal handling (Ctrl+C should stop the running command, not the whole shell)


> Built to understand how shells work—not just how to use them.