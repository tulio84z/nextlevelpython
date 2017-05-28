
def test_sequence_operations():
	S = 'Spam'
	assert len(S) == 4
	assert S[0] == 'S'
	assert S[1] == 'p'
	assert S[-1] == 'm'
	assert S[-2] == 'a'

	assert S[-1] == S[len(S) -1]

	assert S[1:3] == 'pa'

	assert S[1:] == 'pam'
	assert S[0:3] == S[:3] == S[:-1] == 'Spa'
	assert S == S[:] == 'Spam'

	assert S + 'xyz' == 'Spamxyz'
	assert S * 8 == 'SpamSpamSpamSpamSpamSpamSpamSpam'

def test_immutability():
	S = 'Spam'

	try:
		S[0] = 'z'
	except Exception as e:
		t = TypeError()
		assert type(e) == type(t)

	id_s1 = id(S)

	#Creates different string!
	S = 'z' + S[1:]
	assert S == 'zpam'
	
	id_s2 = id(S)
	assert id_s1 != id_s2