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


