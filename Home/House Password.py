#!/usr/bin/env python
# coding: utf-8

# In[1]:


def checkio(data: str) -> bool:
    chars = set(data)
    low = False
    up = False
    digit = False
    if len(data) >= 10:
        for ch in chars:
            if not low and ch.islower():
                low = True
            if not up and ch.isupper():
                up = True
            if not digit and ch.isdigit():
                digit = True
    return low and up and digit


# In[2]:


#Some hints
#Just check all conditions
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")


# In[ ]:




