class student:
  def __init__(self, first, last, code, credits):
    self.first = first
    self.last = last
    self.code = code
    self.credits = credits
  
  def tuition(self, rate):
    if self.code == 'i':
      c = float(rate) * float(250)
    else:
      c = float(rate) * float(500)
    return c

stdl1 = student('Ali','haq','i','3')

print(stdl1.code)
print(stdl1.tuition(1))
print(stdl1.tuition(2))
print(stdl1.first)
print(stdl1.last)
