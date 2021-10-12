a = [1,1,2,2,3,4,4,5,5]

def lonelyinteger(a):
    # Write your code here
    for integer in a:
        if(a.count(integer) == 1):
            return integer

print(lonelyinteger(a))