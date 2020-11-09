class Attribute:
	def __init__(self, attribute_id=0):
		print("Attribute constructor.")
		self.attribute_id = attribute_id

	def __get__(self, obj, objtype=None):
		value = obj.__attr
		print("Accessing %r with attribute id %r" % ("attr", self.attribute_id ))
		print("Accessing %r giving %r" % ("attr", value))
		return value

	def __set__(self, obj, value):
		print("Updating %r to %r" % ("attr", value))
		obj.__attr = value

class Session:
	attr1 = Attribute(1)             		# Descriptor instance
	attr2 = Attribute(10)

	def __init__(self):
		return

def main():
	session = Session()
                    
	session.attr1 = 2
	session.attr2 = 20

	print(vars(session))

	print(session.attr1)
	print(session.attr2)

	print(vars(vars(Session)['attr1']))
	print(vars(vars(Session)['attr2']))

	print(session._Attribute__attr)

if __name__ == '__main__':
	main()
	print("Testing")