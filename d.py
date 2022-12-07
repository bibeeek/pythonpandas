def sq(x): # 0 1 2 3 4 5 6 ..9
    if x>0:
        return x
positives = filter(sq,[1,-5,0,6,-2,8])
print(list(positives))
