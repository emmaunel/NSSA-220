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
    md5list = []
    for i in bin_dir:
       elem_list = []
       elem_list.append(i)
       elem_list.append(hashlib.md5(i).hexdigest())
       temp.append(elem_list)
   # print(temp)
    with open(filename) as f:
	for l in f:
	    line = l.strip().split(" ")
	   # print(line)
	    md5list.append(line)

    # Comparing both list
    # temp contains md5 from the file(md5.txt)
    # md5list contains md5 from the script(system)
    for ele in temp:
	for md5 in md5list:
	    if ele[0] == md5[0]:
		#if ele[1] != md5[1]:
		print(str(ele[0]) + ": MD5 original = " + md5[1] + ", new MD5 = " + ele[1])

if __name__ == "__main__":
    main()
