from dotenv import find_dotenv
from configparser import ConfigParser


def read_credentials(file="cred.cfg", verbose=False):
    """Read credentials from a file and return a dictionary with the credentials. By default it reads from 'cred.cfg' file. If the file is not found in the current directory, it will look in the parent directory and so on until it finds the file.

    File must follow the windows .ini format (https://en.wikipedia.org/wiki/INI_file):

    [salesforce_id]
    username = username
    password = password
    security_token = security_token

    [sql_server]
    username = username
    password = password
    server = server
    port = port

    Parameters
    ----------
    file = 'cred.cfg' (str): Name of the file with the credentials. By default cred.cfg.
    verbose = False (bool): If True, it prints the path of the file where the credentials were loaded from.

    Returns
    -------
    credentials (dict): Dictionary with the credentials.
    """

    credentials = ConfigParser(interpolation=None)
    credentials.read(find_dotenv(file))
    if verbose:
        print("Credentials loaded from:", find_dotenv(file))

    return credentials
