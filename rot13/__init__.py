
# coding: utf-8

# In[3]:



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

  



# In[ ]:



