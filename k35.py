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
    """Print H using beepers"""
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

  def e(self):
    """Print E using beepers"""
    self.tl()
    self.put5()
    self.tr()
    self.m()
    self.put2()
    self.m()
    self.put()
    


def main():
    """ Karel code goes here!"""
    move()
    turn_left()
    move()
    move()
    kt = ktools()
    kt.h()
    kt.e()
    kt.l()
    kt.l()
    kt.o()
    pass



if __name__ == "__main__":
    run_karel_program()