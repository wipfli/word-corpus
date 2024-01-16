import subprocess

# downloads osm planet from https://mirror.init7.net/openstreetmap/planet/

command = f'axel -n 10 https://mirror.init7.net/openstreetmap/planet/planet-latest.osm.bz2'
print(command)
subprocess.run(command, shell=True)

command = f'bunzip2 planet-latest.osm.bz2'
print(command)
subprocess.run(command, shell=True)
