# from flask import Flask, request, jsonify
#
# app = Flask(__name__)
#
# # Sample data
# data = { 'hello': 'hello world!'}
#
#
# # GET API
# @app.route('/api/data', methods=['GET'])
# def get_data():
#     return jsonify(data)
#
#
# # POST API
# @app.route('/api/data', methods=['POST'])
# def post_data():
#     new_data = request.json
#     data.update(new_data)
#     return jsonify({'message': 'Data created successfully'})
#
#
# # PUT API
# @app.route('/api/data/<key>', methods=['PUT'])
# def put_data(key):
#     updated_data = request.json
#     if key in data:
#         data[key] = updated_data
#         return jsonify({'message': f'Data with key {key} updated successfully'})
#     else:
#         return jsonify({'error': f'Data with key {key} not found'}), 404
#
#
# if __name__ == '__main__':
#     app.run(host='localhost', port=8080)

# import requests
# import json
#
# cookies = {'SESSIONID': '0b256366-404a-4454-a551-6097ea8e6857'}
#
# response = requests.get(
#     'https://www.test.com'
#     , cookies=cookies
# )
#
# # print(json.loads(response.text))
#
# print(json.dumps(json.loads(response.text), indent=4))

import yaml

random_condition = """
    - type: value
      key: some_id
      value:
        - '04549'
        - '24543'
"""


class CustomDumper(yaml.Dumper):
    def represent_data(self, data):
        if isinstance(data, str) and data.isdigit():
            return self.represent_scalar('tag:yaml.org,2002:str', data, style="'")

        return super(CustomDumper, self).represent_data(data)


names = yaml.safe_load(random_condition)

# names = yaml.safe_load(random_condition)
with open('names.yml', 'w') as file:
    yaml.dump(names, file, Dumper=CustomDumper, sort_keys=False, default_flow_style=False)
print(open('names.yml').read())
