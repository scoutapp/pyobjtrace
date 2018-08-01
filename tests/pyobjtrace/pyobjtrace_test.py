from pyobjtrace import objtrace

def test_enables_and_disabled():
    objtrace.enable()
    objtrace.disable()
