class Item():
  
  def __init__(self):
    self.name = None
    self.description = None
    self.usage = None
    self.construct = None
    self.stored = None

  def use(self, item):
    print("You put the " + item.name + " into your hand.")
    print("(you remember that " + item.usage() + ")")
    
  def describe(self):
    print( "\nYou see a " + self.name + " on the " + self.stored + "." )
    #print( "\nA " + self.name + ": " + self.description.capitalize() + "." )
    #print( "Use: " + self.usage.capitalize() + "." )
  
  def set_name(self, item_name):
    self.name = item_name
  
  def set_description(self, item_description):
    self.description = item_description.lower()
  
  def set_usage(self, usage):
    self.usage = usage.lower()
    
  def set_construct(self, material):
    self.construct = material.lower()
  
  def set_stored(self, stored, location):
    self.stored = location
    
  def get_name(self):
    return self.name

  def get_description(self):
    return self.description
    
  def get_usage(self):
    return self.usage

  def get_construct(self):
    return self.construct

  def get_stored(self):
    return self.stored
  
