    #  война и мир!
text = open('C:\\Users\\user\\Desktop\\dataset_3363_4.txt','r')
s = text.read().split()
text.close()
s1=list()
s2=list()
for i in set(s):
    s1.append(i)
    s2.append(s.count(i))
print(s1[s2.index(max(s2))],max(s2))
