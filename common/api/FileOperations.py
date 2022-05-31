import json


class FileOperations:

    def __int__(self):
        pass

    def read_file_as_json_readonly(self, file_path):
        file = open(file_path, 'r')
        json_input = file.read()
        return json.loads(json_input)