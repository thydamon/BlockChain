#########################################################################
# File Name: BlockChain.py
# Author: Damon
# mail: thydamon@gmail.com
# Created Time: Sat 16 Dec 2017 06:57:36 AM EST
#########################################################################
#!/usr/bin/python

import hashlib
import json
from time import time

class BlockChain(object):
	def __init__(self):
		self.chain = []
		self.current_transactions = []

		# create the genesis block
		self.new_block(previous_hash=1, proof=100)

	def new_block(self,proof, previous_hash=None):
		"""
		@brief  generate a new block

		<pre>
				generate a new block
		</pre>

		@params [in]<int> proof: the proof given by the proof of work algorithm
		@params [in]<optional> previous_hash: hash of previous block
		
		@return <dict>: new block
		"""
		block = {
			'index': len(self.chain) + 1,
			'timestamp': time(),
			'proof': proof,
			'previous_hash': previous_hash or self.hash(self.chain[-1]),
		}
	def new_transaction(self,sender,recipient,amount):
		"""
		@brief  generate a new transaction information, it will be 
				include a block
		<pre>
				generate a new transaction information, it will be
				include a block
		</pre>

		@params [in]<str> sender:address of the sender
		@params [in]<str> recipitent:address of the recipient
		@params [in]<str> amount:transaction amount

		@return <int>: the index of the block that will hold this transaction
		"""
		self.current_transactions.append({
			'sender':sender,
			'recipient':recipient,
			'amount':amount,})
		return self.last_block['index'] + 1

	def hash(block):
		"""
		@brief	genrate SHA-256 hash value of block

		<pre>
				genrate SHA-256 hash value of bloc	
		</pre>

		@params [in]<dict> block:block
		@return <str>:
		"""

		# the dictionay must be orderly, or it will have inconsistent hash values
		block_string = json.dumps(block,sort_keys=True).encode()
		return hashlib.sha256(block_string).hexdigest()
	def last_block(self):
		return self.chain[-1]
