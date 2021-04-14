# Count Charecters
# Given a string . Find the fequency of each charecter in that


def freq_count(inp):
    ret_dict = {}
#   for char in set(inp):
#       ret_dict[char] = inp.count(char)

    for char in inp:
        if char in ret_dict:
            ret_dict[char] += 1
        else:
            ret_dict[char] = 1
        
        
    return ret_dict

if __name__ == "__main__":
    inp_list = ["one","two","aabbcc","abcabc","abacbacbds"]
    for inp in inp_list:
        print("Freq count for {0} is {1}".format(inp,freq_count(inp)))
