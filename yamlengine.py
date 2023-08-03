# testing space for reading nad displaying yaml files
# Aug 2, 2023 20:05
import yaml
from yaml.loader import SafeLoader
"""
# Open the file and load the file
with open("entries/entry.yml") as f:
    data = yaml.load(f, Loader=SafeLoader)
    print(data)
"""

data = {
  "rate": '4',
  "date": '08.02.2023',
  'sig': 'Yours truly',
  'desc': 'Today went stunningly'
}

#Saves a dict "data" into a .yml

def saveEntry(data):
    date = data['date']
    f = open(f"entries/{date}.yml", "a")
    f.write(yaml.dump(data))
    f.close()

saveEntry(data)
