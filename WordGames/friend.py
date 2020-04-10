class Friend(Character):
  def __init__(self, char_name, char_description):
    super().__init__(char_name, char_description)
    self.friendliness = 0
    self.item = None
    
  def give_item(self, item):
    if self.item is not None:
      print("I cannot hold another item")
      return False
    else:
      self.item = item
      return True
      
  def embrace(self):
    self.friendliness = self.friendliness + 1
    print("Friendship increased to " + str(self.friendliness) + ".")
  
  def attack(self, character):
    if isinstance(character, Enemy):
      print( "[" + self.name + "] attacks " + character.get_name() + " ...")
    elif isinstance(character, self):
      print( "[" + self.name + "] embraces " + character.get_name() + " warmly.")
    else:
      print( "[" + self.name + "] Sorry, I dont know " + character.get_name() + ".")

  def return_item(self, item):
    if item == self.item:
      self.item = None
      return item
    else:
      print("I do not have the " + item.get_name() + " with me")
      return False
