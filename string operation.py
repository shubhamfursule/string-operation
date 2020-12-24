import string
Sentence = "Data Science is one of the bEst course 90 "
count =0
consonants =0
words = len(list(Sentence.split(" ")))
upper = 0
sentence = 0
blank =0 
number = 0
def length_string(sent):
    length_of_string = 0
    while Sentence[length_of_string:]:        
        length_of_string += 1
    return length_of_string
lengths = length_string(Sentence)
print(f"Total length of string :{lengths}")


for i in range(length_string(Sentence)):    
    if Sentence[i] in "aeiou":
        count+=1
    else:
        consonants+=1
    if " " == Sentence[i]:
        blank +=1
    if Sentence[i] in "0123456789":
        number +=1
    if Sentence[i].isupper():
        upper+=1
print(f"Total number of Vovels are :{count}")
print(f"Total number of consonants are :{consonants}")
print(f"Total number of Blanks :{blank}")
print(f"Total number of words are :{words}")
print(f"Total number of digits : {number}")
print(f"Total number of upper cases :{upper}")
print(f"Total length of string :{lengths}")