from stanfordkarel import *


class ktools: 
  def m(self):
    """Shorthand for Move"""
    move()

  def tl(self):
    """Turn Left"""
    turn_left()

  def tr(self):
    self.tl()
    self.tl()
    self.tl()


  def ta(self):
    """Turn Around"""
    self.tl()
    self.tl()

  def pick(self):
    """Pick Beeper"""
    pick_beeper()
  def put(self):
    """Put Beeper"""
    put_beeper()


  def put2(self):
    """Put 2 beepers in a line"""
    self.put()
    self.m()
    self.put()

  def put5(self):
    """Put 5 beepers in a line"""
    self.put2()
    self.m()
    self.put2()
    self.m()
    self.put()

  def h(self):
    """Print H usin beepers"""
    self.tl()
    self.put5()
    self.tr()
    self.m()
    self.m()
    self.m()
    self.tr()
    self.put5()
    self.ta()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.put2()
    self.tl()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.m()
    self.m()
    self.m()

  def fic(self) -> bool:
    """Front Is Clear"""
    return front_is_clear()

  def fib(self) -> bool:
    """Front Is Blocked"""
    return not self.fic()

  def ric(self) -> bool:
    """Right Is Clear"""
    self.tr()
    if self.fic():
      self.tl()
      return True
    self.tl()
    return False

  def rib(self) -> bool:
    """Right Is Blocked"""
    return not self.ric()

  def mazemove(self):
    """Maze Move"""
    if self.fib():
      self.tl()
    else:
      self.m()
      if self.ric():
        self.tr()
        self.m()
        if self.ric():
          self.tr()
          self.m()

  def mm(self, num):
    for number in range(0, num):
      self.m()

  def putm(self, num):
    for i in  range(num - 1):
      self.put()
      self.m()
    self.put()

  def pickm(self, num):
    for _ in range(num - 1):
      self.pick()
      self.m()
    self.pick()

  def zero(self):
    """Print 0 Using Beepers"""
    self.tl()
    self.put5()
    self.tr()
    self.m()
    self.putm(2)
    self.m()
    self.tr()
    self.put5()
    self.tr()
    self.m()
    self.m()
    self.putm(2)
    self.ta()
    self.mm(5)

  def one(self):
    self.tl()
    self.mm(5)
    self.ta()
    self.putm(5)
    self.tl()
    self.mm(2)
    pass

    

def main():
    """ Karel code goes here! """
    kt = ktools()
    kt.one()
    for _ in range(9):
      kt.zero()    
    pass



if __name__ == "__main__":
    run_karel_program()