# hello python

# На вход подаются 2 файла, которые в память не поместятся. 
# В каждом файле в каждой строке число. Числа могут повторяться как в каждом файле, так и между файлами. 
# Каждый файл отсортирован по возрастанию. 
# Вам необходимо сделать третий файл, который будет содержать отсортированные по возрастанию данные из первого и второго файла.

# F1: 1 3 5 5
# F2: 4 5 6
# F3: 1 3 4 5 5 5 6

file1 = open('file1.txt', 'r')

file2 = open('file2.txt', 'r')

file3 = open('file3.txt', 'w')

line_file1 = file1.readline()
line_file2 = file2.readline()

while line_file1 or line_file2:
    dig_line1 = 10000
    dig_line2 = 10000
    if line_file1:
        dig_line1 = int(line_file1)
    if line_file2:
        dig_line2 = int(line_file2)
    if dig_line1 == dig_line2:
        file3.write(str(dig_line1) + '\n')
        file3.write(str(dig_line2) + '\n')
        line_file1 = file1.readline()
        line_file2 = file2.readline()
    elif dig_line1 < dig_line2:
        file3.write(str(dig_line1) + '\n')
        line_file1 = file1.readline()
    elif dig_line1 > dig_line2:
        file3.write(str(dig_line2) + '\n')
        line_file2 = file2.readline()

file1.close()
file2.close()
file3.close()
        

