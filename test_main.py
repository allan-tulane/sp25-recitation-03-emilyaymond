from main import quadratic_multiply, BinaryNumber



## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(3)) == 3*3
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(4)) == 3*4
    assert quadratic_multiply(BinaryNumber(4), BinaryNumber(5)) == 4*5
    assert quadratic_multiply(BinaryNumber(10), BinaryNumber(10)) == 10*10
    assert quadratic_multiply(BinaryNumber(20), BinaryNumber(8)) == 20*8
    assert quadratic_multiply(BinaryNumber(16), BinaryNumber(2)) == 16*2
