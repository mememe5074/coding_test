def index_reverse(i, j, ex_list):
    tmp = ex_list[i:j]
    tmp.reverse()
    tmp.extend(ex_list[j:])
    tmp2 = ex_list[:i]
    tmp2.extend(tmp)
    return tmp2

test = [3,4,1,2]
index_reverse(1,3,test)