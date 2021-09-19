# https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

def minimumBribes(q):
    # Write your code here
    count = 0
    for i in range(len(q)):    
        # print(q[i], i+1, q[i] - (i+1))
        if q[i] - (i+1) > 2:
            print('Too chaotic')
            return  #this return is needed to provent keep looping over to the next print
        if q[i] - (i+1) > 0: 
            if q[i] - (i+1) == 1 or q[i] - (i+1) == 2:  
                count += q[i] - (i +1)
    print(count) 

minimumBribes([1,2,5,3,7,8,6,4])


# This soluation is off by one.... 