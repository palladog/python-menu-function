# python-menu-function
A menu solution for Python console applications

## Problem
When coding simple Python console applications, I was faced with a somewhat time-consuming annoyance: unnecessary repetition of menu functions. 

I always had a main menu function in a boundary class that both printed and got the user choice for me (which I then could use to decide what function to run), but I still felt I could effectivize the code. Furthermore, the main menu function was useless when I needed to implement other menu functions, because it was static and hard-coded to the main menu.

I needed to find a better solution – one that meant I could define every aspect of a menu, and then send that as an argument to a menu function that could print the menu, get the user choice, and run the function of the chosen menu option.


## Solution
```python
menu = {
    1: {
        "label": "",
         "func": FUNC
    }
}

choice = input("Choose a menu option")

menu[choice]["func"]()

```
The answer was nested dictionaries! By creating a menu dictionary, with one nested dictionary per menu option, I could store:
* The menu option index (as the name of the nested dictionary)
* The label (to be printed to the user with the other menu options)
* The name of the function to be called (if the user chooses that menu option)

This means I only need to call *one* function each time I need to run any kind of menu. It also means I can store the menus in JSON files.

Below is a condensed example of this solution. Look at the Python files for the complete code with docstrings and comments!

```python
# userinterface.py

class UserInterface:

    def __init__(self):
        pass
        

    def ask_user(self, message: str) -> str:
        return input("\n" + message + "\n> ")


    def notify_user(self, message: str) -> None:
        print(message)


    def choose_menu(self, heading: str, menu: dict) -> None:
        self.notify_user(heading)

        for i in menu:
            self.notify_user(f"{i}. {menu[i]['label']}")

        while True:
          try:
              choice = int(self.ask_user("Choose a menu option").strip())

              if choice in range(1, len(menu) + 1):
                  menu[choice]["func"]()
                  return False

              else: 
                  self.notify_user("The number you input isn't among the menu options.")

            except(ValueError):
                self.notify_user("Only numbers allowed!")


# app.py

class App:
    """The main class of the app."""

    def __init__(self):
        self.ui = UserInterface()

    
    def method1(self):
        print("Method 1: Success!")
    
    
    def app_menu(self):
        """The main menu of the app."""

        MAIN_MENU = {
            1: {
                "label": "Method 1",
                "func": self.method1
            }
        }

        self.ui.choose_menu("MAIN MENU", MAIN_MENU)
```
