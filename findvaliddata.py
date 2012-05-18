import sys

fp=open("data.txt","r")
cfp=open("validdata.txt","w")


for row in fp:
	if row.find("gender")==-1 or row.find("age")==-1:
		continue
	else:
		res = row.split("|")
		cfp.write(res[3]+"\t"+res[5]+"\t"+res[7])

fp.close()
cfp.close()
