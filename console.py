#!/usr/bin/python3
"""HNBNB Module"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class
    """
    prompt = "(hbnb) "
    __unique_entry = ["BaseModel"]

    def do_create(self, line):
        """Create A BaseModel Instance"""
        if line == "":
            print("** class name missing **")
        else:
            m = line.split()
            if m[0] not in self.__unique_entry:
                print("** class doesn't exist **")
            else:
                cls_inst = BaseModel()
                print(cls_inst.id)

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
