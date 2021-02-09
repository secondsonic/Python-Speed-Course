#Handling Exception
#normalx = 7 / 0
#ZeroDivisionError: division by zero
try:
    x = 7 / 0
except Exception as e:
    print(e)
finally:
    print('Finally')
#OR
try:
    x = 7 / 0
except:
    print()