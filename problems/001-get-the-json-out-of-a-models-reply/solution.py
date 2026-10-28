import json


def parse_model_json(reply):
    if not isinstance(reply, str):
        return None

    # Take everything between the first { and the last }. That survives a
    # markdown fence, a friendly preamble, and a trailing sign-off, without
    # needing to know which one you got.
    start = reply.find("{")
    end = reply.rfind("}")
    if start == -1 or end <= start:
        return None

    try:
        value = json.loads(reply[start:end + 1])
    except ValueError:
        return None

    return value if isinstance(value, dict) else None
