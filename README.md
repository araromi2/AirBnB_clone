### How to start the command interpreter

To start the command interpreter, run the following command:

```./console.py```
### How to use it

Once the command interpreter is started, you can use it to interact with the AirBnB clone simulation. The interpreter provides a number of commands that allow you to create new places, manage existing places and book reservations for places. The following commands are available:

* `create`: Creates a new instance of a class. The class name is passed as an argument to the command. The command returns the id of the new instance.
* `show`: Prints the string representation of an instance based on the class name and id.
* `destroy`: Deletes an instance based on the class name and id.
* `all`: Prints all string representation of all instances based or not on the class name.
* `update`: Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). You can also update a class attribute by passing the class name as an argument.

### Examples

#### Create a new place

```(hbnb) create Place```
#### Show a place

```(hbnb) show Place 1234-1234-1234```

#### Destroy a place

```(hbnb) destroy Place 1234-1234-1234```