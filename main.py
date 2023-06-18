def strcounter(s):
    for syn in set(s):
        count = 0
        for sub_syn in s:
            if syn == sub_syn:
                count +=1
        print(syn, count)

strcounter('fckjreee')

