text = open('C:\\Users\\user\\Desktop\\dataset_3363_3.txt','r')
s = text.read().lower().split()
text.close()
s1=list()
s2=list()
for i in set(s):
    s1.append(i)
    s2.append(s.count(i))
a = max(s2)
b = s2.index(19)
print(s1[b],a)
         
