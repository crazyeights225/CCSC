#Generating all possible shifts of word
#DEC 2016
#Written for CryptoChallenge: Ceasar's Cypher
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def shiftLeft(l,n):
    return l[n:] + l[:n]

def shiftRight(l,n):
    return l[n:]+l[:n]

def getWord(index):
    word=""
    for i in index:
        for a in range(0, len(alphabet)):
            if(i==a):
                word+=""+alphabet[a]
    return word


word=raw_input("Enter a word: ")
#letters=[]
index=[]
for x in word:
    x=x.lower()
    #letters.append(x)
    for y in range(0,len(alphabet)):
        if(x==alphabet[y]):
            index.append(y)

def  shifting(n, index):       
    newIndex=[]           
    for x in index:
        for y in range(0, len(alphabet)):
            if(x+n>=26):
                j=(x+n)-26
                if(alphabet[j]==shiftLeft(alphabet, n)[y]):
                    newIndex.append(j)
            if(x+n<26):
                if(alphabet[x+n]==shiftLeft(alphabet, n)[y]):
                    newIndex.append(x+n)
            
    print getWord(newIndex)                
            

for a in range(0, len(alphabet)):   
    shifting(a, index)
    
print getWord(index)    
#print letters
print index

