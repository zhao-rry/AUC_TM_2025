import re

text = "this is a random samplE text so that i can try out different stuff with regex don't mind mE plEase i don't really even know what i am doing i'm just bored and a little confusEd by regular exprEssions but they seem really cool"

# replace all "e" and "E" with "3"
print(re.sub(r"[e|E]", "3", text)) # or r"e" followed by re.I

# make a pattern that converts the entire text to leetspeak
def to_leet(text: str) -> str:
    leet_dict = {"a": "4", "e": "3", "o": "0", "t": "7", "s": "5"}
    pattern = re.compile(r"[aeots]")
    return pattern.sub(lambda m: leet_dict[m.group(0)], text)

print(to_leet(text))