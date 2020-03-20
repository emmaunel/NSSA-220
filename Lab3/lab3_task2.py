import sys
import os
import hashlib

def main():
    if len(sys.argv) < 2:
		print("Usage: python lab3_task2.py <filename>")
		exit(0)
    filename = sys.argv[1]
    bin_dir = os.listdir("/usr/bin/")
    #print(bin_dir)
    temp=[]
    for i in bin_dir:
       elem_list = []
       elem_list.append(i)
       elem_list.append(hashlib.md5(i).hexdigest())
       temp.append(elem_list)
   # print(temp)
    with open(filename) as f:
	for l in f:
	    line = l.strip().split(" ")
	    print(line)



if __name__ == "__main__":
    main()
