import subprocess

def shell(cmd, **kwargs):
  return subprocess.run(cmd, shell=True, **kwargs)