import version_checker

#basic numeric types
def test_integers_and_long():
    i = 1234; assert type(i) == int
    i = -24; assert type(i) == int
    i = 0; assert type(i) == int
    if version_checker.is_version_27():
        i = 99999999999999; assert type(i) == long
        exec("i = 99999999999999L; assert type(i) == long")
        exec("i = 99999999999999l; assert type(i) == long")

    #Python 3.6 does not have long type
    if version_checker.is_version_36():
        i = 99999999999999; assert type(i) == int
        try:
            exec("i = 99999999999999L; assert type(i) == long")
            exec("i = 99999999999999l; assert type(i) == long")
        except:
            assert True

def test_floating_point_numbers():
    f = 1.23; assert type(f) == float
    f = 1. ; assert type(f) == float
    f = 3.14e-10 ; assert type(f) == float
    f = 4E210 ; assert type(f) == float
    f = 4.0e+210 ; assert type(f) == float

def test_octal_hex_binary_literals():
    o = 0o177; assert type(o) == int
    x = 0x9ff; assert type(x) == int
    b = 0b101010; assert type(b) == int

    assert (0o1, 0o20, 0o377) == \
           (0x01, 0x10, 0xFF) == \
           (0b1, 0b10000, 0b11111111) == \
           (1, 16, 255)

def test_complex_numbers():
    complex_nums = a,b,c = 3+4j, 3.0+4.0j, 3J
    
    for item in complex_nums:
        assert type(item) == complex

    num = 1
    assert eval("type(" +str(num)+") == int")

    num = str(num) + 'j'
    assert eval("type(" +num+") == complex")

def test_sets():
    a,b = set('spam'), {1, 2, 3, 4}
    assert type(a) == set
    assert type(b) == set

def test_boolean_type():
    x = (a,b,c,d,e,f) = True, False, bool(1), bool(0), bool("a"), bool(None)
    assert (a,b,c,d,e,f) == (True, False, True, False, True, False)

    for item in x:
        assert (type(item) == bool) and isinstance(item,int)

def test_boolean_chains():

    A,B,C = 2,4,6
    assert A < B < C

    A,B,C = 2,6,4
    assert A < B > C

    #Pitfal:
    assert (1 == 2 < 3) != ((1 == 2) < 3)
    assert (1 == 2 < 3) == (1 == 2 and 2 < 3)

def test_mixed_types_conversion():
    """
    Python always converts 'up' the lesser complex operand (1 becomes 1.0) 
    whenever there are mixed types (e.g.: int and float)
    """

    a = 1 + 2.0
    assert type(a) == float

    a,b = 2 + 4.0, 2.0 ** 2
    assert type(a) == type(b) == float

    assert 1 == 1.0

def test_integer_division_and_true_division():
    a,b = 3,4

    if version_checker.is_version_27():
        assert b/a == 1 == 1.0
        assert type(b/a) == int
        assert type(b/float(a)) == float


    if version_checker.is_version_36():
        assert (b/a == 1 == 1.0) == False
        assert b/a == 1.3333333333333333
        assert type(b/a) == float
        assert type(b//a) == int    

def test_truncation_versus_floor():
    """// Is floor division and NOT truncation division! """
    a,b = 5,2
    if version_checker.is_version_27():
        
        assert 5/2 == 2
        assert 5/-2 == -3
        assert 5//2 == 2
        assert 5//-2 == -3
        
        import math
        assert math.trunc(5/-2) == -3 
        assert math.trunc(5//-2) == -3

    if version_checker.is_version_36():
        assert 5/2 == 2.5 #Difference
        assert 5/-2 == -2.5 #Difference
        assert 5//2 == 2
        assert 5//-2 == -3
        
        import math
        assert math.trunc(5/-2) == -2 #Difference
        assert math.trunc(5//-2) == -3

def test_decimals():
    """
    Decimals == Fixed precision numbers!
    """
    from decimal import Decimal
    assert Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3') == Decimal('0.0')

    res = str(Decimal(1) / Decimal(7))
    assert  len(res) == 30 #0. + 28 precision digits (default)

    import decimal  
    decimal.getcontext().prec = 4
    res = str(Decimal(1) / Decimal(7))
    assert  len(res) == 6 #0. + 4 precision digits (default)

    with decimal.localcontext() as ctx:
        ctx.prec = 2
        assert Decimal('1.00') / Decimal('3.00') == Decimal('0.33')

        #Useful in monetary applications:
        pay = Decimal(str(1999 + 1.33))
        assert str(pay) == '2000.33' #2 precision digits 


def test_fractions():
    """
    Rational numbers
    """
    from fractions import Fraction
    x = Fraction(1, 3)
    y = Fraction(4, 6)

    assert x + y == Fraction(1,1)
    assert Fraction('.25') == Fraction(.25) == Fraction('1/4') == Fraction(1,4)


def test_sets():
    """
    Mathematical sets
    """
    x = set('abcde')
    y = set('bdxyz')
    assert x-y == {'a', 'c', 'e'} # Difference
    
    assert x | y == {'a', 'c', 'b', 'e', 'd', 'y', 'x', 'z'} # Union
    
    assert x & y == {'b', 'd'} # Intersection
    
    assert x ^ y == {'a', 'c', 'e', 'y', 'x', 'z'} # Symmetric difference (XOR)