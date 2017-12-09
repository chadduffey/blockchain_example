import hashlib
import json
from time import time


class BlockChain(object):
	def __init__(self):
		self.chain = []
		self.current_transactions = []

		#genisis block
		self.new_block(previous_hash=1, proof=100)


	def new_block(self):
		"""
		Create a new block in the blockchain

		:param proof: <int> the proof given by the proof of work algorithm
		:param previous_hash: (Optional) <str> Hash of previous block
		:return: <dict> New Block
		"""

		block = {
			'index': len(self.chain) + 1,
			'timestamp': time(),
			'transactions': self.current_transactions,
			'proof': proof,
			'previous_hash': previous_hash or self.hash(self.chain[-1]),
		}

		#reset the list of transactions
		self.current_transactions = []

		self.chain.append(block)

		return block


	def new_transaction(self, sender, recipient, amount):
		""" 
		creates a new transaction to go into the next mined block

		:param sender: <str> Address of the sender
		:param recipient: <str> Address of the recipient
		:param amount: <int> Amount
		:return: <int> the index of the block that will hold this transaction
		"""

		self.current_transactions.append({
			'sender': sender,
			'recipient': recipient,
			'amount': amount
			})

		return self.last_block['index'] + 1

	@staticmethod
	def hash(block):
		"""
		Create SHA-256 hash of the block

		:param block: <dict> Block
		:return: <str>
		"""

		#order dict so that hashes are consistent
		block_string = json.dumps(block, sort_keys=True).encode()

		return hashlib.sha256(block_string).hexdigest()


	@property
	def last_block(self):
		return self.chain[-1]

