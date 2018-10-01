from encode import encode


def test_empty_string():
  assert encode("") == ""
  
  def test_strings_second_test():
    assert encode("aaa") == 'a3'
    
  def test_strings_third_test():
    assert encode("aabab") == 'a2b1a1b1'
    
  def test_strings_fourth_test():
    assert encode("aaaabbbb") == 'a4b4'
