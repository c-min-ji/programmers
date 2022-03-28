def solution(n, arr1, arr2):
    answer = []
    bin_arr1 = []
    bin_arr2 = []
    for i in range(n):
        a = bin(arr1[i]).replace("0b","")
        b = bin(arr2[i]).replace("0b","")
        if len(a)<n:
            a = ("0"*(n-len(a))+a)
        if len(b)<n:
            b = ("0"*(n-len(b))+b)
        bin_arr1.append(a)
        bin_arr2.append(b)
    x = []
    for b in range(len(bin_arr1)):
        c = ''
        for i in range(len(bin_arr1)):
            if bin_arr1[b][i] == "1" or bin_arr2[b][i]=="1":
                c+="#"
            else:
                c+=" "
        x.append(c)
    
    return x
