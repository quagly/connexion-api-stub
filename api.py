# `api.py` file contents
import re

def string_length(body):
    return {"length": len(body)}, 200

def string_info(body, include_whitespace):
    if include_whitespace:
        None
    else:
        body = re.sub(r"\s+", "", body)
    return {
                "length": len(body),
                "include_whitespace": include_whitespace,
                "body": body
           }, 200

def get_dict():
    ret_dict = {
        "home": 0.0037428185399140637,
        "government": 0.002829530081728651
        }
    return ret_dict, 200
