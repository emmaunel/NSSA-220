import sys

def read_data(filename, list):
    with open(filename) as f:
        start = 73
        count = 1
        for l in f:
            print(l)


def main():
    filename = sys.argv[1]
    sepal_length = []
    sepal_width = []
    petal_length = []
    petal_width = []
    occ = dict()
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
                if line[4] in occ:
                    occ[line[4]] = occ[line[4]] + 1
                else:
                    occ[line[4]] = 1
            count += 1
    print("Sepal Length: min=" + str(min(sepal_length)) + ", max=" + str(max(sepal_length)) + ", average=" + str(round(sum(sepal_length)/len(sepal_length), 2)))
    print("Sepal Width: min=" + str(min(sepal_width)) + ", max=" + str(max(sepal_width)) + ", average=" + str(round(sum(sepal_width)/len(sepal_width), 2)))
    print("Petal Length: min=" + str(min(petal_length)) + ", max=" + str(max(petal_length)) + ", average=" + str(round(sum(petal_length)/len(petal_length), 2)))
    print("Sepal Length: min=" + str(min(petal_width)) + ", max=" + str(max(petal_width)) + ", average=" + str(round(sum(petal_width)/len(petal_width), 2)))
    print("Iris Types: Iris Setosa=" + str(occ['Iris-setosa']) + ", Iris Versicolor=" + str(occ['Iris-versicolor']) + ", Iris Virginica=" + str(occ['Iris-virginica']))

main()