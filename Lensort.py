lst = ['python', 'perl', 'java', 'c', 'haskell', 'ruby']

def lensort(li):
    li.sort(key=lambda x: len(x))

lensort(lst)
print lst