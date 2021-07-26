from hashlib import sha256


# Hashing function
def update_hash(*args):
    hashing_text = ''
    h = sha256()
    
    
    for arg in args:
        hashing_text += str(arg)
        
    h.update(hashing_text.encode('utf-8'))
    
    return h.hexdigest()



# The Block class
class Block():
    data = None
    hash = None
    nonce = 0
    previous_hash = '0' * 64
    
    

    def __init__(self, data, number = 0):
        self.data = data
        self.number = number
        
        
    # Block Hahsing method   
    def hash(self):
        return update_hash(
            self.previous_hash, 
            self.number, 
            self.data, 
            self.nonce
            )
    
    
    # Formatted output method
    def __str__(self):
        return str('Block: %s\nHash: %s\nPrevious: %s\nData: %s\nNonce: %s' %(
            self.number, 
            self.hash(), 
            self.previous_hash, 
            self.data, 
            self.nonce
            ))


# Blockchain class
class Blockchain():
    difficulty = 4
    
    
    
    def __init__(self, chain=[]):
        self.chain = chain


    # Inserts a single block to the blockchain
    def add(self, block):
        self.chain.append(block)
        
        
    # Deletes a block in the blockchain   
    def remove(self, block):
        self.chain.remove(block)
        
        
    # Mines a single block    
    def mine(self, block):
        try:
            # Assign previous Hash value to new block
            block.previous_hash = self.chain[-1].hash()
        except IndexError:
            pass
        
        # Loops until the 0s at the begining of the block hash equals the difficulty
        while True:
            if block.hash()[:self.difficulty] == '0' * self.difficulty:
                self.add(block)
                break
            else:
                # Keeps tracks of how many times it the sha256 algorithm ran
                block.nonce += 1
                
                
    # Checks if a block is valid            
    def isValid(self):
        for i in range(1, len(self.chain)):
            _previous = self.chain[i].previous_hash
            _current = self.chain[i-1].hash()
            if _previous != _current or _current[:self.difficulty] != '0' * self.difficulty:
                return False
            else:
                return True