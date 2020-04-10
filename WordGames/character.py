class Character():
  def __init__(self, char_name, char_description):
    self.name = char_name
    self.description = char_description
    self.conversation = None

  def describe(self):
    print( "\n" + self.name + " is here!" )
    print( self.description )
  
  def talk(self):
    if self.conversation is not None:
      print("\n[" + self.name + " says]: " + self.conversation)
    else:
      print(self.name + " doesn't want to talk to you")

  def fight(self, combat_item):
    print("\n[" + self.name + "] doesn't want to fight you." )
    return True

  def set_conversation(self, conversation):
    self.conversation = conversation
    
  def get_description(self):
    return self.description



