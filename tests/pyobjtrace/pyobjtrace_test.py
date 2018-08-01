from pyobjtrace import objtrace

def test_enables_and_disabled():
    objtrace.enable()
    objtrace.get_counts()
    objtrace.disable()

def test_allocation_counts():
    x = 0
    l = []
    objtrace.enable()
    while x < 100:
        l.append([1])
        x = x + 1
    c = objtrace.get_counts()
    assert((10, 0, 0, 0) == c)
