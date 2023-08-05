# Generate module from local file
A Python package to dynamically create module from local Python file.

# Install
```
pip install modgen
```
# Usage
```
import modgen
module_name = 'my_selected_module_name'
module_location = 'path/to/my/module/file.py'
modgen.create(module_name, module_location)
```
From this point you can import your file with the selected module name:
```
import my_selected_module_name
```
