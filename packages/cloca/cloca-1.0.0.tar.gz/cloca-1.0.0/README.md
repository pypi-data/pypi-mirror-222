### cloca - Global Clock Python Library

[![License](https://img.shields.io/badge/license-GPL%203.0-blue.svg)](https://www.gnu.org/licenses/gpl-3.0.en.html)

cloca is a simple Python library that provides a global clock with functionalities to increment time, read the current time, and reset the clock. It is designed to be used across multiple modules, ensuring they all share the same state.

### Features

- Global clock with manual time incrementation.
- Read the current time from anywhere in your Python project.
- Reset the clock to zero as needed.

### Installation

You can install cloca using pip:

```
pip install cloca
```

### Usage

#### Importing cloca

```python
from cloca import increase, now, reset
```

#### Increasing Time

Use the `increase` function to manually increment the global clock time by a specified amount.

```python
# Increase time by 5 units
increase(5)
```

#### Reading Current Time

Use the `now` function to get the current time from anywhere in your project.

```python
current_time = now()
print(f"Current time: {current_time}")
```

#### Resetting the Clock

You can reset the global clock to zero using the `reset` function.

```python
reset()
```

### Example

Here's a simple example showcasing the usage of cloca:

```python
from cloca import increase, now

# Increase time by 10 units
increase(10)

# Read the current time
current_time = now()
print(f"Current time: {current_time}")

# Reset the clock to zero
reset()

# Read the time after resetting
current_time = now()
print(f"Current time after reset: {current_time}")
```

### About the Name

The name "cloca" comes from the Latin word "clocca" (also spelled "cloca"), which means "bell." In this context, it represents a bell-like timekeeping mechanism. Just like a bell that rings to mark the passing of time, cloca acts as a global clock to manage time in Python projects.

### License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

### Contributing

Contributions to cloca are welcome! Feel free to open issues and submit pull requests for any bug fixes or new features.

### Issues

If you encounter any problems or have questions, please feel free to open an issue [here](https://github.com/ahmad-siavashi/cloca/issues).

### Acknowledgments

This project was inspired by the need for a simple global clock for Python projects.


---

Thank you for using cloca! We hope this library simplifies time management in your Python projects. If you have any feedback or suggestions, please let us know. Happy coding!