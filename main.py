#from www.python-course.eu

#ENCRYPTER

letters = {
    'A':'X', 'B':'Y', 'C':'Z', 'D':'A',
    'E':'B', 'F':'C', 'G':'D', 'H':'E',
    'I':'E', 'J':'G', 'K':'H', 'L':'I',
    'M':'J', 'N':'K', 'O':'L', 'P':'M',
    'Q':'N', 'R':'O', 'S':'P', 'T':'Q',
    'U': 'R', 'V': 'S', 'W': 'T', 'X': 'U',
    'Y': 'V', 'Z': 'W',
    ' ':' ', '-':'-',
    } 

userString = input("Enter a sentence that needs to be encrypted with a Caesar cipher:\n")
userString = userString.upper() #transform to all caps
listLetters=list(userString) #get rid of hyphens and split into words
print(listLetters) #check on what's going on

listNew=[]
for item in listLetters:
    a=letters.get(item) #get values (digits) from dict
    listNew.append(a) #and create a new list with digits
print(listNew) #check on what's going on

while ("" in listNew): 
    listNew.remove("") #remove empty elements from list

print(*listNew,sep='') #print without white spaces


#--------------------------------------------
#DECRYPTER
letters = {
    'X':'A',
    'Y':'B',
    'Z':'C',
    'A':'D',
    'B':'E',
    'C':'F',
    'D':'G',
    'E':'H',
    'E':'I',
    'G':'J',
    'H':'K',
    'I':'L',
    'J':'M',
    'K':'N',
    'L':'O',
    'M':'P',
    'N':'Q',
    'O':'R',
    'P':'S',
    'Q':'T',
    'R':'U',
    'S':'V',
    'T':'W',
    'U':'X',
    'V':'Y',
    'W':'Z',
    ' ':' ',
    '-':'-',
    } 

userString = input("Enter a sentence that needs to be encrypted with a Caesar cipher:\n")
userString = userString.upper()
listLetters=list(userString)
#get rid of hyphens and split into words
print(listLetters) #check on what's going on

listNew=[]
for item in listLetters:
    a=letters.get(item) #get values (digits) from dict
    listNew.append(a) #and create a new list with digits
print(listNew) #check on what's going on

while ("" in listNew): 
    listNew.remove("") #remove empty elements from list
    
#print(*listDigits)
print(*listNew,sep='') #print without white spaces
