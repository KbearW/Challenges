'''Quick sort- best runtime: O(nlog n)
worse runtime: O(n**2)
average runtime: O(nlog n)

first sort the initial array by finding the median...
in the case that we can't figure out how to find the median and just pick the first elemt as the midpoint
runtime will become the worse case bc if the list is already sorted, then one side of the sort will have 
zero elemt and the other side will have all the elemt'''