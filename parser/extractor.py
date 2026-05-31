import re


def extract_number(pattern: str, text: str):

    match = re.search(pattern, text)

    if match:
        return float(match.group(1))

    return None