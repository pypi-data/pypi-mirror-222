# Import local module
A Python package to dynamically import local Python modules.

It let's you import modules from Python files sitting anywhere.

```
module_name = 'my_selected_module_name'
module_location = 'path/to/my/module/file.py'
import_local_module(module_name, module_location)

import my_selected_module_name
```