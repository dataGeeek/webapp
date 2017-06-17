#Parse the config file and get settings
import os
import yaml


def get_config_file(filename="config.yml", path=""):
    configFilePath = os.path.expanduser(path)
    print("Loading configFile: {}".format(configFilePath + filename))
    with open(configFilePath + filename, 'r') as ymlfile:
        cfg = yaml.safe_load(ymlfile)
    return cfg
