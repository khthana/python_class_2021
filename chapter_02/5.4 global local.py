def test_local_1():
    print(var)
    
def test_local_2():
    var = 3
    print(var)

def test_local_3():
    global var
    print(var)

def test_local_4():
    global var
    var = 5
    print(var)

def test_local_5():
    var = 8
    global var
    print(var)
    
var = 10
test_local_1()
test_local_2()
test_local_3()
test_local_4()
test_local_5()
