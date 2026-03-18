class StaticArray:
   def __init__(self, n):
      self.data = [None] * n
   def get_at(self, i):
      if not (0 <= i < len(self.data)): raise IndexError
      return self.data[i]
   def set_at(self, i, x):
      if not (0 <= i < len(self.data)): raise IndexError
      self.data[i] = x

def birthday_match(students):
    '''
    Find a pair of students with the same birthday
    Input: tuple of student (name, bday) tuples
    Output: tuple of student names or None
    '''
    n = len(students)
    record = StaticArray(n)
    for k in range(n):
        (name1, bday1) = students[k]
        for i in range(k):
            (name2, bday2) = record.get_at(i)
            if bday1 == bday2:
               return (name1, name2)
        record.set_at(k, (name1, bday1))
    return None


def print_match(pair):
    if pair is not None:
        print(' * Matching birthday found for students: {0:s} and {1:s}.'.format(pair[0], pair[1]))
    else:
        print(' * No matching birthday found.')
    

if __name__ == '__main__':
    s1 = (('Eilen', ('aug',10)), ('Fiona', ('jan',10)))
    s2 = s1 + (('Betty', ('aug', 10)),)

    print('\n Student list = ',s1)
    m = birthday_match(s1)
    print_match(m)

    print('\n Student list = ',s2)
    m = birthday_match(s2)
    print_match(m)

