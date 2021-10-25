from src.cli import CLIObject

def main():
    json_path = input("Select a json file by indicating the json file path.\n")

    cli = CLIObject(json_path)

    while True:
        command_line_input = input(f" {json_path} % ")
        split = command_line_input.split()

        if split[0] == "ls":
            print(cli.ls())
        elif split[0] == "get":
            #This is in case the username has any spaces in it
            if len(split) > 1:
                username = "".join(split[1:])
                print(cli.get(username))
            else:
                print(f"Error: No username passed into the get function.")
        else:
            print(f"Command {split[0]} could not be found. The commands are 'ls' and 'get <username>'")

if __name__ == "__main__":
    main()