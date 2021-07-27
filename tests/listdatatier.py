# DBS-3 imports
from dbsClient.apis.dbsClient import *
url="https://cmsweb-prod.cern.ch/dbs/prod/global/DBSReader/datatiers"
cert="/afs/cern.ch/user/n/nfarmer/.globus/usercert.pem"
prkey="/afs/cern.ch/user/n/nfarmer/.globus/userkey.pem"
# API Object    
dbs3api = DbsApi(url=url, cert=cert, key=prkey)
# dbs3api = DbsApi(url=url)

print(dbs3api.listDataTiers())

print(dbs3api.listDataTiers(datatier='AOD'))

