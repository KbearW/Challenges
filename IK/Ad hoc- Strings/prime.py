def prime(v):
    res = []
    # the num list should starts from 2 b/c 0, 1 are not prime!
    # mod is looking at the remainder!
    for i in range(2, v+1):
        for j in range(2, i):
        # for/else loop is need here to catch all things that fail
            if(i % j == 0):
                # Note: prime can only be div by 1 and itself, 
                # so if the remainder is 0 for any division, 
                # it's not a prime--> break
                break
        else:
            res.append(i)
        #     # break
        #     # print(i, j)
            # print(f'this is a prime {i}')
            # break
    return res
print(prime(30))