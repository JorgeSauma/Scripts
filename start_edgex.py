import subprocess

subprocess.call(["sudo", "docker-compose", "up", "-d", "volume"])
subprocess.call(["sudo", "docker-compose", "up", "-d", "portainer"])
subprocess.call(["sudo", "docker-compose", "up", "-d", "consul"])
subprocess.call(["sudo", "docker-compose", "up", "-d", "mongo"])
subprocess.call(["sudo", "docker-compose", "up", "-d", "config-seed"])
subprocess.call(["sudo", "docker-compose", "up", "-d", "logging"])
subprocess.call(["sudo", "docker-compose", "up", "-d", "notifications"])
subprocess.call(["sudo", "docker-compose", "up", "-d", "rulesengine"])
subprocess.call(["sudo", "docker-compose", "up", "-d", "data"])
subprocess.call(["sudo", "docker-compose", "up", "-d", "export-client"])
subprocess.call(["sudo", "docker-compose", "up", "-d", "export-distro"])
subprocess.call(["sudo", "docker-compose", "up", "-d", "metadata"])
subprocess.call(["sudo", "docker-compose", "up", "-d", "scheduler"])
subprocess.call(["sudo", "docker-compose", "up", "-d", "command"])
subprocess.call(["sudo", "docker-compose", "up", "-d", "device-virtual"])

