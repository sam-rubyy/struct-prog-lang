import re

patterns = [
    [r"\d*\.\d+|\d+\.\d*|\d+", "number"],
    [r"\+", "+"],
    [r".", "error"]
]

for pattern in patterns:
    pattern[0] = re.compile(pattern[0])

def tokenize(characters):
    tokens = []
    position = 0
    while position < len(characters):
        #Find first of
        for pattern, tag in patterns:
            match = pattern.match(characters, position)
            if match:
                break

        assert match
        if tag == "error":
            raise Exception(f"Syntax Error: Unrecognized/Unimplemented token:{[match.group(0)]}")
        
        token = {"tag":tag, "position":position}
        value = match.group(0)
        if token["tag"] == "number":
            if "." in value:
                token["value"] = float(value)
            else:
                token["value"] = int(value)
        tokens.append(token)
        position = match.end()
    tokens.append({"tag":None, "position":position})
    return tokens

def test_simple_tokens():
    print("test simple tokens")
    assert tokenize("+") == [
        {"tag":"+", "position":0},
        {"tag":None, "position":1}
        ]
    assert tokenize("3") == [
        {"tag":"number", "position":0, "value":3},
        {"tag":None, "position":1}\
        ]

if __name__ == "__main__":
    print("testing tokenizer")
    test_simple_tokens()
    print("done")