import re

def are_anagrams(str1, str2):
    """
    Creating this function to check if two strings are anagrams.
    It also ignores case, spaces, and punctuation.
    """
    # Normalizing both strings and converting them to lowercase
    # also removing all non-alphanumeric characters (spaces, punctuation)
    str1_cleaned = re.sub(r'[^a-z0-9]', '', str1.lower())
    str2_cleaned = re.sub(r'[^a-z0-9]', '', str2.lower())
    
    # now checking if sorted characters in both cleaned strings are equal
    return sorted(str1_cleaned) == sorted(str2_cleaned)

# Test cases
print(are_anagrams("Listen", "Silent"))          
print(are_anagrams("A gentleman", "Elegant man"))
print(are_anagrams("Clint Eastwood", "Old West Action")) 
print(are_anagrams("dad", "ad*d"))
print(are_anagrams("madman", "dadman"))
print(are_anagrams("Dormitory", "Dirty room"))   
print(are_anagrams("The eyes", "They see"))      
print(are_anagrams("Python", "Java"))            
