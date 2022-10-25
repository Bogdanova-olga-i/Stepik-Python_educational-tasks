'''3.4-1'''
dict={}
with open('dataset_3363_2.txt', 'r') as inf:
    for line in inf:
        line=line.strip()
        text=line.upper().split()
        for word in text:
            if word not in dict:
                dict[word]=1
            else:
                dict[word]+=1
m=1
w=['z']
for word in dict:
    if dict[word]>m:
        m=dict[word]
        w[0]=word
    elif dict[word]==m:
        if 'word'<w[0]:
            w[0]='word'
with open('out_word_count.txt', 'w') as z:
    z.write(w[0], str(m))




