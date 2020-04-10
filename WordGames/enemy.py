class Enemy(Character):
  enemies_defeated = 0

  def __init__(self, char_name, char_description):
    super().__init__(char_name, char_description)
    self.weakness = None
   
  def fight(self, combat_item):
    if combat_item == self.weakness:
      print("You successfully fend " + self.name + " off with the " + combat_item.get_name() )
      Enemy.enemies_defeated = Enemy.enemies_defeated + 1
      return True
    else:
      print("You brought a " + combat_item.get_name() + "! " + self.name + " wipes you out, puny room invader!")
      return False

  def set_weakness(self, weakness):
    self.weakness = weakness
  
  def set_defeated(self,number_defeated):
    Enemy.enemies_defeated = number_defeated
  
  def get_defeated(self):
    return Enemy.enemies_defeated

  def get_weakness(self):
    return self.weakness
 
