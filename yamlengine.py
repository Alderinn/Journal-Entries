# testing space for reading nad displaying yaml files
# Aug 2, 2023 20:05
import yaml
from yaml.loader import SafeLoader
# Open the file and load the file
with open("entry.yml") as f:
    data = yaml.load(f, Loader=SafeLoader)
    print(data)