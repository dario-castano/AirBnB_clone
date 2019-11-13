# Holberton's hBnB: An "AirBnB" clone
This is the repository for the AirBnB clone made for Holberton School.

## Included files:
|Name | Description |
|-----|-------------|
| models/engine/file_storage.py | FileStorage class | 
| models/amenity.py | Amenity class |  
| models/base_model.py | BaseModel class|  
| models/city.py | City class |   
| models/place.py | Place class |   
| models/review.py | Review class |   
| models/state.py | State class |   
| models/user.py | User class |   
| tests/test_console.py | Test suite for the console |   
| tests/test_models/test_amenity.py | Amenity class (test) |   
| tests/test_models/test_base_model.py | BaseModel class (test) |   
| tests/test_models/test_city.py | City class (test) |    
| tests/test_models/test_place.py | Place class (test) |   
| tests/test_models/test_review.py | Review class (test) |   
| tests/test_models/test_state.py | State class (test) |   
| tests/test_models/test_user.py | User class (test) |   
| tests/test_models/test_engine/test_file_storage.py | FileStorage class (test) |   
| AirBnB.mdj | UML Class Diagram (StarUML) | 
| console.py | Main file - entry point |
| cmd_parser.py | Command parser (CMDParser) |
| AUTHORS | Authors file | 
| LICENSE | License file | 
| README.md | README - This file | 

## Phase 1: The console
This is the first part of the application. Closely related to the backend, the console allow us to run
a wide number of operations without the need to alter data using databases or some kind of file storage.

### A little review
The console allow us to run CRUD operations on the model by two different syntaxes:
+ Simple syntax:

``` <operation> <class> <id> <attr-name> "<attr-value>"```

+ Dot syntax (composite): 

``` <class>.<operation>(<parameters>)```

You can use these kinds anyway you like. You have to take into account that some operations
does not include some parameters.

You can take a look to our _syntax guide_ if you want
to see some details about a specific operation.

#### Installation
Please clone this repo and be sure you have python 3.4 or greater installed.
For MacOS, you can use Homebrew or MacPorts. On Linux, you can install python3 using 
the package manager your distribution uses (apt, yum, zypper, etc...). On BSD you can use
the ports tree or a pkg application. On haiku, please use hpkg to install python.

#### Start
There are two ways to run the console: running like an executable file or calling python3 to
run the console.py file:

+ Run directly
```./console.py```

+ Calling python
```python3 console.py```

If you are using newer Macs or BSD, please call python3 because the console executable 
looks for python3 in /usr/bin instead of /usr/local/bin.

Next, you should see a command prompt. This tells us the console are ready to run operations.

```
$ ./console.py 
(hbnb)  
```

#### Basic commands
##### quit

Usage: ```quit```

Exits the console

##### help

Usage: ```help <topic>```

Without parameters, shows a list of commands or operations who has a little
description.

```
$ ./console.py 
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
```

With topic, shows the description about the given topic

```
(hbnb) help all

        all - Prints all string representation of all instances
        based or not on the class name
```

Now, we are going to see the syntax of the CRUD operations:

#### Syntax Guide
##### all

Usage: ```all``` , ```<class>.all()``` or ```all <class>```

Prints all string representation of all instances based or not on the class name.

Without parameters, shows all objects stored in the JSON-string persistence layer

```
(hbnb) all
["[BaseModel] (73d57b87-4665-48a0-bf8d-c4840472188e) {'id': '73d57b87-4665-48a0-bf8d-c4840472188e', 'created_at': date
time.datetime(2019, 11, 12, 23, 14, 50, 239444), 'updated_at': datetime.datetime(2019, 11, 12, 23, 14, 50, 239464)}", 
"[User] (b8504ad5-bd0b-413a-883d-bdb43ada290b) {'id': 'b8504ad5-bd0b-413a-883d-bdb43ada290b', 'created_at': datetime.
datetime(2019, 11, 12, 23, 15, 0, 624053), 'updated_at': datetime.datetime(2019, 11, 12, 23, 15, 0, 624085)}", "[User]
 (e5b478b7-51e7-4118-b163-8ca88106fdf5) {'id': 'e5b478b7-51e7-4118-b163-8ca88106fdf5', 'created_at': datetime.datetime
(2019, 11, 12, 23, 15, 1, 871272), 'updated_at': datetime.datetime(2019, 11, 12, 23, 15, 1, 871285)}"]

```

