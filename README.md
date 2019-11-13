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
run the console.py file

+ Run directly
```./console.py```

+ Calling python
```python3 console.py```

If you are using newer Macs or BSD, please call python3 because the console executable 
looks for python3 in /usr/bin instead of /usr/local/bin.

Next, you should see a command prompt. This tells us the console are ready to run operrations.

```
$ ./console.py 
(hbnb)  
```

