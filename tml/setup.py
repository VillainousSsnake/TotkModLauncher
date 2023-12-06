# TotkModLauncher/tml/setup.py
# Currently installs pip dependencies

import subprocess
import sys


print("Installing dependencies")


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


for pk in ["SarcLib", "sarc", "zstandard", "rstb"]:
    install(pk)


print("Finished Installing Dependencies\nRun main.py to use the app!")