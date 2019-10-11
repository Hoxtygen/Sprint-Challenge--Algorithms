'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    wordLen = len(word)
    if wordLen == 0 or wordLen < 2:
        return 0
    elif word[0:2] == "th":
        return count_th(word[1:]) + 1
    else:
        return count_th(word[1:])


print(count_th("testhtesth"))