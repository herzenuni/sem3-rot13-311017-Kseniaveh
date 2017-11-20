#Вехова Ксения, ИВТ-2 курс, задание ROT13
# Не доконца доработано задание ROT13, не очень понимаю, как можно сделать try/except, кроме того как создать меню с выбором действий:
из консоли или из файла. Поэтому на данном этапе представляю просто поотдельности сделанные работы:) 
А также в отдельной папке представлен модуль ROT13 и модуль на проверку функции ROT13.
#Функция шифрования по алгоритму ROT13, основная часть 

text=input("Введите нужный текст:")
def rot13(str):
    res = []
    for x in str:
        if (ord("A")<=ord(x)<=ord("M")) or (ord("a")<=ord(x)<=ord("m")):
          res.append(chr(ord(x)+13))
        elif ord("N")<=ord(x)<=ord("Z") or (ord("n")<=ord(x)<=ord("z")):
          res.append(chr(ord(x)-13))
        else:
          res.append(x)
    return ''.join(res)
print(rot13(text))

#Функция шифрования по алгоритму ROT13, с добавлением try/except и тестированием 

text=input("Введите нужный текст:")
try:
  text=text/13
except TypeError:
  print("Ошибка обработанна")
print("Программа пошла дальше")
def rot13(str):
    """
    Функция шифрует входную строку, с помощью алгоритма Rot13
    """
    res=[]
    for x in str:
      try:
        if (ord("A")<=ord(x)<=ord("M")) or (ord("a")<=ord(x)<=ord("m")):
          res.append(chr(ord(x)+13))
        elif ord("N")<=ord(x)<=ord("Z") or (ord("n")<=ord(x)<=ord("z")):
          res.append(chr(ord(x)-13))
        else:
          res.append(x)
      except Exception:
        res.append(x)
    return ''.join(res)

def testRot13(str):
  """
  Функция проверяет функцию шифрования Rot13
  """
  assert(rot13(rot13(str)) == str) 
  return rot13(rot13(str)) == str


print(rot13(text))
print(testRot13(text))

#Функция шифрования по алгоритму ROT13 из файла

text=open("myfile.txt")
a=text.read(5)
out=open("file2.txt","w")
def rot13(str):
    """
    Функция шифрует входную строку, с помощью алгоритма Rot13
    """
    res = []
    for x in str:
        if (ord("A")<=ord(x)<=ord("M")) or (ord("a")<=ord(x)<=ord("m")):
          res.append(chr(ord(x)+13))
        elif ord("N")<=ord(x)<=ord("Z") or (ord("n")<=ord(x)<=ord("z")):
          res.append(chr(ord(x)-13))
        else:
          res.append(x)
    return ''.join(res)
kod="Coded in ROT13 - "+rot13(a)
dekod="Decoded from ROT13 - "+rot13(rot13(a))
out.write(kod)
out.write("\n")
out.write(dekod)
out.close()
text.close()

