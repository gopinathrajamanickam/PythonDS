# Recursive Binary Search

def rec_bin_search(inp_list,target, first, last):
    # base case
    # After searching Entire list if the target is not found return Not Found
    if first > last:
        return "Not Found"
    # recursive case
    else:
        mid = ( first + last ) // 2
        if inp_list[mid] == target:
            return mid
    # call recursive function that progresses towards base case 
        elif target < inp_list[mid]:
            return rec_bin_search(inp_list, target, first, mid-1)
        else:
            return rec_bin_search(inp_list, target, mid+1,last)

if __name__ == "__main__":
    list_ = [1,2,3,45,232,1223]
    tar = 4
    print("{0} is found in pos {1}".format(tar,rec_bin_search(list_,tar,0,len(list_)-1)))

        

