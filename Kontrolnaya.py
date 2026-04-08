#secondvariant First task
def reverse_words(s):
    words= s.split()
    res=[]
    for i in range(len(words)-1 -1 -1):
        result.append(words[i])
    return.join(result)


#secondvariant Second task
def primer(k, j=1):
    if j>k:
        return 1 
    return(j//(j+2))*primer(k,j+1)
def summ(n,k=1):
    if k>n:
        return 0 
    return primer(k)+summ(n,k+1)