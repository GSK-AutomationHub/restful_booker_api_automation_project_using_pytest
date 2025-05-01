import json
import os
from configparser import ConfigParser
from dotenv import load_dotenv

""" this utility consist function to read from config, env etc property files """

class PropReader:

    @staticmethod
    def read_config_file(category, key):
        config = ConfigParser()
        config.read(".\\src\\config\\config.ini")
        return config.get(category, key)


    @staticmethod
    def read_env_file():
        credentials = {}
        load_dotenv(".\\src\\config\\.env")
        credentials.update({
            'username': f"{os.getenv("AUTH_USERNAME")}",
            'password': f"{os.getenv("AUTH_PASSWORD")}"
        })
        return credentials


    @staticmethod
    def read_json_file(filename):
        with open(f".\\src\\resources\\{filename}", 'r') as file:
            return json.load(file)


    @staticmethod
    def read_csv_file(self):
        pass



