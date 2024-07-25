class A:
    pass

class B(A):
    pass

print(issubclass(B, A))  # Output: True

