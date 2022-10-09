import sys

multiples_lists = []

#open input file specified as first argument used to run the program
#the expected input is a list of 3 integers with space between them
#find the max multiples of the 1st and 2nd integers with up to a ceiling specified by the 3rd interger
#Sort the output ascending within the line and by the number of multiples over the whole list
#TODO: Add better error handling to unexpected input of intergers within the file
with open(sys.argv[1],'r') as input_file:
    for line in input_file:
        line = [int(i) for i in line.split()]
        if line[0] > 0:
            multiples_a = [line[0] * j for j in range(1,line[2] // line[0])]
        if line[1] > 0:
            multiples_b = [line[1] * k for k in range(1,line[2] // line[1])]
        multiples_lists.append (str(line[2]) + ":" + ' '.join(map(str,sorted(multiples_a + multiples_b))))
    multiples_lists.sort(key = len)    
input_file.close()

#print out sorted list to the screen and outputfile specified as the second argument used to run the program
#TODO: Add better handling for no outputfile provided
with open(sys.argv[2],'w') as output_file:
    for lst in multiples_lists:
        print(lst)
        output_file.write(lst + '\n')
output_file.close()
        

