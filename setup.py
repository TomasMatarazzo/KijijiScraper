""" This is the Starting Point of Kijiji Web Scraping Script Environment Setup """

import sys
import os

""" Getting Basic Logging Options """


class SetupEnvironment:

    def installAndUnpgradeLibraries(self):
        try:
            print('hi')
            # Upgrading Pip Version
            pip_install_stream = os.popen('python -m pip install --upgrade pip')

            # Selenium Installation
            selenium_install_stream = os.popen('pip install selenium')

            # Requests Installation
            requests_install_stream = os.popen('pip install requests')

            flask_install_stream = os.popen('pip install flask')

            pandas_install_stream = os.popen('pip install pandas')

            flaskweb_install_stream = os.popen('pip install flaskwebgui')

            # Same libraries but in pip3.

            selenium_install_stream = os.popen('pip3 install selenium')

            requests_install_stream = os.popen('pip3 install requests')

            flask_install_stream = os.popen('pip3 install flask')

            pandas_install_stream = os.popen('pip3 install pandas')

            flaskweb_install_stream = os.popen('pip3 install flaskwebgui')


        except Exception:
            print("Setup Module : Environment could not be setup due to System Error")
            print(
                "Setup Module : Please provide required privileges to run the Script Or Contact System Administrator")
            sys.exit()


# Checking Python Version
python_major_version = sys.version_info.major
if python_major_version < 3:
    print("Please upgrade your python version to Python 3.")
else:
    # Staring Environment Setup
    setupEnvironment = SetupEnvironment()
    setupEnvironment.installAndUnpgradeLibraries()
