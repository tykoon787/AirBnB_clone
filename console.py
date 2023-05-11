#!/usr/bin/python3
import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity
from models import storage

class HBNBCommand(cmd.Cmd):
    """
    CLI for AirBnB
    """
    prompt = "(hbnb) "
    def do_create(self, class_name):
        """
        Creates a new instance of BaseMOdel, saves it json and prints the id

            Parameters:
                class_name (string) : A class name that will be instantiated to an object
        """
        if class_name:
            if class_name in globals():
                cls = globals()[class_name]
                new_obj = cls()
                new_obj.save()
                print(new_obj.id)
            else:
                print(" ** Class doesn't exist ** ")
        else:
            print(" ** Class name missing **")

    def do_show(self, arg):
        """
        Prints the string representation of an object based on the Class Name and ID
        """
        if arg:
            args = arg.split()
            try:
                cls = globals()[args[0]]
                try:
                    if args[1]:
                        name_id = args[0] + "." + args[1]
                        # storage.reload()
                        file_data = storage.all()
                        for key, value in file_data.items():
                            if key == name_id:
                                print(value)
                                return
                        print(" ** No Instance found **")
                    else:
                        print(" ** Instance id missing ** ")
                except IndexError:
                    print("** Instance id missing **")
            except KeyError:
                print("** Class doesn't exist **") 
        else:
            print("** Class Name missing ** ")
         
    def do_destroy(self, arg):
        """
        deletes an instance based on name and id
        updates the changes to the JSON file
        """
        if arg:
            args = arg.split()
            try:  # check if class name exits
                cls = globals()[args[0]]
                try:
                    if args[1]:
                        name_id = args[0] + "." + args[1]
                        # storage.reload()
                        file_data = storage.all()
                        if name_id in file_data:
                            print("Deleting {}".format(name_id))
                            del file_data[name_id] 
                            storage.save()
                        else:
                            print("** no instance found **")
                except IndexError:
                    print("** Instance id missing **")
            except KeyError:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and ID by adding or updating attributes
        The changes are saved to the json file
        """
        # Check if class_name is present
        if arg:
            args = shlex.split(arg)
            # id not present
            if len(args) == 1:
                print(" ** instance id missing **")
                return
            # attr_name not present
            elif len(args) == 2:
                print(" ** attribute name missing **")
                return
            # attr_value not present
            elif len(args) == 3:
                print(" ** attribute value missing **")
                return
            else: 
                class_name = args[0]
                id = args[1]
                attr_name = args[2]
                try:
                    # Conversion to Int
                    attr_value = int(args[3])
                except ValueError:
                    try:
                        # Conversion to a float
                        attr_value = float(args[3])
                    except ValueError:
                        # Defaulting to string value
                        attr_value = args[3]

                # print("Type of arg[3] {}".format(type(attr_value)))
                if class_name not in globals():
                    print(" ** class doesn't exist ** ")
                    return
                else:
                    name_id = class_name + "." + id            
                    reloaded_data = storage.all()
                    for key, value in reloaded_data.items():
                        if key == name_id:
                            # Set an attribute to the object
                            setattr(value, attr_name, attr_value)
                            # Save
                            storage.save()
                            return
                    print(" ** no instance found ** ")
        else:
            print(" ** class name missing ** ")
            return
        
    def do_all(self, arg):
        """_summary_

        Args:
            arg (_type_): _description_
        """
        data_list = []
        if arg:
           try:
                class_name = globals()[arg] 
                print("Class_name ==> {}".format(class_name))
                file_data = storage.all()
                for key, value in file_data.items():
                    if type(value) == class_name:
                        # Append list
                        data_list.append(value.__str__())
           except KeyError:
                print(" ** class doesn not exist **")
        else:
            file_data = storage.all()
            for key, value in file_data.items():
                # Append list
                data_list.append(value.__str__())
        print(data_list)

    def emptyline(self):
            """console to execute nothing when you press enter without an argument"""
            pass

    def do_quit(self, line):
        """
        Exit CLI
        """
        return True

    def do_EOF(self, line):
        """
        Handles EOF, or Exits
        """
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()