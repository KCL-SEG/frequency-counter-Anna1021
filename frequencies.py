"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for item in items:
        key = str(item)

        if key not in frequencies:
            frequencies[key] = 1
        else:
            frequencies[key] += 1

    return frequencies


testResult1 = frequencies([100, "hello", "100", "100", "hello"])
testResult2 = frequencies([200, "Hello", "200", "200", "hello"])
print(testResult1)
print(testResult2)

