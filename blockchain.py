class BlockChain(object):
	def __init__(self):
		self.chain = []
		self.current_transactions = []

	def new_block(self):
		#create a new block, add to the chain
		pass

	def new transaction(self, sender, recipient, amount):
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
		#hash a block (without need to instantiate the class)
		pass

	@property
	def last_block(self):
		#return the last block in the chain
		pass

