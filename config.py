import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Define a function to retrieve the value of a variable
def get_config_value(variable_name: str):
    return os.environ.get(variable_name)