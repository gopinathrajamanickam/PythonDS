# Sequential search

def seq_search(list_, n):
    pos = -1
    for i in range(0,len(list_)-1):
        if list_[i] == n:
            pos = i + 1
            break
        
    return pos

if __name__ == "__main__":
    inp_lists = [[10,32,3,212,333],[2,3,4212,423,2132]]
    n = 3
    for inp in inp_lists:
        print("Given number {0} is present in list {1} at position {2}"
              .format(n,inp,seq_search(inp,n)))
    
