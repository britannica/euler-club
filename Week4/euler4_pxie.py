def isPalindrome(word):
    word =str(word)
    return word == word[::-1]



def largestPalindrome():
    result = [];
    for x in range(1000):
        for y in range(1000):
            if isPalindrome((999-x)*(999-y)):
                result.append( (999-x)*(999-y))
    return max(result)
      
     
