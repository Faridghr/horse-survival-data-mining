import csv
with open('horseColic1.csv') as f:
    reader = csv.reader(f)
    listOfRecords = []
    for row in reader:
        listOfRecords.append(row)
    for i in range(0 ,len(listOfRecords)):
        listOfRecords[i] = listOfRecords[i][0].split()
    count_r = 0
    mean = [[],[],[]]
    for record in listOfRecords :
        label = record[22]
        countOfRecord = 0
        for attribute in record :
            mean[0].append(0)
            mean[1].append(0)
            mean[2].append(0)
            if label == '1' and attribute != '?':
                mean[0][countOfRecord] += float(attribute)
            elif label == '2' and attribute != '?':
                mean[1][countOfRecord] += float(attribute)
            elif label == '3' and attribute != '?':
                mean[2][countOfRecord] += float(attribute)
            countOfRecord += 1
        count = 0
        for attribute in record :
            mean[0][count] = mean[0][count]/countOfRecord
            mean[1][count] = mean[1][count]/countOfRecord
            mean[2][count] = mean[2][count]/countOfRecord
            count += 0
        count = 0
        for attribute in record :
            if attribute == '?' :
                if label == '1':
                    listOfRecords[count_r][count] = str(mean[0][count])
                elif label == '2':
                    listOfRecords[count_r][count] = str(mean[1][count])
                elif label == '3':
                    listOfRecords[count_r][count] = str(mean[2][count])
            count += 1
        count_r += 1
    print(listOfRecords[0])
    for i in range(0 , len(listOfRecords)) :
        listOfRecords[i] = listOfRecords[i][:23]
    print(listOfRecords[0])
    f = open('horseColic_out.csv' ,'w')
    s = ''
    for record in listOfRecords :
        s = ''
        for attribute in record :
            s += attribute + ' '
        f.write(s + '\n')
