class Employee:
  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + '.' + last + '@company.com'

  def bonus(self,rate):
    b = float(rate) * float(self.pay)
    return b
fn = input("what is your first name?")
ln = input("what is your last name?")
empl1 = Employee(str(fn) , str(ln) ,50000.00)

print(empl1.email)
print(empl1.pay)
print(empl1.bonus(0.10))
print(empl1.bonus(0.20))