# borrow the bots and test data from test_injection.py
from test_injection import ask_plain, ask_sandwich, documents, question

# documents[1] is the polite attack
# print what each bot actually says, 3 times each
for i in range(3):
    print("PLAIN:", ask_plain(documents[1], question))
    print("SANDWICH:", ask_sandwich(documents[1], question))
    print()
