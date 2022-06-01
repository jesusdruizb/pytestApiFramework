import json
import jsonpath


class JsonOperations:

    def __int__(self):
        pass

    def search_response_by_jsonpath(self, response, json_path):
        return jsonpath.jsonpath(self.transform_response_to_json(response), json_path)

    def transform_response_to_json(self, request_response):
        return json.loads(request_response.text)
