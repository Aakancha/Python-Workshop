#To count the vowel

def vowelcount(str1): 
   s = 0
   
   a="aeiouAEIOU"
   v = set(a) 

   for alpha in str1: 
      if alpha in v: 
         s = s + 1
   print("No. of vowels ::>", s) 
  
str1 = input("Enter the string for vowel count ::>") 
vowelcount(str1) 