def any_lowercase1(s):
     for c in s:
          if c.islower():
               return True
          else:
               return False

# 2

def any_lowercase2(s):
     for c in s:
          if 'c'.islower():
               return 'True'
          else:
               return 'False'


# 3

def any_lowercase3(s):
     for c in s:
          flag = c.islower()
     return flag


# 4

def any_lowercase4(s):
     flag = False
     for c in s:
          flag = flag or c.islower()
     return flag


# 5

def any_lowercase5(s):
     for c in s:
          if not c.islower():
               return False
     return True


print(any_lowercase1("Heloo"))
print(any_lowercase2("Heloo"))
print(any_lowercase3("Heloo"))
print(any_lowercase4("Heloo"))
print(any_lowercase5("Heloo"))