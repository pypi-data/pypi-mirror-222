import re
from typing import Dict


class DataType:
    INTEGER = "integer"
    NUMBER = "number"
    STRING = "string"
    BOOLEAN = "boolean"
    ARRAY = "array"
    OBJECT = "object"
    ONE_OF = "oneOf"
    ANY_OF = "anyOf"


def class_name_titled(input_str: str) -> str:
    """
    Make the input string suitable for a class name
    """
    # Capitalize the first letter always
    input_str = input_str[:1].title() + input_str[1:]
    for badstr in [".", "-", "_", ">", "<", "/"]:
        input_str = input_str.replace(badstr, " ")
    if " " in input_str:
        # Capitalize all the spaces
        input_str = input_str.title()
    input_str = input_str.replace(" ", "")
    return input_str


def clean_prop(input_str: str) -> str:
    """
    Clean a property to not have invalid characters
    """
    for dropchar in [">", "<"]:
        input_str = input_str.replace(dropchar, "")
    for badstr in ["-", "."]:
        input_str = input_str.replace(badstr, "_")
    reserved_words = ["from"]
    if input_str in reserved_words:
        input_str = input_str + "_"
    return input_str


def _split_upper(s):
    res = re.findall(".[^A-Z]*", s)
    if len(res) > 1:
        return "_".join(res)
    return res[0]


def _snake_case(s):
    for badchar in ["/", "-", "."]:
        s = s.replace(badchar, "_")
    s = _split_upper(s)
    if s[0] == "_":
        s = s[1:]
    return s.lower()


def get_func_name(operation: Dict, path: str) -> str:
    if operation.get("operationId"):
        return _snake_case(operation["operationId"].split("__")[0])
    return _snake_case(path)


def get_type(t):
    t_type = t.get("type")
    if t_type == DataType.STRING:
        return "str"
    if t_type in [DataType.INTEGER, DataType.NUMBER]:
        return "int"
    if t_type == DataType.BOOLEAN:
        return "bool"
    if t_type == DataType.OBJECT:
        return "typing.Dict[str, typing.Any]"
    if t_type == DataType.ARRAY:
        return "typing.List[typing.Any]"
    if ref := t.get("$ref"):
        return f'"{class_name_titled(ref.replace("#/components/schemas/", ""))}"'
    if t_type is None:
        # In this case, make it an "Any"
        return "typing.Any"
    return t_type
