import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import datetime
import psutil
import platform
from modules.colors import BOLD, BLUE, RESET
from modules.icons import icons



def neofetch():
    uname = platform.uname()
    system = uname.system
    distro = ""
    version = ""
    
    if system == "Linux":
      try:
        with open("/etc/os-release") as f:
          for line in f:
            if line.startswith("NAME="):
              distro = line.split("=")[1].strip().strip('"')
            elif line.startswith("VERSION="):
              version = line.split("=")[1].strip().strip('"')
      except FileNotFoundError:
        distro = "Linux"
    
    logo = icons.get(distro if distro else system, ["Unknown OS"])
    
    def siSystem():
      if system == 'Windows':
        return f"{BLUE}{system}{RESET}"
      else:
        return f"{system} ({distro})" if distro else f"{system}"
    
    # Calcular el uptime en un formato legible
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.datetime.fromtimestamp(boot_time_timestamp)
    uptime = datetime.datetime.now() - bt
    days, seconds = uptime.days, uptime.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    readable_uptime = f"{days} days, {hours} hours, {minutes} mins" if days > 0 else f"{hours} hours, {minutes} mins"
    
    info = [
      f"{BOLD}User:{RESET} {psutil.users()[0].name}",
      f"{BOLD}System:{RESET} {siSystem()}",
      f"{BOLD}Node Name:{RESET} {uname.node}",
      f"{BOLD}Release:{RESET} {uname.release}",
      f"{BOLD}Version:{RESET} {uname.version}",
      f"{BOLD}Machine:{RESET} {uname.machine}",
      f"{BOLD}Processor:{RESET} {uname.processor}",
      f"{BOLD}RAM:{RESET} {round(psutil.virtual_memory().total / (1024.0 **3))} GB",
      f"{BOLD}OS:{RESET} {distro} {version} on {system} {uname.machine}",
      f"{BOLD}Kernel:{RESET} {uname.release}",
      f"{BOLD}Uptime:{RESET} {readable_uptime}",
      f"{BOLD}Packages:{RESET} {len(psutil.pids())} (dpkg)",
      f"{BOLD}Shell:{RESET} {psutil.Process().name()}",
      f"{BOLD}CPU Usage:{RESET} {psutil.cpu_percent()}%",
      f"{BOLD}Memory Usage:{RESET} {psutil.virtual_memory().percent}%",
    ]
    
    # Definir la distancia fija arriba y abajo
    fixed_padding = 3
    empty_line = " " * 0
    
    # Agregar líneas vacías arriba y abajo
    logo = [empty_line] * fixed_padding + logo + [empty_line] * fixed_padding
    info = [empty_line] * fixed_padding + info + [empty_line] * fixed_padding
    
    max_lines = max(len(logo), len(info))
    for i in range(max_lines):
      logo_line = logo[i] if i < len(logo) else ""
      info_line = info[i] if i < len(info) else ""
      print(f"{logo_line:<35} {info_line}")



if __name__ == "__main__":
  neofetch()
