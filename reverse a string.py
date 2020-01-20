def reverse(string): 
    string = "".join(reversed(string)) 
    return string 
  
s = input("enter a String\n")
  
print ("The original string  is : ",end="") 
print (s) 
  
print ("The reversed string(using reversed) is : ",end="") 
print (reverse(s)) 
