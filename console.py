import cmd
from models.base_model import BaseModel
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
                if args[1]:
                    name_id = args[0] + "." + args[1]
                    storage.reload()
                    file_data = storage.all()
                    for key, value in file_data.items():
                        if key == name_id:
                            print(value)
                            return
                    print(" ** No Instance found **")
                else:
                    print(" ** Instance id missing ** ")
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
                if len(args) == 1:
                    print("** instance id missing **")
                else:
                    name_id = args[0] + "." + args[1]
                    storage.reload()
                    file_data = storage.all()
                    if name_id in file_data:
                        print("Deleting {}".format(name_id))
                        del file_data[name_id] 
                        storage.save()
                    else:
                        print("** no instance found **")
            except KeyError:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and ID by adding or updating attribute
        The changes are saved to the json file
        """
        if arg:
            args = arg.split() 
            if len(args) < 4:
                print(" ** Usage: do_update <class_name> <id> <attr_name> <attr_value>")
                return
            
            class_name = args[0]
            id = args[1]
            attr_name = args[2]
            attr_value = args[3]

            if class_name not in globals():
                print(" ** Class does not exist ** ")
                return
            else:
                name_id = class_name + "." + id
                storage.reload()
                # Store reloaded data
                reloaded_data = storage.all()
                for key, value in reloaded_data.items():
                    if key == name_id:
                        instance_dict = value
                        # Add the attibute name to the dictionary and its value
                        instance_dict[attr_name] = attr_value
                        # Save the file
                        storage.save()
                        break
                    else:
                        print(" ** Key not found ** ")

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