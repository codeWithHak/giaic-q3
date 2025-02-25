# lest learn interning
# interning matlab agar hamne use ki same (immutable (str,int,etc)) values different varaibles me
# to wo un dono varaibles ka memory address same rakhega kiu ke vlaues same hen
# issey memory optimization hojati he
# integere -5 se 256 ke darmiyan sab intern hote hen
# or str bhi choti ho agar to intern hojati he

a = 4
b = 4
print(a is b)

c = "this is a long string that will not be interned bhai kiu intern horahi he"
d = "this is a long string that will not be interned bhai kiu intern horahi he"
print(c is d) # strings kab tak intern hoti rahengi kis length tak