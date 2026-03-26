a=int(input("a>"))
b=int(input("b>="))
c=int(input("c>="))

if a**2+b**2==c**2:
    print("직각삼각형 입니다.")
elif a**2+b**2>c**2:
    print("둔각삼각형 입니다.")
else :
    print("예각삼각형 입니다.")
