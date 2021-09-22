def fizzBuzz(n):
    dict = {3:"Fizz", 5:"Buzz"}
    ans = []
    
    for i in range(1, n+1):
        s=""
        
        for key in dict.keys():
            if i % key == 0:
                s += dict[key]
                
        if not s:
            s = str(i)
                
        ans.append(s)
        
    return ans
