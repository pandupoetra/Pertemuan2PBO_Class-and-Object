class py_solusion:
    def reverse_words(self,s):
        return ' '.join(reversed(s.split()))
x=input()
print(py_solusion().reverse_words(x))