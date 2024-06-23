import json
import requests


class LambdaTestService:
    BASE_URL = "https://test-backend.lambdatest.com/api/dev-tools/"

    async def _send_request(self, path, input_key, input_str):
        url = self.BASE_URL + path
        response = requests.post(url, data={input_key: input_str})
        return response

    async def convert_json_to_xml(self, input_str: str) -> str:
        response = await self._send_request("json-to-xml", "input-str", input_str)
        return response.text

    async def convert_json_to_yaml(self, input_str: str) -> str:
        response = await self._send_request("json-to-yaml", "json-str", input_str)
        return response.json()["data"]

    async def extract_text_from_json(self, input_str: str) -> str:
        response = await self._send_request("extract-text-json", "input-str", input_str)
        return response.json()["data"]

    async def convert_yaml_to_json(self, input_str: str) -> str:
        response = await self._send_request("yaml-to-json", "yaml-str", input_str)
        return response.json()["data"]

    async def convert_xml_to_yaml(self, input_str: str) -> str:
        response = await self._send_request("xml-to-yaml", "xml-str", input_str)
        return response.json()["data"]
