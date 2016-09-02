import os
import sys
import sqlite3
import statistics

#Identifies the path on my personal computer where the SQLite database is located
msd_set_path='C:/Users/User/Desktop/BSc Computer Science/Year 3/COMP3200 - Part III Individual Project/Dataset/Last fm dataset/Final'
msd_set_db_path=os.path.join(msd_set_path,'Database')
assert os.path.isdir(msd_set_path),'The path is wrong'

def getSimilar(ID):
        
		#Query for accessing the similars_src table
        q = "SELECT target FROM similars_src WHERE tid='%s'" % ID
        res = conn.execute(q)
        qres=res.fetchone()
        
		#Creation of two arrays used for storing the data temporarily and eventually print it
        if qres == None:
                result=[]
        else:
                data = qres[0]
                result =[]
                simil = []
        
		#Applying the proposed algorithm of variance and mean
        for idx, d in enumerate(data.split(',')):
                if idx % 2 == 0:
                        p = [d]
                else:
                        p.append(float(d))
                        result.append(p)            
                        simil.append(float(d))
                        a = statistics.mean(simil)
        b = statistics.variance(simil)
        lower = a-b
        upper = a+b               
        for s in range(len(simil)):
                c = (a - simil[s])*(a - simil[s])
                
				#Check for duplicates
                if simil[s] != simil[s-1]:
                        print('Similar track: ' + str(result[s][0]) + ' has variance of ' + str(c))        
                          
        print ('Number of similar tracks found:' + str(len(result)))
        print ("Overall variance: " + str(b))
        print ("Min boundary: " + str(lower))
        print ("Mean: " + str(a))
        print ("Max boundary: " + str(upper))
        return result

#Creating a connection with the database and executing the query to fetch the data
conn = sqlite3.connect(os.path.join(msd_set_db_path,'lastfm_similars.db'))
q = "SELECT tid FROM similars_src"
res = conn.execute(q)
conn.close

s = input('Search for an artist by ID: ')
similar_artists=getSimilar(s)
