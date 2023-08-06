import importlib.util
import click
import os
from cookbook import CookBook
from shell import shell

def compile_bakefile(path):
  spec = importlib.util.spec_from_file_location("BakeFile", path)
  bakefile = importlib.util.module_from_spec(spec)
  spec.loader.exec_module(bakefile)
  return bakefile.book

@click.command()
@click.option("--file", default=f"{os.path.join(os.getcwd(), 'Bakefile.py')}", help="Path to the Bakefile")
@click.argument("recipe_list", nargs=-1)
def main(file, recipe_list):
  cookbook: CookBook = compile_bakefile(file)
  if len(recipe_list) == 0:
    print(cookbook.text())
    return
  for recipe_name in recipe_list:
    cookbook.get_recipe(recipe_name).invoke()
      
  
if __name__ == "__main__":
  main()