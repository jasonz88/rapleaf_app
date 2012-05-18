import RapleafApi
import sys

""" This example script takes an e-mail as a command line argument 
and queries Rapleaf's database for any data associated with
the provided e-mail (unknown fields are left blank) 
The hash returned from query_by_email is iterated through
and each k/v pair is sent to std out """
  
api_key = '0b6edc22e68f41da9ebbf8bfbcf565eb'        # Set your API key here
finished_email = sys.argv[1]
unfinished_email = sys.argv[2]

fp=open("finished.txt","r")
ufp=open("unfinished.txt","r")

dp=open("dataset.txt","w")
dataset=[]

api=RapleafApi.RapleafApi(api_key)

for femail in fp.readlines():
	try:
		res=api.query_by_email(femail)
		dp.write("email"+"|"+femail[:-2]+"|")
		for k,v in res.iteritems():
			dp.write(k+"|"+v+"|")
		dp.write("class"+"|"+"f"+"\n")
	except Exception as inst:       # HTTP code returned other than 200
		code, body = inst.args
		print('Error Code = %d' % code)
		print('Error Body = %s' % body)



for uemail in ufp.readlines():
	try:
		res=api.query_by_email(uemail)
		dp.write("email"+"|"+uemail[:-2]+"|")
		for k,v in res.iteritems():
			dp.write(k+"|"+v+"|")
		dp.write("class"+"|"+"u"+"\n")
	except Exception as inst:       # HTTP code returned other than 200
		code, body = inst.args
		print('Error Code = %d' % code)
		print('Error Body = %s' % body)



fp.close()
ufp.close()
dp.close()
