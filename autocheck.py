"""                                         Автоперевірка 1

                        Теорія автоперевірки 1
                        
When speed, correctness, and a small amount of memory are essential, the pickle package is the best choice for 
serializing/deserializing Python objects.

The pickle package has two pairs of paired methods:

The first pair of methods are dumps, which pack an object into a byte string, and loads, which unpack from a byte 
string into an object.

These methods are needed when we want to control what to do with a byte representation, such as sending it over 
the network or receiving it from the network."""
import pickle

some_data = {
    (1, 3.5): 'tuple',
    2: [1, 2, 3],
    'a': {'key': 'value'}
}

byte_string = pickle.dumps(some_data)
unpacked = pickle.loads(byte_string)

print(unpacked == some_data)  # True
print(unpacked is some_data)  # False
"""
In this example, the dictionary some_data packed in byte_string is unpacked into unpacked. The unpacked is 
strictly equal to some_data, but it is still not the same object.

The second pair of methods are dump and load. They pack into a byte-writable file and unpack from a byte-readable 
file."""

import pickle

some_data = {
    (1, 3.5): 'tuple',
    2: [1, 2, 3],
    'a': {'key': 'value'}
}

file_name = 'data.bin'

with open(file_name, "wb") as fh:
    pickle.dump(some_data, fh)

with open(file_name, "rb") as fh:
    unpacked = pickle.load(fh)

print(unpacked == some_data)  # True
print(unpacked is some_data)  # False

"""
The result is similar to the previous example. The main difference is that during the execution of this code, the 
data.bin file appeared in the working folder.

                        Завдання до автоперевірки 1
                        
There is a list, each element of which is a dictionary with user contacts of the following type:

    {
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}

The dictionary contains the name of the user name, their email, phone number, and the favorite property (whether 
the contact is a favorite or not).

Implement two functions. One is for serializing and deserializing a list of contacts using the pickle package, and 
the other is for storing the resulting data in a binary file.

The first function, write_contacts_to_file, takes two parameters: filename — the file’s name, and contacts — the 
list of contacts. It saves the specified list to a file using the dump method of the pickle package.

The second function, read_contacts_from_file, reads and returns the specified list of contacts from the file 
filename using the pickle package's load method."""

import pickle

def write_contacts_to_file(filename, contacts):
    with open(filename, 'wb') as file:
        pickle.dump(contacts, file)
    return None

def read_contacts_from_file(filename):
    with open(filename, 'rb') as file:
        contacts = pickle.load(file)
    return contacts

contacts = {
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}
write_contacts_to_file('contacts.bin', contacts)
print(read_contacts_from_file('contacts.bin'))
# Виведення
# {'name': 'Allen Raymond', 'email': 'nulla.ante@vestibul.co.uk', 'phone': '(992) 914-3792', 'favorite': False}


"""                                     Автоперевірка 2

                        Теорія автоперевірки 2
                        
The JSON protocol (which stands for JavaScript Object Notation) is a prevalent transmission protocol on the Internet. 
This protocol has several advantages:

- simple, easy to implement;
- readable;
- relatively compact (there are much more economical protocols).

The first advantage made JSON universal, any modern programming language supports JSON. And if not, you can easily 
implement JSON support yourself.

JSON also has some disadvantages:

- imited set of types;
- resource-intensive (there are more resource-intensive protocols).

JSON supports the following data types:

- a record (like a dictionary in Python), only strings can be used as a key, the value can be any JSON type;
- array (like a list in Python);
- number (there is no difference between integers or fractions);
- literal (True, False, None);
- string.

As in Python, a record and an array can contain nested records and/or dictionaries of any nesting depth.

You should be careful with type conversions when working with JSON in Python. Tuples become lists when unpacked from JSON. 
Dictionary keys, if they were numbers, become strings.

Python supports JSON and comes with the json package as standard, which contains everything you need to work with JSON.

The dump and load methods save data to a writeable file and read from a readable file.

import json

some_data = {'key': 'value', 2: [1, 2, 3], 'tuple': (5, 6), 'a': {'key': 'value'}}
file_name = 'data.json'

with open(file_name, "w") as fh:
    json.dump(some_data, fh)

with open(file_name, "r") as fh:
    unpacked = json.load(fh)

unpacked is some_data  # False
unpacked == some_data  # False

unpacked['key'] == some_data['key']  # True
unpacked['a'] == some_data['a']  # True
unpacked['2'] == some_data[2]  # True
unpacked['tuple'] == [5, 6]  # True

The data.json file with the following structure will be the result:

{
  "key": "value",
  "2": [
    1,
    2,
    3
  ],
  "tuple": [
    5,
    6
  ],
  "a": {
    "key": "value"
  }
}

                        
                        Завдання до автоперевірки 2
                        
There is a list, each element of which is a dictionary with user contacts of the following type:

{
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}
The dictionary contains the name of the user name, their email, phone number, and favorite property (whether the contact 
is a favorite or not).

Develop two functions. One is for serializing and deserializing a list of contacts using a json package, and the other 
is for storing the resulting data in a text file.

The first function, write_contacts_to_file, takes two parameters: filename — the file’s name, and contacts — the list of 
contacts. It saves the specified list to a file using the dump method of the json package.

The json file structure should be as follows:

{
  "contacts": [
    {
      "name": "Allen Raymond",
      "email": "nulla.ante@vestibul.co.uk",
      "phone": "(992) 914-3792",
      "favorite": false
    },
    ...
  ]
}
That is, the list of contacts should be stored under the "contacts" key, not just save the list to a file.

The second function read_contacts_from_file reads and returns the specified list of contacts from the file filename, previously 
saved by the write_contacts_to_file function, using the load method of the json package."""

