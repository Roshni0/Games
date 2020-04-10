class Room():
  
  def __init__(self, name):
    self.name = name
    self.description = None
    self.linked_rooms = {}
    self.character = None
    self.item = None

  def describe(self): 
	  print(self.description.capitalize())
  
  def link_room(self, room_to_link, direction):
	  self.linked_rooms[direction] = room_to_link
	  #print( self.name + " linked rooms: " + repr(self.linked_rooms) )  
	
  def move(self, direction):
    if direction in self.linked_rooms:
      return self.linked_rooms[direction]
    else:
      print("Command not understood.")
      return self

  def set_name(self, name):
    self.name = name
  
  def set_description(self, room_description):
    self.description = room_description.lower()
  
  def set_character(self, character):
    self.character = character
  
  def set_item(self, item):
    self.item = item
    
  def get_name(self):
    return self.name
    
  def get_description(self):
    return self.description 
    
  def get_character(self):
    return self.character
      
  def get_item(self):
    return self.item

  def get_details(self):
    print( "\nFrom the " + self.name + ", " + self.description + ", you can see that: " )
    for direction in self.linked_rooms:
      room = self.linked_rooms[direction]
      print( "\t> the " + room.get_name() + " is " + direction )

  
