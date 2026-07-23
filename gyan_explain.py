command_database = {
    "grep": {
        "description": "Search utility — finds lines in files that match a pattern.",
        "flags": {
            "-i": "Ignore case (uppercase/lowercase treated the same)",
            "-v": "Invert match — show lines that do NOT match",
            "-r": "Recursive — search through all files in a directory",
            "-n": "Show line numbers alongside matches",
            "-c": "Count — show only the number of matching lines, not the lines themselves",
            "-l": "Show only filenames that contain a match, not the matches themselves",
        }
    },
    "find": {
        "description": "Search utility — locates files and directories based on conditions like name, type, or size.",
        "flags": {
            "-name": "Match files by name (supports wildcards like *.py)",
            "-type": "Filter by type — f for file, d for directory",
            "-size": "Filter by file size (e.g. +100M for files over 100MB)",
            "-mtime": "Filter by when the file was last modified (in days)",
            "-delete": "Delete matching files (use carefully!)",
        }
    },
    "chmod": {
        "description": "Changes file permissions — controls who can read, write, or execute a file.",
        "flags": {
            "-R": "Recursive — apply the permission change to all files in a directory",
            "+x": "Add execute permission",
            "-x": "Remove execute permission",
            "+r": "Add read permission",
            "+w": "Add write permission",
        }
    },
}

def handle_explain(parts):
    if len(parts) < 2 :
        print("Usage: explain <command> [flags...]")
        return 

    cmd_name = parts[1]

    if cmd_name not in command_database:
        print(f"No explanation available for '{cmd_name}'.")
        return

    entry = command_database[cmd_name]
    print(f"\n{cmd_name} - {entry['description']}")

    remaining_args = parts[2:]

    for args in remaining_args:
        if args.startswith("-") and not args.startswith("--"):
            for char in args[1:]:
                flag = "-" + char
                if flag in entry["flags"] :
                    print(f" {flag} {entry['flags'][flag]}")
                else:
                    print(f" {flag} (no explanation available)")

        else :
            print(f" {args} (Argument - likely a file name or target)")

    print()


    