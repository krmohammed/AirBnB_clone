#!/usr/bin/python3
"""
console module
"""
import cmd
import re
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    AirBnB Console
    Create a new object (ex: a new User or a new Place)
    Retrieve an object from a file, a database etc…
    Do operations on objects (count, compute stats, etc…)
    Updates attributes of an object
    Destroys an object
    """

    prompt = "(hbnb) "
    __my_models = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
    __missing_class_name = "** class name missing **"
    __wrong_class = "** class doesn't exist **"
    __no_instance = "** no instance found **"
    __no_id = "** instance id missing **"

    def do_quit(self, line):
        """exit the cmd
        """
        return True

    def do_EOF(self, line):
        """same as quit, exit
        """
        return True

    def emptyline(self):
        """overrides the emptyline method
        """
        pass

    def do_create(self, line):
        """
        Creates a new instance of BaseModel
        saves it (to a JSON file) and prints the id
        """
        if line:
            lines = line.split()
            if lines[0] in self.__my_models:
                new_instance = eval(f"{lines[0]}()")
                new_instance.save()
                print(new_instance.id)
            else:
                print(self.__wrong_class)
        else:
            print(self.__missing_class_name)

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id
        Usage: $ show <class name> <id>
        """
        if line:
            lines = line.split()
            if lines[0] in self.__my_models:
                if len(lines) > 1:
                    classes = storage.all()
                    class_key = f"{lines[0]}.{lines[1]}"
                    if class_key in classes:
                        print(classes[class_key])
                    else:
                        print(self.__no_instance)
                else:
                    print(self.__no_id)
            else:
                print(self.__wrong_class)
        else:
            print(self.__missing_class_name)

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        (saves the change into the JSON file).
        Usage: $ destroy <class name> <id>
        """
        if line:
            lines = line.split()
            if lines[0] in self.__my_models:
                if len(lines) > 1:
                    classes = storage.all()
                    class_key = f"{lines[0]}.{lines[1]}"
                    if class_key in classes:
                        storage.destroy(class_key)
                        storage.save()
                    else:
                        print(self.__no_instance)
                else:
                    print(self.__no_id)
            else:
                print(self.__wrong_class)
        else:
            print(self.__missing_class_name)

    def do_all(self, line):
        """
        Prints all string representation of all instances based
        or not on the class name.
        Usage: $ all <class name>
        """
        all_str_rep = []
        if line:
            lines = line.split()
            if lines[0] in self.__my_models:
                for key, value in storage.all().items():
                    if lines[0] == key.split(".")[0]:
                        all_str_rep.append(value.__str__())
            else:
                print(self.__wrong_class)
                return
        else:
            for value in storage.all().values():
                all_str_rep.append(value.__str__())
        if all_str_rep:
            print(all_str_rep)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        (saves the change into the JSON file).
        Usage: $ update <class name> <id> <attribute name> "<attribute value>"
        """
        if line:
            lines = line.split()
            if len(lines) == 1:
                if lines[0] not in self.__my_models:
                    print(self.__wrong_class)
                else:
                    print(self.__no_id)
                return
            if len(lines) == 2:
                key = f"{lines[0]}.{lines[1]}"
                if key not in storage.all().keys():
                    print(self.__no_instance)
                else:
                    print("** attribute name missing **")
                return
            if len(lines) == 3:
                print("** value missing **")
            else:
                key = f"{lines[0]}.{lines[1]}"
                classes = storage.all()
                obj = classes[key]
                inst = obj
                try:
                    val = eval(lines[3])
                    try:
                        val = eval(val)
                    except:
                        pass
                    setattr(inst, lines[2], val)
                    inst.save()
                except:
                    pass
        else:
            print(self.__missing_class_name)

    def precmd(self, line):
        """overrides the precmd method
        """
        comm = re.match(r'(.+)\.(.+)\(([^)]*)\)', line)
        if comm is not None:
            comms = list(comm.groups())
        else:
            comms = None
        if comms and len(comms) > 0:
            a = [i.strip() for i in comms[2].split(",")]
            if comms[1] == "count":
                classes = storage.all()
                insts = [i for i in classes.keys() if i.startswith(comms[0])]
                print(len(insts))
                return ""
            if a[0]:
                b = [eval(i) for i in a]
            else:
                b = ['']
            return " ".join([comms[1], comms[0]] + b)
        return line


if __name__ == "__main__":
    HBNBCommand().cmdloop()