import json

def write_contacts_to_file(filename, contacts):
    with open(filename, 'w') as file:
        json.dump({"contacts": contacts}, file)
    

def read_contacts_from_file(filename):
    with open(filename, 'r') as file:
        contacts = json.load(file)["contacts"]
    return contacts


contacts = {
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}
write_contacts_to_file('contacts.json', contacts)
print(read_contacts_from_file('contacts.json'))
# Виведення
# {'name': 'Allen Raymond', 'email': 'nulla.ante@vestibul.co.uk', 'phone': '(992) 914-3792', 'favorite': False}


"""                                  Автоперевірка 3

                        Теорія автоперевірки 3
                        
Another very commonly used information exchange format is the tabular representation. The csv format is an open format 
for storing tabular data that any editor supports. The csv format is essentially the same text file, but with the condition 
that all information in it is divided into columns and rows by delimiter characters. Typically, a comma separates columns 
and rows by a newline character. But you can use any other combination of characters.

Python supports working with tabular data in the csv format. The csv package is provided as standard."""

import csv

with open('eggs.csv', 'w', newline='') as fh:
    spam_writer = csv.writer(fh)
    spam_writer.writerow(['Spam'] * 5 + ['Baked Beans'])
    spam_writer.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

with open('eggs.csv', newline='') as fh:
    spam_reader = csv.reader(fh)
    for row in spam_reader:
        print(', '.join(row))

"""
As a result of executing this code, the eggs.csv file appeared in the working folder. If you open it with a table editor, it
will open as a table.

There are two auxiliary classes in the csv package for working with tabular data that make it a little more convenient:"""

import csv

with open('names.csv', 'w', newline='') as fh:
    field_names = ['first_name', 'last_name']
    writer = csv.DictWriter(fh, fieldnames=field_names)
    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

with open('names.csv', newline='') as fh:
    reader = csv.DictReader(fh)
    print(reader.fieldnames)
    for row in reader:
        print(row['first_name'], row['last_name'])

""" The DictWriter and DictReader classes allow you to work with table rows as dictionaries, where column names (first row) 
are used as keys.

Thus, you can use Python to generate tabular data and import data from tables.

                        
                        Завдання до автоперевірки 3
                        
There is a list, each element of which is a dictionary with user contacts of the following type:

    {
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}
The dictionary contains the name of the user name, their email, phone number, and the favorite property (indicating whether the 
contact is a favorite).

Develop two functions to serialize and deserialize a list of contacts using a csv package and store the resulting data in a 
text file.

The first function write_contacts_to_file takes two parameters: filename — the name of the file, and contacts — the list of 
contacts. This function saves the specified list in a csv file.

The structure of the csv file should be as follows:

name,email,phone,favorite
Allen Raymond,nulla.ante@vestibul.co.uk,(992) 914-3792,False
Chaim Lewis,dui.in@egetlacus.ca,(294) 840-6685,False
Kennedy Lane,mattis.Cras@nonenimMauris.net,(542) 451-7038,True
Wylie Pope,est@utquamvel.net,(692) 802-2949,False
Cyrus Jackson,nibh@semsempererat.com,(501) 472-5218,True
Please note that the first line of the file contains the headers, which are the names of the keys.

The second function, read_contacts_from_file, reads, converts, and returns the specified list of contacts from the file filename 
saved earlier by the `write_contacts_to_file function.

Notice. When reading a csv file, we get the favorite dictionary property as a string, i.e., for example, favorite='False'. You need 
to convert it back to a logical expression to make it favorite=False."""

import csv


def write_contacts_to_file(filename, contacts):
    with open(filename, 'w', newline='') as file:
        fieldnames = ['name', 'email', 'phone', 'favorite']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for contact in contacts:
            writer.writerow(contact)
    

def read_contacts_from_file(filename):
    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)
        contacts = []
        for row in reader:
            row['favorite'] = True if row['favorite'] == 'True' else False
            contacts.append(row)
    return contacts
