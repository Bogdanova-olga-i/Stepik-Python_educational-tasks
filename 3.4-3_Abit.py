'''3.4-3 The program reads the source file with structure (Abit_Surname; math_grade; phys_grade; rus_grade). For each applicant, calculates the average mark for three subjects and writes it to a file
The program also calculates the average scores for each of the subjects.'''
dict={}
abit_count, sum_math, sum_phys, sum_lang=0,0,0,0
with open('dataset_3363_4.txt', 'r') as inf, open('out_abit.txt', 'w') as out:
    for abit in inf:
        abit=line.strip(;)
        sum,count=0,0
        for i in range(1:(len(abit)-1)):
            sum+=int(abit[i])
            count\+=1
        abit_average=sum/count
        out.write(abit_average+'\n')
        abit_count+=1
        sum_math+=int(abit[1])
        sum_phys+=int(abit[2])
        sum_lang+=int(abit[3])
    out.write(str(sum_math/abit_count)+' '+str(sum_phys/abit_count)+' '+str(sum_lang/abit_count)


