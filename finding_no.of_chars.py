n = input()
n = n.lower()
count = {}
for chars in n:
    if chars == " ":
        continue 
    if chars in count:
        count[chars] += 1
    else:
        count[chars] = 1 
        
for chars in sorted(count):
    print(chars,": ",count[chars], sep="")
        
