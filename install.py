import platform
import os

# Currently only Linux is supported
# TODO Add Windows and MacOS support
if platform.system() == 'Linux':
    config_path = os.path.join(' ', 'home', os.getlogin(), '.terminoter')
    if not os.path.exists(home_path):
        os.mkdir(config_path)
    else:
        print("Seems like you already have terminoter installed.")
