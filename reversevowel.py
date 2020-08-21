def convert(string):
    string=list(string)
    vowel=[]
    for ch in string:
        if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I'
     or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
            vowel.append(ch)
    
    for ch in range(0,len(string)):   
        if(string[ch]=='A' or string[ch]=='a' or string[ch]=='E' or string[ch] =='e' or string[ch]=='I'
     or string[ch]=='i' or string[ch]=='O' or string[ch]=='o' or string[ch]=='U' or string[ch]=='u'):
            try:
                v=vowel.pop()
            except:
                pass
            string[ch]=v
    new=""
    for x in string: 
            new += x  
    return new
string="hello"
print(convert(string))