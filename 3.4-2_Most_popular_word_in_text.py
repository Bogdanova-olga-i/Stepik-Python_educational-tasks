'''Task 3.4-2. The program reads the text from the file and outputs the most popular word and the number of its repetitions to the file. If there are several equally popular words, print the lexigraphically smaller'''
dict={}
with open('dataset_3363_2.txt', 'r') as inf:
    for line in inf:
        line=line.strip()
        text=line.upper().split()
        for word in text: #word count
            if word not in dict:
                dict[word]=1
            else:
                dict[word]+=1
m=1
w=['z']
for word in dict:
    if dict[word]>m: #search most popular word
        m=dict[word]
        w[0]=word
    elif dict[word]==m: #lexigraphical comparing
        if 'word'<w[0]:
            w[0]='word'
with open('out_word_count.txt', 'w') as z:
    z.write(w[0], str(m))




