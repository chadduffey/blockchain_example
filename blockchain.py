class BlockChain(object):
	def __init__(self):
		self.chain = []
		self.current_transactions = []

	def new_block(self):
		#create a new block, add to the chain
		pass

	def new transaction(self):
		#add a transaction to the list
		pass

	@staticmethod
	def hash(block):
		#hash a block (without need to instantiate the class)
		pass

	@property
	def last_block(self):
		#return the last block in the chain
		pass

	