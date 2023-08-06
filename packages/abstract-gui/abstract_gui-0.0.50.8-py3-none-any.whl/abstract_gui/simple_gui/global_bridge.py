class WindowGlobalBridge:
        """
    A class to manage the global variables shared between different scripts.

    Attributes:
        global_vars (dict): A dictionary to store global variables for each script.
        
    Methods:
        __init__(self):
            Initializes the WindowGlobalBridge with an empty dictionary for global_vars.

        retrieve_global_variables(self, script_name, global_variables):
            Stores the global variables of a script in the global_vars dictionary.

        return_global_variables(self, script_name):
            Returns the global variables of a script.
    """
    def __init__(self):
        """
        Initializes the WindowGlobalBridge with an empty dictionary for global_vars.
        """
        self.global_vars = {}

    def retrieve_global_variables(self, script_name, global_variables):
        """
        Stores the global variables of a script in the global_vars dictionary.

        Args:
            script_name (str): The name of the script.
            global_variables (dict): The global variables to store for the script.
        """
        self.global_vars[script_name] = global_variables
        
    def return_global_variables(self, script_name):
        """
        Returns the global variables of a script.

        Args:
            script_name (str): The name of the script.

        Returns:
            dict: The global variables of the script. If no global variables are found, it returns an empty dictionary.
        """
        return self.global_vars.get(script_name, {})
