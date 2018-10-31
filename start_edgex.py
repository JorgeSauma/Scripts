import subprocess

subprocess.Popen("docker-compose up -d volume")
subprocess.Popen("docker-compose up -d portainer")
subprocess.Popen("docker-compose up -d consul")
subprocess.Popen("docker-compose up -d mongo")
subprocess.Popen("docker-compose up -d config-seed")
subprocess.Popen("docker-compose up -d logging")
subprocess.Popen("docker-compose up -d notifications")
subprocess.Popen("docker-compose up -d rulesengine")
subprocess.Popen("docker-compose up -d data")
subprocess.Popen("docker-compose up -d export-client")
subprocess.Popen("docker-compose up -d export-distro")
subprocess.Popen("docker-compose up -d metadata")
subprocess.Popen("docker-compose up -d scheduler")
subprocess.Popen("docker-compose up -d command")
subprocess.Popen("docker-compose up -d device-virtual")

