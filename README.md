# Devops_CLI_exercise
Python 3 CLI created as part of a Devops exercise. Uses docker-compose and dockerfile to run in a container.

## How to run

To run the CLI application, run the command
`docker-compose run --rm cli`

Upon the building of the docker container, you will recieve a prompt to 
enter the path to the JSON file. You can enter `test_json.json` or add
your own json file in the root directory to test.

From there, you should be prompted with `[Your JSON path] % `, which is similar to shell command prompt to enter a command. From there, you can enter either:
-  `ls`, to recieve a list of usernames in the employee database
-  `get <username>` to recieve specific information about one username

## Tests

There are three basic pytest tests that cover basic capabilities of the CLIObject class. You can run those in a docker container as well using the command
`docker-compose run --rm test`
