import asyncio
import json
import os

from HW_32.lambda_service import LambdaTestService
from HW_32.utils import read_data_file

lambda_test_service = LambdaTestService()


async def convert_json_to_xml(file_name: str, future: asyncio.Future):
    input_json = read_data_file(os.path.join("json", f"{file_name}.json"))
    result = await lambda_test_service.convert_json_to_xml(input_json)
    future.set_result(result)


async def convert_json_to_yaml(file_name: str, future: asyncio.Future):
    input_json = read_data_file(os.path.join("json", f"{file_name}.json"))
    result = await lambda_test_service.convert_json_to_yaml(input_json)
    future.set_result(result)


async def extract_text_from_json(file_name: str) -> str:
    input_json = read_data_file(os.path.join("json", f"{file_name}.json"))
    result = await lambda_test_service.extract_text_from_json(input_json)
    return result


async def convert_yaml_to_json(future: asyncio.Future) -> str:
    result_yaml = await future
    result = await lambda_test_service.convert_yaml_to_json(result_yaml)
    return result


async def convert_xml_to_yaml(future: asyncio.Future):
    result_xml = await future
    result = await lambda_test_service.convert_xml_to_yaml(result_xml)
    return result


async def write_content_to_file(file_name: str, content: str) -> None:
    with open(file_name, "w", encoding="utf8") as file:
        if isinstance(content, dict):
            content_str = json.dumps(content, indent=2)
        else:
            content_str = str(content)

        file.write(content_str)


async def main():
    future_xml = asyncio.Future()
    future_yaml = asyncio.Future()

    await asyncio.create_task(convert_json_to_xml("1", future=future_xml))
    content_yaml = await asyncio.create_task(convert_xml_to_yaml(future=future_xml))

    await asyncio.create_task(convert_json_to_yaml("1", future=future_yaml))
    content_json = await asyncio.create_task(convert_yaml_to_json(future=future_yaml))

    content_text = await asyncio.create_task(extract_text_from_json("1"))

    await write_content_to_file("converted.yaml", content_yaml)
    await write_content_to_file("converted.json", content_json)
    await write_content_to_file("converted.txt", content_text)


if __name__ == '__main__':
    asyncio.run(main())
