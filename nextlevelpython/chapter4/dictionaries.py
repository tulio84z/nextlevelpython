
def test_mapping_operations():

	D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
	assert D['food'] == 'Spam'

	D['quantity'] += 1
	assert D['quantity'] == 5 and D == {'color': 'pink', 'food': 'Spam', 'quantity': 5}

	D = {}
	D['name'] = 'Bob' # Create keys by assignment
	D['job'] = 'dev'
	D['age'] = 40
	assert D == {'age': 40, 'job': 'dev', 'name': 'Bob'}
	assert D['name'] == 'Bob'

	bob1 = dict(name='Bob', job='dev', age=40) # Keywords
	assert bob1 == {'age': 40, 'name': 'Bob', 'job': 'dev'}

	bob2 = dict(zip(['name', 'job', 'age'], ['Bob', 'dev', 40]))
	assert bob2 == {'job': 'dev', 'name': 'Bob', 'age': 40}


def test_dictionary_nesting():
	rec = {'name': {'first': 'Bob', 'last': 'Smith'},'jobs': ['dev', 'mgr'],'age': 40.5}

	assert rec['name'] == {'last': 'Smith', 'first': 'Bob'}
	assert rec['name']['last'] == 'Smith'
	assert rec['jobs']  == ['dev', 'mgr']
	assert rec['jobs'][-1] == 'mgr'

	rec['jobs'].append('janitor') # Expand Bob's job description in place
	assert rec == {'age': 40.5, 'jobs': ['dev', 'mgr', 'janitor'], \
	'name': {'last': 'Smith','first': 'Bob'}}

def test_missing_keys():
	D = {'a': 1, 'b': 2, 'c': 3}
	assert D == {'a': 1, 'b': 2, 'c': 3}

	try:
		D['f']
	except Exception as e:
		ke = KeyError()
		assert type(ke) == type(e)

def test_default_values():
	D = {'a': 1, 'b': 2, 'c': 3}
	value = D.get('x', 0) # Index but with a default
	assert value == 0

	#Previous assertions is equivalent to this:
	value = D['x'] if 'x' in D else 0 # if/else expression form
	assert value == 0

def test_sorting_keys():
	D = {'a': 1, 'c': 3, 'b': 2}

	#Order does not matter!
	assert D == \
	{'a': 1, 'c': 3, 'b': 2} == \
	{'a': 1, 'b': 2, 'c': 3} == \
	{'c': 3, 'b': 2, 'a': 1} 

	'''
	Order of keys is not garanteed -might vary according to python implementation/version
	assert Ks == ['a', 'c', 'b'] might fail since it is not dependent on the order 
	of declaration!	'''
	Ks = list(D.keys())

	#assures correct order!
	Ks.sort()
	assert Ks == ['a', 'b', 'c']

	val = 1
	for key in Ks:
		assert val == D[key]
		val +=1

	assert D == {'a': 1, 'c': 3, 'b': 2}
	
	val = 1	
	for key in sorted(D):
		assert val == D[key]
		val +=1