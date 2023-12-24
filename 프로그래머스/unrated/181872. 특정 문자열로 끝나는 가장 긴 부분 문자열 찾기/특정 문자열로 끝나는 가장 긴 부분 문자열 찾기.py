def solution(myString, pat):
    for i in range(len(myString)):
        if pat in myString[len(myString)  - i - len(pat):len(myString) - i]:
            return myString[:len(myString) - i]
