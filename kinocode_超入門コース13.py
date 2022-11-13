class Student:

  def __init__(self,name):
    self.name = name

  def avg(self,math,english):
    # methodの引数には必ずselfが必要
    print((math + english)/2)

a001 = Student("sato")
print(a001.name)

a002 = Student("tanaka")
print(a002.name)