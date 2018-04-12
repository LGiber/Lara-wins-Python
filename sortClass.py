inFile = open('input.txt', 'r', encoding='utf8').readlines()
outFile = open('output.txt', 'w', encoding='utf8')

for line in sorted(inFile):
    line = line.split()
    outFile.write(line[0] + " " + line[1] + " " + line[3] + '\n')
    print(line[0] + " " + line[1] + " " + line[3])
