import rot13 as r
def test_Rot13(str):
  """
  Функция проверяет функцию шифрования Rot13
  """
  assert(r.rot13(r.rot13(str)) == str) 
  return r.rot13(r.rot13(str)) == str