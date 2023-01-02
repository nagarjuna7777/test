import subprocess
cmd = 'dir c:\ -Recurser'.split()
sp = subprocess.Popen(cmd,shell=False,stderr=subprocess.PIPE,stdout=subprocess.PIPE,universal_newlines=True)
sp.wait()
o,e=sp.communicate()
print(o.splitlines())
print(e.splitlines())
