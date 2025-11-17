📌 README.md – Python: Everything is Object
📖 Introduction

This project explores one of the most fundamental concepts in Python: everything is an object.
Understanding how Python handles objects, references, mutability, identity, and assignments is essential for writing correct and efficient code.
This project is different from others because most tasks are conceptual: you must reason about how Python behaves internally rather than writing scripts.

🧠 Concepts Covered
🔹 Objects

In Python, every value is an object: integers, strings, lists, functions, classes, and even modules.
Each object has:

a type

an identifier (memory address in CPython)

a value

🔹 References and Assignment

Variables do not hold data directly.
They hold references to objects stored in memory.

Example:

a = 89
b = a


a and b both reference the same integer object 89.

🔹 Mutable vs Immutable Objects
Immutable objects

They cannot be modified after creation.
Examples:

int

float

str

tuple

bool

Any operation that seems to “modify” them actually creates a new object:

a = 1
a += 1   # new object is created

Mutable objects

They can be changed in place.
Examples:

list

dict

set

Example:

l1 = [1, 2, 3]
l2 = l1
l1.append(4)
# Both refer to the same updated object

🔹 Identity vs Equality
Operator	Meaning
==	Compare values
is	Compare identity (same object in memory)

Example:

s1 = "Best"
s2 = "Best"
s1 == s2   # True
s1 is s2   # Might be True due to interning, but not guaranteed

🔹 Python Passing Variables to Functions

Python uses pass-by-assignment:

Functions receive a reference to the object.

If the object is mutable, modifications inside the function affect the caller.

If the object is immutable, modification creates a new object and does not affect the caller.

Examples:

Immutable:

def inc(n):
    n += 1

a = 1
inc(a)
# a stays 1


Mutable:

def inc(lst):
    lst.append(4)

l = [1, 2, 3]
inc(l)
# l becomes [1, 2, 3, 4]

🔹 Aliasing

Two variables are aliases when they reference the same object.

l1 = [1, 2, 3]
l2 = l1


Modifying l1 will affect l2.

🔹 Cloning Lists

To create a new list object:

copy = a_list[:]       # slicing
# or
copy = list(a_list)

📝 Project Structure

Each .txt file contains one line answer with:

No spaces before or after

No shebang

Ending with a newline

Example directories:

0-answer.txt
1-answer.txt
…
19-copy_list.py


Python file 19-copy_list.py must be 3 lines max and cannot import modules.

🎯 Learning Objectives Summary

By completing this project, students will be able to explain:

What objects are in Python

Differences between classes and instances

Mutable vs immutable types

What a reference is and how assignment works

How to check if two variables refer to the same object

How to get type and id of an object

What aliasing is

How Python passes arguments to functions

Behavior differences with mutable and immutable objects

🖥️ Requirements

Python 3.8.5 (Ubuntu 20.04)

pycodestyle 2.7.*

All files executable

README.md required

.txt answers: one line only, no extra space

📝 Blog Post (Task 29)

You must write a blog post on:

Medium or LinkedIn

In English

With examples and at least one picture

Topics required:

Introduction

id() and type()

Mutable objects

Immutable objects

Why this distinction matters

How Python passes arguments and implications

You will then add the final URLs at the end of the project task.

✅ Conclusion

Understanding that everything is an object helps avoid bugs related to references and mutable types.
These concepts are fundamental for writing clean, predictable Python code and are frequently tested in technical interviews.