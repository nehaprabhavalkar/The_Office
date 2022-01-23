import yaml

def load_yaml_data():
    with open('../conf/config.yml', 'r') as file:
        data = yaml.safe_load(file)
    return data