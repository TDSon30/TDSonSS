# Python function to automatically create data.yaml config file
# 1. Reads "classes.txt" file to get list of class names
# 2. Creates data dictionary with correct paths to folders, number of classes, and names of classes
# 3. Writes data in YAML format to data.yaml

import yaml
import os

def create_data_yaml(path_to_classes_txt, path_to_data_yaml):
    # Read class.txt to get class names
    if not os.path.exists(path_to_classes_txt):
        print(f'classes.txt file not found! Please create a classes.txt labelmap and move it to {path_to_classes_txt}')
        return

    classes = []
    with open(path_to_classes_txt, 'r') as f:
        for line in f.readlines():
            if len(line.strip()) == 0:
                continue
            classes.append(line.strip())

    number_of_classes = len(classes)

    # Create data dictionary
    data = {
        'path': '/content/YOLO/data',
        'train': 'train/images',
        'val': 'validation/images',
        'nc': number_of_classes,
        'names': classes
    }

    # Write data dictionary to data.yaml
    with open(path_to_data_yaml, 'w') as f:
        yaml.dump(data, f)

    print(f'data.yaml file created successfully at {path_to_data_yaml}')
    return


# Define path to classes.txt and run function
path_to_classes_txt = '/content/YOLO/custom_data/classes.txt'
path_to_data_yaml = '/content/YOLO/data.yaml'
create_data_yaml(path_to_classes_txt, path_to_data_yaml)

with open('/content/YOLO/data.yaml', 'r') as f:
    data = yaml.safe_load(f)

print(data)
