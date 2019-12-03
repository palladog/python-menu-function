class UserInterface:
    """A user interface with which other classes can communicate with
    the user.

    """

    def __init__(self):
        pass


    def ask_user(self, message: str) -> str:
        """Asks the user something and returns the user input.

        Args:
            message (str): The question asked to the user

        Returns:
            str: What the user inputs as the answer to the question
        
        """
        return input("\n" + message + "\n> ")


    def notify_user(self, message: str) -> None:
        """Prints a message to the user.

        Args:
            message (str): The message printed to the user
        
        """
        print(message)


    def choose_menu(self, heading: str, menu: dict) -> None:
        """Prints a menu and runs the function of the chosen menu option.

        Args:
            heading (str): The menu heading
            menu (dict): A nested dictionary in which each menu option
                has a label (which will be printed for the user to see)
                and a function (without the parenthesis) that will run
                if the user chooses that menu option.
        
        The nested dictionary must be modeled as followed:

            nested_dict = {
                1: {
                    "label": "",
                    "func": FUNC
                }
            }

        The nested dictionaries must have numeric names in ascending
        order, as there is a validation check for numeric values within
        the range of the length of the dictionary.

        When the user chooses a correct menu option, its "func" value
        will be inserted in the function below (which has parenthesis
        appended to it).

            menu[choice]["func"]()

        """ 

        self.notify_user(heading)

        # Prints menu by iterating through the dict
        for i in menu:
            self.notify_user(f"{i}. {menu[i]['label']}")
        

        while True:
            try:
                choice = int(self.ask_user("Choose a menu option").strip())
                # .strip() removes starting and ending spaces
                
                if choice in range(1, len(menu) + 1):
                    # Runs the function of the chosen menu option
                    menu[choice]["func"]()
                    return False
                
                else: 
                    self.notify_user("The number you input isn't among the menu options.")

            except(ValueError):
                self.notify_user("Only numbers allowed!")



    
