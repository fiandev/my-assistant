import os
from dotenv import dotenv_values, load_dotenv

load_dotenv()

environment = {
    **os.environ,
    **dotenv_values(".env")
}