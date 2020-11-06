from functools import singledispatch

@singledispatch
def fun(arg, verbose=False):
	if verbose:
		print("Let me just say,", end=" ")
	print(arg)

@fun.register
def _(arg: int, verbose=False):
	if verbose:
		print("Strength in numbers, eh?", end=" ")
	print(arg)

@fun.register
def _(arg: list, verbose=False):
	if verbose:
		print("Enumerate this:")
	for i, elem in enumerate(arg):
		print(i, elem)

@fun.register(complex)
def _(arg, verbose=False):
	if verbose:
		print("Better than complicated.", end=" ")
	print(arg.real, arg.imag)


def main():
	fun(1,True)
	fun(complex(12,13),True)
	fun(["Pen","Pineapple","Apple","Pen"],True)
	
if __name__ == '__main__':
	main()