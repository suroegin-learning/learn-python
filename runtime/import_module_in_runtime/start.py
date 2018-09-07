import sys

module_names = [
    'package.app',
]

for module_name in module_names:
    exec(f"from {module_name} import *")

print_ts()