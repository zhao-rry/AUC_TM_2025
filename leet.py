import re

text = "this is a random samplE text so that i cAn try out different stuff with regex don't mInd mE plEase i dOn't really even know what i am doing i'm just bored and a little confusEd by regular exprEssions but they seem really cool"

# replace all "e" and "E" with "3"
print(re.sub(r"[e|E]", "3", text)) # or r"e" followed by re.I

# make a pattern that converts the entire text to leetspeak
def to_leet(text: str) -> str:
    leet_dict = {"a": "4", "e": "3", "i": "1", "o": "0", "t": "7", "s": "5"}
    pattern = re.compile(r"[aeiots]", re.I)
    return pattern.sub(lambda m: leet_dict[m.group(0).lower()], text)

print(to_leet(text))

''' --- not leet anymore, search proper nouns --- '''

text_cap = "Hi! My name is Will and I am from London. I currently study at British University College. Here, I am currently taking a course called Mine Texting along with my friends. For example, Grinch and Santa Claus are both in this course."

# define proper nouns as:
# group of words starting with capital letters, not directly proceeding a punctuation mark, and not the word "I"

# print(re.findall(r"([^\.\?!:] (([A-Z]\w+ )+))", text_cap))
# initial solution: fails to capture words ending with punctuation, also lots of unnecessary groupings -> instead, use ?: to avoid capturing and use * instead of +

print(re.findall(r"[^\.\?\!:] ([A-Z]\w+(?: [A-Z]\w+)*)", text_cap))