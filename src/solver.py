from importlib import util

def load_file(name, path):
    spec = util.spec_from_file_location(name, path)
    module = util.module_from_spec(spec)
    print(module)
    spec.loader.exec_module(module)
    return module
  
print(" Programer_1_date_1: solver created to solve a simple case")
print(" Programer_1_date_1:  version 1.0 of solver")
print(" Programer_1_date_50: version 2.0 of solver")

feature1 = load_file('foo', './foo.py')