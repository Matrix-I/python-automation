#!/usr/bin/python3
import json
import yaml


def sort_dict_keys(d):
    if isinstance(d, dict):
        return {k: sort_dict_keys(v) for k, v in sorted(d.items())}
    elif isinstance(d, list):
        return [sort_dict_keys(v) for v in d]
    else:
        return d


def sort_objects_by_field(array, field):
    return sorted(array, key=lambda x: x[field])


# Function to read YAML data from a file
def read_yaml(path):
    with open(path, 'r') as file:
        data = yaml.safe_load(file)
    return data


# Function to write YAML data to a file
def write_yaml(data, path):
    with open(path, 'w') as path:
        yaml.dump(data, path, default_flow_style=False, sort_keys=False)


def represent_str(dumper, data):
    # Wrap string values in double quotes
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='')


# Path to the YAML file
filePath = 'files/sample.yaml'

# Open the YAML file and load its contents
yaml.add_representer(str, represent_str)
yamlData = read_yaml(filePath)

# print(json.dumps(yamlData, indent=2))

pathSorted = sort_dict_keys(yamlData['paths'])
schemasSorted = sort_dict_keys(yamlData['components']['schemas'])
# requestBodiesSorted = sort_dict_keys(yamlData['components']['requestBodies'])
# responsesSorted = sort_dict_keys(yamlData['components']['responses'])


yamlData['paths'] = pathSorted
yamlData['components']['schemas'] = schemasSorted
# yamlData['components']['requestBodies'] = requestBodiesSorted
# yamlData['components']['responses'] = responsesSorted


# # Sorted oneOf value YAML. If use for another file let's comment it.
# operativeData = yamlData['components']['schemas']['OperativeData']['oneOf']
# operativeDataSorted = sort_objects_by_field(operativeData, '$ref')
# # print(json.dumps(operativeDataSorted, indent=2))
# yamlData['components']['schemas']['OperativeData']['oneOf'] = operativeDataSorted


# Path to the YAML result file
filePathOutput = 'files/result.yaml'
# Write YAML data to a file without sorting keys
write_yaml(yamlData, filePathOutput)
