import json
import blockchain
import time

def dataToTransaction(userId, equipId):
    
    temp=[userId, equipId]
    blockTransaction=json.dumps(temp)
    
    return blockTransaction
    
