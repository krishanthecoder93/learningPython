word1 = input("Enter a word to check : ")
word2  =input("Enter other word to check: ")

if len(word1)!=len(word2):
    print("Not Anagram")
else:
    count = {}
    for ch in word1:
        count[ch] = count.get(ch,0)+1
    for ch in word2:
        if ch not in count:
            print("Not Anagram")
            break
        count[ch]-=1
    else:
        if all(v==0 for v in count.values()):
            print("Anagram")
        else:
            print("Not Anagram")

