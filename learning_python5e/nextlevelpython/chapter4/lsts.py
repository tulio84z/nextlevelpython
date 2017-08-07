
def test_sequence_operations():

	L = [123, 'spam', 1.23] # A list of three different-type objects
	assert len(L) == 3

	assert L[0] == 123 
	assert L[:-1] == [123, 'spam']
	assert  L + [4, 5, 6] == [123, 'spam', 1.23, 4, 5, 6] 

	assert L * 2 == [123, 'spam', 1.23, 123, 'spam', 1.23]
	assert L == [123, 'spam', 1.23]

def test_type_specific_operations():
	L = [123, 'spam', 1.23]

	id_1 = id(L)
	L.append('NI')
	assert L == [123, 'spam', 1.23, 'NI']
	id_2 = id(L)
	#Lists are mutable!
	assert id_1 == id_2
	
	assert L.pop(2) == 1.23

	assert L == [123, 'spam', 'NI']

	del L[2]
	assert L == [123, 'spam']


	M = ['bb', 'aa', 'cc']
	M.sort() 
	assert M == ['aa', 'bb', 'cc']
	
	M.reverse()
	assert M == ['cc', 'bb', 'aa']

def test_bounds_checking():
	L = [123, 'spam', 1.23]
	try:
		L[99]
	except Exception as e:
		ie = IndexError()
		assert type(e) == type(ie)

	try:
		L[99] = 1
	except Exception as e:
		ie = IndexError()
		assert type(e) == type(ie)	

def test_nesting():

	M = [[1, 2, 3],\
		 [4, 5, 6],\
		 [7, 8, 9]]
	
	assert M == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

	assert M[1] == [4,5,6]
	assert M[1][2] == 6
	