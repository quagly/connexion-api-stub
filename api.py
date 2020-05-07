# `api.py` file contents
import re

def string_length(body):
    return {"length": len(body)}, 200

def string_info(body, include_whitespace=True):
    if include_whitespace:
        None
    else:
        body = re.sub(r"\s+", "", body)
    return {
                "length": len(body),
                "include_whitespace": include_whitespace,
                "body": body
           }, 200
