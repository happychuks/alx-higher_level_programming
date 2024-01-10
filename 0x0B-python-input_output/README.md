# Python File Input/Output Documentation

## Introduction

Python provides powerful tools for reading from and writing to files. This documentation covers the basics of file input and output operations in Python.

## Reading from Files

### Using `open()` Function

The `open()` function is used to open a file. The first parameter is the file name, and the second parameter is the mode (e.g., "r" for read, "w" for write).

```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

## Writing Files in Python
### Using `open()` Function for Writing

To write to a file, use the `open()` function with the mode set to "w" (write).

```python
with open("output.txt", "w") as file:
    file.write("This is a sample text.")
```

## Appending files

Appending to files in Python is a common operation for adding new content to an existing file without overwriting its existing content. This documentation covers the basics of appending to files.

### Using `open()` Function for Appending

To append content to an existing file, use the `open()` function with the mode set to "a" (append).

```python
with open("output.txt", "a") as file:
    file.write("This is additional text.")
```
