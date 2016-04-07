import configparser
import os


def create_config(path):
    # Create a default config file
    config = configparser.ConfigParser(allow_no_value=True)
    config.add_section("Type")
    config.set("Type", "# You can use 3 types: pickle, json, yml. (Default - pickle)")
    config.set("Type", "file_type", "pickle")

    with open(path, "w") as config_file:
        config.write(config_file)


def get_type():
    if not os.path.exists('GlobalConfigs.conf'):
        create_config('GlobalConfigs.conf')

    config = configparser.ConfigParser()
    config.read('GlobalConfigs.conf')

    return config.get("Type", "file_type")
