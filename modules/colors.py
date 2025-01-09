# Define colors using ANSI escape sequences
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[0m'

# Background colors
BG_RED = '\033[41m'
BG_GREEN = '\033[42m'
BG_YELLOW = '\033[43m'
BG_BLUE = '\033[44m'
BG_MAGENTA = '\033[45m'
BG_CYAN = '\033[46m'
BG_WHITE = '\033[47m'

# Additional styles
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

# Example of use
def example():
  print(f"{RED}Text in red{RESET}")
  print(f"{GREEN}Text in green{RESET}")
  print(f"{YELLOW}Text in yellow{RESET}")
  print(f"{BLUE}Text in blue{RESET}")
  print(f"{MAGENTA}Text in magenta{RESET}")
  print(f"{CYAN}Text in cyan{RESET}")
  print(f"{WHITE}Text in white{RESET}")
  print(f"{BOLD}Text in bold{RESET}")
  print(f"{UNDERLINE}Underlined text{RESET}")

  # Background colors
  print(f"{BG_RED}Red background with default text{RESET}")
  print(f"{BG_GREEN}Green background with default text{RESET}")
  print(f"{BG_BLUE}Blue background with default text{RESET}")

  # Use bright color
  print(f"{RED}{BOLD}{BG_WHITE}Bright red text with white background{RESET}")

if __name__ == "__main__":
  example()
