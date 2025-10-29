from isbn import is_valid_isbn10, is_valid_isbn13

def test_isbn10_invalido():
    assert is_valid_isbn10("0306406153") == False   
    assert is_valid_isbn10("03A6406152") == False   

def test_isbn13_invalido():
    assert is_valid_isbn13("9780306406158") == False 
    assert is_valid_isbn13("97803A6406157") == False  
