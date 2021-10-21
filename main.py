from src.cli import CLIObject

def main():
    json_path = input("Select a json file by indicating the json file path.")

    cli = CLIObject(json_path)

    while True:
        command_line_input = input()

        if command_line_input == "ls":
            print(cli.ls())
        



if __name__ == "__main__":
    main()