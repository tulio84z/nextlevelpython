
def test_silly_number_operations():
	assert 123 + 222 == 345

def test_silly_multiplication():
	result = 1.5 * 4
	assert result == 6
	assert type(result) == type(1.0)

def test_silly_exponentiation():
	assert 2 ** 100 == 1267650600228229401496703205376

#def test_show_amount_of_digits():
#	assert len(str(2 ** 1000000)) == 301030