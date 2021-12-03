def substringmatch(init, substring):
    # Runtime: O(n**2)/ Space: O(n)
    n = len(init)
    k = len(substring)
    for i in range(n-k):
        for j in range(k):
            if init[i] == substring[j]:
                if init[i:i+k] == substring[:]:
                    print(f'{substring} is in {init}')    
                    return
            else:
                i += 1
    print('no match')
    return
init = 'abcdef'
substring = 'A'
print(substringmatch(init, substring))