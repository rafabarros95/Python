import pytest
import Numbers

from Numbers.Calculator import square

def main():
    test_positiv()
    test_negative()
    test_zero()

def test_positiv():
    assert square(5) == 25
    assert square(3) == 9
    assert square(8) == 64
    assert square(1) == 1
    
def test_zero():
    assert square(0) == 0

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(-4) == 16

def test_str():
    with pytest.raises(TypeError):  # raises the input as string 
        square("cat")


if __name__ == "__main__":
    main()
    print("Everything passed")