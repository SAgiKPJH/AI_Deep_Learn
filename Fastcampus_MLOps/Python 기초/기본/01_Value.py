print(2**3)
print("3"*3)
print("Hello"[:3])
print("Hello"[-3:])
print("Hello"[1:-1])
print("Hello".isalpha())
print("33".isdecimal())
multi_line = """
    Hello,
    This is a multi-line string.
    It contains multiple lines.
"""
print(multi_line)
print("Hello %s, Nice %f" % ("Wow", 10.5))
print("Hello {}, Nice {}".format("Wow", 10.5))
print("Hello {1}, Nice {0}".format("Wow", 10.5))
print(f"I Say, {multi_line}")
num = input("숫자를 입력해주세요.")
print(num)