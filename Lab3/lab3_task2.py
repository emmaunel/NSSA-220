import sys
import os
import hashlib

md5orig = "md5_orig.txt"
def main():
    if len(sys.argv) < 2:
		print("Usage: python lab3_task2.py <filename>")
		exit(0)
    filename = sys.argv[1]
    
    md5origlist = []
    with open(md5orig) as f:
		for l in f:
			line = l.strip().split(" ")
			md5origlist.append(line)

    #print(str(md5origlist))
    md5new = []
    with open(filename) as f:
		for l in f:
			line = l.strip().split(" ")
			md5new.append(line)

    for ele in md5origlist:
    	#print(ele[0])
        for md5 in md5new:
			#print(md5[0])
			if ele[0] == md5[0]:
				#print("Match: " + md5[1])
				if ele[1] == md5[1]:
					continue
				else:
					print(str(ele[0]) + ": MD5 original = " + md5[1] + ", new MD5 = " + ele[1])
				break

				#if ele[1] != md5[1]:
			#	print(str(ele[0]) + ": MD5 original = " + md5[1] + ", new MD5 = " + ele[1])
				#print(ele)
    # Comparing both list
    # temp contains md5 from the file(md5.txt)
    # md5list contains md5 from the script(system)
    #for ele in md5new:
	#for md5 in md5orig:
	 #   if ele[0] == md5[0]:
		#if ele[1] != md5[1]:
		#print(str(ele[0]) + ": MD5 original = " + md5[1] + ", new MD5 = " + ele[1])

if __name__ == "__main__":
    main()
