from modules.colors import BOLD, BLUE, RESET, GREEN, CYAN, RED, YELLOW
from modules.simulate_neofetch import neofetch
from modules.calculator import calculator

class App:
  def __init__(self):
    self.users = []

  def run(self):
    while True:
      welcome = f"{BOLD}Welcome to the app!{RESET}"
      menu = f"\n {CYAN}1. Login{RESET} \n {BLUE}2. Register{RESET}"
      print(welcome, menu)

      try:
        option = int(input("Enter an option: "))
      except ValueError:
        print(f"{RED}Invalid input, please enter a number.{RED}")
        continue

      if option == 1:
        if self.sign_in():
          self.main_menu()
      elif option == 2:
        print(self.sign_up())

  def sign_in(self):
    user = input("Enter your user: ")
    password = input("Enter your password: ")
    for u in self.users:
      if u['user'] == user and u['password'] == password:
        print(f"{BOLD}Welcome {user}!{RESET}")
        return True
    print("Invalid user or password")
    return False

  def sign_up(self):
    user = input("Enter your user: ")
    password = input("Enter your password: ")
    self.users.append({'user': user, 'password': password})
    return f"{BLUE}User registered!{RESET}"

  def main_menu(self):
    while True:
      menu = f"\n {GREEN}1. Neofetch{RESET} \n {YELLOW}2. Calculator{RESET} \n {BLUE}3. Logout{RESET} \n {RED}4. Exit{RESET}"
      print(menu)

      try:
        option = int(input("Enter an option: "))
      except ValueError:
        print(f"{RED}Invalid input, please enter a number.{RESET}")
        continue

      if option == 1:
        self.use_neofetch()
      elif option == 2:
        self.use_calculator()
      elif option == 3:
        break
      elif option == 4:
        exit()

  def use_neofetch(self):
    neofetch()

  def use_calculator(self):
    calculator()

if __name__ == "__main__":
  app = App()
  app.run()