With parameter, shows all objects of the given class

```
(hbnb) BaseModel.all()
["[BaseModel] (73d57b87-4665-48a0-bf8d-c4840472188e) {'id': '73d57b87-4665-48a0-bf8d-c4840472188e', 'created_at': date
time.datetime(2019, 11, 12, 23, 14, 50, 239444), 'updated_at': datetime.datetime(2019, 11, 12, 23, 14, 50, 239464)}"]
```

```
(hbnb) all User
["[User] (b8504ad5-bd0b-413a-883d-bdb43ada290b) {'id': 'b8504ad5-bd0b-413a-883d-bdb43ada290b', 'created_at': datetime
.datetime(2019, 11, 12, 23, 15, 0, 624053), 'updated_at': datetime.datetime(2019, 11, 12, 23, 15, 0, 624085)}", "[User]
 (e5b478b7-51e7-4118-b163-8ca88106fdf5) {'id': 'e5b478b7-51e7-4118-b163-8ca88106fdf5', 'created_at': datetime.datetime
(2019, 11, 12, 23, 15, 1, 871272), 'updated_at': datetime.datetime(2019, 11, 12, 23, 15, 1, 871285)}"]
```

##### count

Usage: ```<class>.count()``` or ```count <class>```

Count the total objects of a given class

```
(hbnb) count User
2
```

```
(hbnb) User.count()
2
```

##### create

Usage: ```<class>.create()``` or ```create <class>```

Creates a new instance of the class, saves it (to the JSON file) and prints the id.

```
(hbnb) City.create()
c3cc63b3-047c-4366-91b4-da34289004e3
```

```
(hbnb) create Review
40c9a0ba-dc9c-4190-8ac9-ba0ca3f1c819
```

##### destroy

Usage: ```<class>.destroy(<id>)``` or ```destroy <class> <id>```

Deletes an instance based on the class name and id. This operation deletes the data
inside the JSON storage file.

```
(hbnb) Review.destroy(40c9a0ba-dc9c-4190-8ac9-ba0ca3f1c819)
(hbnb)
```

```
(hbnb) destroy City c3cc63b3-047c-4366-91b4-da34289004e3
(hbnb) 
```

##### show

Usage: ```<class>.show(<id>)``` or ```show <class> <id>```

Prints the string representation of an instance based on the class name and id.

```
(hbnb) State.show(29812026-12a5-44fe-a3c0-d81511900b10)
[State] (29812026-12a5-44fe-a3c0-d81511900b10) {'id': '29812026-12a5-44fe-a3c0-d81511900b10', 'created_at': datetime.
datetime(2019, 11, 12, 23, 51, 38, 522386), 'updated_at': datetime.datetime(2019, 11, 12, 23, 51, 38, 522420)}
```

```
(hbnb) show Amenity bc275c25-49b3-4cd0-96ae-a74544425889
[Amenity] (bc275c25-49b3-4cd0-96ae-a74544425889) {'id': 'bc275c25-49b3-4cd0-96ae-a74544425889', 'created_at': datetime
.datetime(2019, 11, 12, 23, 53, 12, 73787), 'updated_at': datetime.datetime(2019, 11, 12, 23, 53, 12, 73822)}
```

##### update

Usage: ```<class>.update(<id>, <attribute>, "<value>")```,

```<class>.update(<id>, <dictionary>)```,

```update <class> <id> <attribute> "<value>"```

Updates an instance based on the class name and id by adding or 
updating attribute (save the change into the JSON file).

NOTE: Please enclose attributes and values in double quotes. It allows to add
names separated by spaces.
```
(hbnb) User.update(b8504ad5-bd0b-413a-883d-bdb43ada290b, "name", "Donald de Jesus")
(hbnb)
```
If you want to pass a dictionary as a parameter, you can do it this way:
```
(hbnb) User.update(b8504ad5-bd0b-413a-883d-bdb43ada290b, {'name': 'Palomo Usuriaga', 'car': 'Dodge'})
(hbnb) 
```
But if you only want to change a value, you could to this way:
```
(hbnb) update User b8504ad5-bd0b-413a-883d-bdb43ada290b name "Rigoberto Uran"
(hbnb)
```

### Authors
Dario Castaño <dario.castano@aim.com>

SantiagoHerreG <888@holbertonschool.com>
