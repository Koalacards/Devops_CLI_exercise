import json

class CLIObject:
    def __init__(self, json_path:str):
        self.employee_record = self._get_json(json_path)

    def _get_json(self, json_path:str):
        """Gets the JSON file as described by the json path.

        Args:
            json_path (str): The file path to the JSON file

        Raises:
            FileNotFoundError: The file with the given path cannot be found
            json.decoder.JSONDecodeError: There was an error when converting
            the file from JSON to python formatting (bad JSON formatting, or
            the file is not JSON)

        Returns:
            List: List of employee records (converted from JSON format)
        """
        try:
            file = open(json_path)
            file_json = json.load(file)
            return file_json
        except FileNotFoundError:
            raise FileNotFoundError(f"File with path {json_path} could not be found.")
        except json.decoder.JSONDecodeError:
            raise json.decoder.JSONDecodeError(f"The file at path {json_path} could not be decoded. Make sure that it is a json file and is formatted correctly.")
        
    def ls(self):
        """
        Prints out a list of all of the employees (usernames only)
        in the employee record
        """
        return_str = "Current Employee Usernames:\n"
        employee_usernames = []
        for employee in self.employee_record:
            username = employee.get("username", None)
            employee_usernames.append(username)
        return_str+= "\n".join(employee_usernames)

        return return_str
    
    def get(self, username:str):
        """Prints out the information about an employee with a given username

        Args:
            username (str): The username passed in
        """
        for employee in self.employee_record:
            employee_username= employee.get("username", None)
            if username == str(employee_username):
                firstname = str(employee.get("firstname", None))
                lastname = str(employee.get("lastname", None))
                department = str(employee.get("department", None))
                return_string = f"Employee information for username {username}: \n \
                First name: {firstname} \n \
                Last name: {lastname} \n \
                Department: {department}" 
                return return_string
        