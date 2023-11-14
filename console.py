#!/usr/bin/python3
"""HNBNB Module"""
import cmd
from models import storage
from models.amenity import Amenity
from models.basemodel import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class
    """
    prompt = "(hbnb) "
    __unique_entry = ("Amenity", "BaseModel",
                      "City", "Place", "Review", "State",  "User")
    __unique_attr = ("id", "created_at", "updated_at")

    def do_create(self, line):
        """Create A BaseModel Instance"""
        if line == "":
            print("** class name missing **")
        else:
            word_count = line.split()
            if word_count[0] not in self.__unique_entry:
                print("** class doesn't exist **")
            else:
                cls_inst = ""
                if word_count[0] == "BaseModel":
                    cls_inst = BaseModel()
                elif word_count[0] == "User":
                    cls_inst = User()
                elif word_count[0] == "Amenity":
                    cls_inst = Amenity()
                elif word_count[0] == "City":
                    cls_inst = City()
                elif word_count[0] == "Place":
                    cls_inst = Place()
                elif word_count[0] == "Review":
                    cls_inst = Review()
                elif word_count[0] == "State":
                    cls_inst = State()
                storage.new(cls_inst)
                cls_inst.save()
                print(cls_inst.id)

    def do_show(self, line):
        """
        do_show method prints the string representation
        """
        if line == "":
            print("** class name missing **")
        else:
            word_count = line.split()
            if word_count[0] not in self.__unique_entry:
                print("** class doesn't exist **")
            elif len(word_count) == 1:
                print("** instance id missing **")
            elif len(word_count) == 2:
                storage_key = storage.all()
                inst_key = f"{word_count[0]}.{word_count[1]}"
                if inst_key in storage_key.keys():
                    print(storage_key[inst_key])
                else:
                    print("** no instance found **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the classname and id
        """
        if line == "":
            print("** class name missing **")
        else:
            word_count = line.split()
            if word_count[0] not in self.__unique_entry:
                print("** class doesn't exist **")
            elif len(word_count) == 1:
                print("** instance id missing **")
            elif len(word_count) == 2:
                storage_key = storage.all()
                inst_key = f"{word_count[0]}.{word_count[1]}"
                if inst_key in storage_key.keys():
                    del storage_key[inst_key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name.
        """
        storage_key = storage.all()
        if line == "":
            for val in storage_key.values():
                print(val)
        else:
            word_count = line.split()
            if word_count[0] not in self.__unique_entry:
                print("** class doesn't exist **")
            else:
                for val in storage_key.values():
                    if val.__class__.__name__ == word_count[0]:
                        print(val)

    def do_update(self, line):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute
        """
        storage_data = storage.all()
        if line == "":
            print("** class name missing **")
        else:
            wordcount = line.split()
            inst_check = ""
            if wordcount[0] not in self.__unique_entry:
                print("** class doesn't exist **")
            else:
                if len(wordcount) == 1:
                    print("** instance id missing **")
                elif len(wordcount) == 2:
                    print("** attribute name missing **")
                elif len(wordcount) == 3:
                    print("** value missing **")
                else:
                    inst_check = f"{wordcount[0]}.{wordcount[1]}"
                    if inst_check not in storage_data.keys():
                        print("** no instance found **")
                        return False
                    elif wordcount[2] in self.__unique_attr:
                        print(f"** cannot update class attribute\
                                                        \"{wordcount[2]}\"")
                        return False
                    else:
                        storage_value = storage_data[inst_check]
                        try:
                            if wordcount[2] == "password":
                                raise NameError
                            if (type(eval(wordcount[3])) == int) or (
                            type(eval(wordcount[3])) == float):
                                storage_value.__dict__[wordcount[2]] = (
                                eval(wordcount[3]))
                        except NameError:
                            if wordcount[2] == "amenity_ids":
                                storage_value.__dict__[wordcount[2]].append(
                                        wordcount[3])
                            else:
                                storage_value.__dict__[wordcount[2]] = (
                                wordcount[3])
                    storage.new(storage_data[inst_check])
                    storage.save()

    def do_quit(self, line):
        """Exit the Programme"""
        print("Left the HBNBCommand Shell")
        return True

    def do_EOF(self, line):
        """Exit the Programme"""
        print("Left the HBNBCommand Shell")
        return True

    def emptyline(self):
        return False


if __name__ == "__main__":
    HBNBCommand().cmdloop()
