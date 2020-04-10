from room import *
from item import *
from character import *

kitchen = Room("Kitchen")
kitchen.set_description("A room filled with ingredients to make all sorts of food, probably all moldy by now.")

dining_hall = Room("Dining Room")
dining_hall.set_description("A sour smelling room scattered with food debris.")

ballroom = Room("Ballroom")
ballroom.set_description("A large room with dusty surfaces and chandeliers.")

bathroom = Room("Bathroom")
bathroom.set_description("A small and grubby water closet in need of de-sanitising.")

kitchen.link_room(dining_hall, "north")
dining_hall.link_room(kitchen, "south")
dining_hall.link_room(ballroom, "east")
ballroom.link_room(dining_hall, "west")
ballroom.link_room(bathroom, "south")
bathroom.link_room(ballroom, "north")

item_list = []
paper = Item()
paper.set_name("Paper")
paper.set_description("a prize-pinning piece of paper for you to map out your way to victory")
paper.set_construct("its precious paper")
paper.set_usage("Flat. Its one sided.")
item_list.append(paper.get_name())

quill = Item()
quill.set_name("Quill")
quill.set_description("a nibbed-needle feather of narcissistic nonsense")
quill.set_construct("flooper head feather with a grafted silver nib")
quill.set_usage("the nib hums when writing, and the feather tickles")
item_list.append(quill.get_name())

ink = Item()
ink.set_name("Black Ink")
ink.set_description("pot of liquid that will lead you to share your victory plan")
ink.set_construct("black liquid")
ink.set_usage("dip the quill in me")
item_list.append(ink.get_name())

paper.set_stored(dining_hall.get_name(), "floor")
dining_hall.set_item( paper)

quill.set_stored(ballroom.get_name(), "floor")
ballroom.set_item(quill)

ink.set_stored(bathroom.get_name(), "floor")
bathroom.set_item(ink)

henk = Enemy("Henk", "a talking computer")
henk.set_conversation("I'm sorry Daniel, I cannot do what you ask.")
henk.set_weakness(paper)
dining_hall.set_character(hal)

may = Friend("May", "a vampire")
may.set_conversation("I need to be home before sunrise, okay?")
bathroom.set_character(may)

bob = Character("Bob", "an apple")
bob.set_conversation("crunch. crunch. crunch. ")
ballroom.set_character(bob)


current_room = kitchen
play_flag = True
while play_flag:
  current_room.get_details()
  inhabitant = current_room.get_character()
  if inhabitant is not None:
    inhabitant.describe()
  object = current_room.get_item()
  if object is not None:
    object.describe()
  command = input("> ").lower()
  if command == "quit": 
    play_flag = False
    print("Quitting, as requested. Goodbye.")
  elif command in ["north", "south", "east", "west"]:
    current_room = current_room.move(command)
  elif command == "talk":
    if inhabitant is not None: 
      inhabitant.talk()
  elif command == "embrace":
    print("Embracing action ...")
    if inhabitant is not None:
      if isinstance(inhabitant, Friend):
        inhabitant.embrace()
      else:
        if isinstance(inhabitant, Enemy):
          print("I don't think you want to get that close to your enemy!")
        else:
          print("You don't know anything about " + inhabitant.get_description + ".")
    else:
        print("There is nobody here to embrace.")
  elif command == "use":
    print("Preparing to use ...")
    continue
    if object is not None:
      object.use(object)
    else:
      print("There is no itme here to use.")
  elif command == "return":
    print("Receiving action ...")
  elif command == "attack":
    print("Attacking action ...")
  elif command == "give":
    print("Giving action ...")
  elif command == "fight":
    print("Fighting action ...")
    if inhabitant is not None:
      weapon = input("Which weapon will you use " + str(item_list) + " > ")
      if isinstance(inhabitant, Enemy):
        if inhabitant.fight(weapon) == False: 
          play_flag = False
          print("\nYou lose, and fall to the ground. The cockroaches will party tonight!")
      else:
        nully = inhabitant.fight(weapon)
    else:
      print("Nobody here to fight.")
  else:
    print("Sorry, I don't understand your command.")
