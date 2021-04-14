# Validate Anagram

# given two strings as input Check if they can be considered anagrams
# i.e the letters in those stringss to be rearranged to form the other

def isAnagram(str1,str2):
    # if the letter freq count is same for given strings it can be called anagrams
    result = 'Not Anagrams'
    freq_dict = {}
    s1 = set(str1)
    s2 = set(str2)
    if len(str1) == len(str2) and len(s1) == len(s2):
        for char in s1:
            freq_dict[char] = str1.count(char)
        for char in s2:
            if char in s1 and freq_dict[char] == str2.count(char):
                result = 'Anagrams'
            else:
                result = 'Not Anagrams'
                break
    return result

if __name__ == "__main__":
    inp_list = [('a','a'),('abb','baa'),('abc','cbwa'),('s','a')]
    for inp in inp_list:
        # print(inp[0])
        print(" {0}  and  {1} are {2}.".format(inp[0], inp[1] , isAnagram(inp[0],inp[1])))
