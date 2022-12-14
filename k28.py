from stanfordkarel import *
from time import sleep

class ktools: 
  def m(self):
    """Shorthand for Move"""
    move()

  def m2(self):
    move()
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


def main():
    """ Karel code goes here! """
    kt = ktools()
    kt.m2()
    kt.m2()
    kt.m()
    kt.tl()
    kt.m()
    kt.m()
    kt.put5()
    kt.tl()
    kt.m2()
    kt.tl()
    kt.m2()
    kt.tl()
    sleep(3)
    kt.tr()
    kt.m2()
    kt.tl()
    kt.m2()
    kt.tl()
    kt.pick()
    kt.m()
    kt.pick()
    kt.m()
    kt.pick()
    kt.m()
    kt.pick()
    kt.m()
    kt.pick()
    kt.tl()
    kt.m2()
    kt.tl()
    kt.m2()
    kt.tl()
    kt.put5()
    kt.tr()
    kt.m2()
    kt.tr()
    kt.m2()
    kt.tr()
    pass



if __name__ == "__main__":
    run_karel_program()