
def test_python_names_contain_refs_to_objects():
    """
    Even the simple int 1 is a object that is shared among references!
    Meaning: python reuses the object 1 (no new 1s are allocated!)
    """
    x = 1
    y = 1
    assert id(x) == id(y) == id(1)
    y = 2
    assert id(x) == id(1) != id(y) == id(2)

def test_how_python_tracks_references():
    """
    Python's GC keeps track of references to objects. 
    All objects (even simple ints) are stored and reused by names
    Once the refcount of an object drops to zero, python will
    activate GC to reclaim that object
    """

    #Once the refcount of an object drops to zero, python will activate GC to reclaim that object
    import random, string
    random_string = ''.join(random.choice(string.ascii_letters) for _ in range(5))
    #2 refs to the same string object
    a = random_string
    import sys
    refs_cnt = sys.getrefcount(random_string)
    #Re-referencing a name by pointing it to a diferent object, frees the previously refd object for GC (if the refcount == 0)
    a = 1
    refs_cnt2 = sys.getrefcount(random_string)
    assert refs_cnt2 < refs_cnt

def test_shared_references_and_in_place_changes():
    L1 = [1,2,3]
    L2 = L1
    assert L1 == [1,2,3] == L2
    
    L2[0] = 24
    assert L1 == [24,2,3] == L2 
    
    L1 = [1,2,3]
    # Make a copy of L1 (or list(L1), copy.copy(L1), etc.)
    L2 = L1[:]

    L2[0] = 24
    assert L1 == [1,2,3] != L2 == [24,2,3] 

def test_shared_references_and_equality():
    """
    == is NOT the same as is
    == : compares values!
    is : compares identity!
    """
    L = [1,2,3]
    M = L
    assert L == M
    assert L is M

    L = [1,2,3]
    M = [1,2,3]

    assert L == M
    assert L is not M

    L = [1,2,3]
    M = L[:]

    assert L == M
    assert L is not M
