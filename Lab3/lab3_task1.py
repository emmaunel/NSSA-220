import sys
import statistics

def read_data(filename, list):
    sepal_length = []
    sepal_width = []
    petal_length = []
    petal_width = []
    hate_list = []
    with open(filename) as f:
        start = 73
        count = 1
        for l in f:
            if count >= start:
                line = l.strip().split(",")
                sepal_length.append(float(line[0]))
                sepal_width.append(float(line[1]))
                petal_length.append(float(line[2]))
                petal_width.append(float(line[3]))
                hate_list.append(line[4])
            count += 1
    list.append(sepal_length)
    list.append(sepal_width)
    list.append(petal_length)
    list.append(petal_width)
    list.append(hate_list)

    return list


def process_numeric_field(lists, column):
    min_val = min(lists[column])
    max_val = max(lists[column])
    ave_val = round(sum(lists[column])/len(lists[column]), 2)
    sd = statistics.stdev(lists[column])
    return min_val, max_val, ave_val, round(sd, 2)

def count_iris_type(why_list_but_dict):
    seto = 0
    vers = 0
    virgi = 0
    for i in why_list_but_dict:
        if i == "Iris-setosa":
            seto += 1
        elif i == "Iris-versicolor":
            vers += 1
        else:
            virgi += 1
    return seto, vers, virgi


def main():
    if len(sys.argv) < 2:
	print("Usage: python lab3_task1.py <filename>")
	exit(0)
    filename = sys.argv[1]
    listoflist = []
    lists = read_data(filename, listoflist)
    for i in range(4):
        min, max, ave, sd = process_numeric_field(lists, i)
        if i == 0:
            print("Sepal Length: min=" + str(min) + ", max=" + str(max) + ", average=" + str(ave) + ", sd=" + str(sd))
        elif i == 1:
            print("Sepal Width: min=" + str(min) + ", max=" + str(max) + ", average=" + str(ave) + ", sd=" + str(sd))
        elif i == 2:
            print("Petal Length: min=" + str(min) + ", max=" + str(max) + ", average=" + str(ave) + ", sd=" + str(sd))
        else:
            print("Petal Width: min=" + str(min) + ", max=" + str(max) + ", average=" + str(ave) + ", sd=" + str(sd))
    seto, vers, virgi = count_iris_type(lists[4])
    print("Iris Types: Iris Setosa=" + str(seto) + ", Iris Versicolor=" + str(vers) + ", Iris Virginica=" + str(virgi))

if __name__ == "__main__":
    main()
