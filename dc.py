#!/usr/bin/python3

import os


def selectopt(arg):
  switcher = {
    1: install,
    2: pull,
    3: showimages,
    4: runningos,
    5: allos,
    6: createcontwithterm,
    7: createcontrunback,
    8: startos,
    9: stopos,
    10: deleteos,
    11: deleteallos,
    12: deleteimage
  }
  func = switcher.get(arg,lambda:"Select a valid option")
  return func()

def install():
  print("Creating docker repo....")
  os.system("sudo dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo")
  print("Installing docker-ce...")
  os.system("sudo dnf install docker-ce --nobest -y")
  print("Starting docker service")
  os.system("systemctl start docker")
  os.system("systemctl enable docker")


def pull():

  print("Select os image: ")
  print(" 1.Alpine")
  print(" 2.Ubuntu")
  print(" 3.Centos")
  print(" 4.Any Other")

  k=int(input())
  if k==1:
    os.system("docker pull alpine") 
  elif k==2:
    os.system("docker pull ubuntu")
  elif k==3:
    os.system("docker pull centos")
  elif k==4:
    print("Enetr the image name you want to pull: ")
    sname = input()
    try:
      os.system("docker pull "+sname)
    except Exception as e:
      return{"Error: {}".format(e)},500

def showimages():
  os.system("docker image ls")

def runningos():
  os.system("docker ps")

def allos():
  os.system("docker ps -a")


def createcontwithterm():
  print("Enter image name: ")
  imname=input()
  print("Enter os name: ")
  osname=input()
  os.system("docker run -it --name "+osname+" "+imname)

def createcontrunback():
  print("Enter image name: ")
  imname=input()
  print("Enter os name: ")
  osname=input()
  os.system("docker run -dit --name "+osname+" "+imname)

def startos():
  print("Enter os name: ")
  osname=input()
  os.system("docker start "+osname)

def stopos():
  print("Enter os name: ")
  osname=input()
  os.system("docker stop "+osname)

def deleteos():
  print("Enter os name")
  osname=input()
  os.system("docker rm "+osname)

def deleteallos():
  os.system("docker rm `docker ps -aq`")

def deleteimage():
  print("Enter image name: ")
  imname=input()
  os.system("docker rmi "+imname)

n=20
while(n!=13):
  print("\n\n")
  print("******Welcome to the Docker CLI*********")
  print("\n")
  print("Select an option")
  print("\n")
  print(" 1.Install Docker")
  print(" 2.Pull Image from dockerhub")
  print(" 3.Show all available images")
  print(" 4.Print all currently running containers")
  print(" 5.Print all containers")
  print(" 6.Create container and get its terminal")
  print(" 7.Create container and run it in background")
  print(" 8.Start a container")
  print(" 9.Stop a container")
  print(" 10.Delete a container")
  print(" 11.Delete all containers")
  print(" 12.Delete an image")
  print(" 13.Exit")
  print("\n\n")
  n=int(input())
  selectopt(n)
