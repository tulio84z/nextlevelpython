
def test_tuple_properties():

	T = (1, 2, 3, 4) # A 4-item tuple
	assert len(T) == 4

	assert T + (5, 6) == (1, 2, 3, 4, 5, 6)
	assert T[0] == 1

def test_tuple_type_specific_operations():
	T = (1, 2, 3, 4)
	assert T.index(4) == 3
	assert T.count(4) == 1 # 4 appears once

def test_tuple_immutability():
	T = (1, 2, 3, 4)
	try:

		T[0] = 2 # Tuples are immutable
	except Exception as e:
		te = TypeError()
		assert type(e) == type(te)

	id_t1 = id(T)
	T = (2,) + T[1:]
	assert T == (2, 2, 3, 4)

	id_t2 = id(T)
	assert id_t1 != id_t2

	try:
		T.append(4)
	except Exception as e:
		ae = AttributeError()
		assert type(ae) == type(e)

def test_tuple_support_for_mixed_types():

	#Different way of defining a tuple
	T = 'spam', 3.0, [11, 22, 33]
	assert T[1] == 3.0
	assert T[2][1] == 22