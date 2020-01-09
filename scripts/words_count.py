# Programm take txt file as argument count number of occurrences and print histo bar chart with number.

import sys

## via arguments :
# file_name = sys.argv[1]
## via console :


def print_dictionary(dic, file_name):
    print("Word\tNumber of occurrences in {0}",file_name)
    for key in dic.keys():
        print(f"{key}-{dic[key]}")

def main():
    file_name = input("Please insert file name to work with: ")
    alpha_statistic = {}
    with open(file_name,'r') as f:
        lines = f.readlines()
        print(lines)
        for line in lines:
            for word in line.split():
                if word.rstrip() in alpha_statistic.keys():
                    alpha_statistic[word]+=1
                else:
                    alpha_statistic[word]=1

    print_dictionary(alpha_statistic, file_name)

if __name__=='__main__':
       main()