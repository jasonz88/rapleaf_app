#This procedure build the decision tree and returns the classification result
#argv[1]: minimun gain of the tree for post pruning
#argv[2]: email address for classify

import sys
import decisiontree

if __name__=="__main__":

	my_data=[line[:-1].split('\t') for line in file('validdata.txt')]

	tree=decisiontree.buildtree(my_data)

	decisiontree.prune(tree,float(sys.argv[1]))

	decisiontree.printtree(tree)

	decisiontree.drawtree(tree)

	import RapleafApi

	api_key = '0b6edc22e68f41da9ebbf8bfbcf565eb'
	api=RapleafApi.RapleafApi(api_key)
	try:
    		response = api.query_by_email(sys.argv[2],False,True)
		res={}
    		for k, v in response.iteritems():
        		res[k]=v
		print res
	except Exception as inst:       # HTTP code returned other than 200
    		code, body = inst.args
    		print('Error Code = %d' % code)
    		print('Error Body = %s' % body)
	try:
		observation=[]
		observation.append(res['gender'])
		observation.append(res['age'])
		print decisiontree.classify(observation,tree)
	except Exception as nres:
		print "not enough info of age and gender"
