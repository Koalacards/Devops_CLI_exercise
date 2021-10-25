from src.cli import CLIObject

def main():
    json_path = input("Select a json file by indicating the json file path.\n")

    cli = CLIObject(json_path)

    while True:
        command_line_input = input(f" {json_path} % ")

        if command_line_input == "ls":
            print(cli.ls())

        split = command_line_input.split()
        if split[0] == "get":
            #This is in case the username has any spaces in it
            username = "".join(split[1:])
            print(cli.get(username))

if __name__ == "__main__":
    main()