import requests

from openxlab.xlab.handler.user_token import get_jwt
import json


class ModelApiClient(object):
    def __init__(self, endpoint, token):
        self.token = token
        self.endpoint = endpoint

    def get_inference_result(self, payload):
        """
        get inference result
        """
        result = self.http_post_response_dto(payload)
        print(f'result:{result}')
        result = Result(result)
        return result

    def http_post_response_dto(self, payload):
        headers = self.http_common_header()
        response = requests.post(self.endpoint, files=payload["files"], data={'texts': payload['texts']},
                                 headers=headers)
        response.raise_for_status()
        return response.content

    def http_common_header(self):
        try:
            jwt = get_jwt()
        except ValueError as e:
            print(f"warning: {e}")
            return
        header_dict = {
            "Authorization": jwt
        }
        return header_dict


class Result(object):
    def __init__(self, original):
        self.original = original

    def tojson(self):
        return json.loads(self.original)

    @property
    def predictions(self):
        data = json.loads(self.original)
        if type(data) == dict:
            return data['predictions']
        else:
            for item in data:
                if 'visualization' in item:
                    del item['visualization']
        return data

    @property
    def visualization(self):
        data = json.loads(self.original)
        if type(data) == dict:
            return data['visualization']
        else:
            visualization_list = [item["visualization"] for item in data]
            return visualization_list
