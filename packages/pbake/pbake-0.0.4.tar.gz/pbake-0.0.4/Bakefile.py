from bake import CookBook
import subprocess

book = CookBook(__file__)

@book.recipe("release")
def release():
  """Run the release script"""
  subprocess.run("rm -rf dist", shell=True)
  subprocess.run("python3 -m pip install twine build", shell=True)
  subprocess.run("python3 -m build", shell=True)
  subprocess.run("python3 -m twine upload dist/*", shell=True)