contacts =[ 
            {"name": "Allen Raymond","email": "nulla.ante@vestibul.co.uk", "phone": "(992) 914-3792", "favorite": False},
            {"name": "Chaim Lewis","email": "dui.in@egetlacus.ca", "phone": "(294) 840-6685", "favorite": False},
            {"name": "Kennedy Lane","email": "mattis.Cras@nonenimMauris.net", "phone": "(542) 451-7038", "favorite": True},
            {"name": "Wylie Pope","email": "est@utquamvel.net", "phone": "(692) 802-2949", "favorite": False},
            {"name": "Cyrus Jackson","email": "nibh@semsempererat.com", "phone": "(501) 472-5218", "favorite": True},
]
write_contacts_to_file('contacts.csv', contacts)
print(read_contacts_from_file('contacts.csv'))
# Виведення
# [{'name': 'Allen Raymond', 'email': 'nulla.ante@vestibul.co.uk', 'phone': '(992) 914-3792', 'favorite': False}, 
# {'name': 'Chaim Lewis', 'email': 'dui.in@egetlacus.ca', 'phone': '(294) 840-6685', 'favorite': False}, 
# {'name': 'Kennedy Lane', 'email': 'mattis.Cras@nonenimMauris.net', 'phone': '(542) 451-7038', 'favorite': True}, 
# {'name': 'Wylie Pope', 'email': 'est@utquamvel.net', 'phone': '(692) 802-2949', 'favorite': False}, 
# {'name': 'Cyrus Jackson', 'email': 'nibh@semsempererat.com', 'phone': '(501) 472-5218', 'favorite': True}]



"""                                     Автоперевірка 4
                        
                        Теорія автоперевірки 4
                        
                        
You can save objects for later use, but only if the class itself has been declared earlier in the code where the unpacking 
takes place. This is necessary so that pickle can correctly save and then unpack a packed class object.

import pickle


class Human:
    def __init__(self, name):
        self.name = name


bob = Human("Bob")
encoded_bob = pickle.dumps(bob)

decoded_bob = pickle.loads(encoded_bob)

bob.name == decoded_bob.name  # True
However, if you wanted to transfer a bob object over the network to another computer that doesn't know anything about the 
Human class, you would receive an error. If the Human class is declared at both ends of the communication channel, then such 
an interaction will work.

                        Завдання до автоперевірки 4
                        
Develop the Person class. It has four properties: the user's name, their email, phone number phone, and the favorite property 
(indicating whether the contact is a favorite).

An example of creating a class instance:

    Person(
    "Allen Raymond",
    "nulla.ante@vestibul.co.uk",
    "(992) 914-3792",
    False,
)
Develop the Contacts class. It must initialize two properties through the constructor: filename — the name of the file for packing 
an object of the Contacts class, contacts — a list of contacts, and instances of the Person class.

An example of creating a class instance:

contacts = [
    Person(
        "Allen Raymond",
        "nulla.ante@vestibul.co.uk",
        "(992) 914-3792",
        False,
    ),
    Person(
        "Chaim Lewis",
        "dui.in@egetlacus.ca",
        "(294) 840-6685",
        False,
    ),
]

persons = Contacts("user_class.dat", contacts)
Develop two methods for serializing and deserializing an instance of the Contacts class using the pickle package and 
storing data in a binary file.

The first method, save_to_file, saves an instance of the Contacts class to a file using the dump method of the pickle 
package. The file name is stored in the filename attribute.

The second method, read_from_file, reads and returns an instance of the Contacts class from the file filename using the 
load method of the pickle package.

Example:

persons = Contacts("user_class.dat", contacts)
persons.save_to_file()
person_from_file = persons.read_from_file()
print(persons == person_from_file)  # False
print(persons.contacts[0] == person_from_file.contacts[0])  # False
print(persons.contacts[0].name == person_from_file.contacts[0].name)  # True
print(persons.contacts[0].email == person_from_file.contacts[0].email)  # True
print(persons.contacts[0].phone == person_from_file.contacts[0].phone)  # True                        """

import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite
          
        
class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
            

    def save_to_file(self):
        with open(self.filename, 'wb') as file:
            pickle.dump(self, file)
            
        

    def read_from_file(self):
        with open(self.filename, 'rb') as file:
            contacts = pickle.load(file)
        return contacts

contacts = [
    Person(
        "Allen Raymond",
        "nulla.ante@vestibul.co.uk",
        "(992) 914-3792",
        False,
    ),
    Person(
        "Chaim Lewis",
        "dui.in@egetlacus.ca",
        "(294) 840-6685",
        False,
    ),
]
persons = Contacts("user_class.dat", contacts)
persons.save_to_file()
person_from_file = persons.read_from_file()
print(persons == person_from_file)  # False
print(persons.contacts[0] == person_from_file.contacts[0])  # False
print(persons.contacts[0].name == person_from_file.contacts[0].name)  # True
print(persons.contacts[0].email == person_from_file.contacts[0].email)  # True
print(persons.contacts[0].phone == person_from_file.contacts[0].phone)  # True  
print(persons.contacts[0].favorite == person_from_file.contacts[0].favorite)  # True


    