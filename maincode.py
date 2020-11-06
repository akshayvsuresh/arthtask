import os
import pyttsx3
import webbrowser as wb
import speech_recognition as sr

print("***********************WELCOME TO AWS CLI***************************")
pyttsx3.speak("Hello, Welcome to AWS CLI. I am here to assist you.")
pyttsx3.speak("Tell me what can i do for you ?")

while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        pyttsx3.speak("start speaking...and tell me next.")
        print("I am listening...")
        audio = r.listen(source)
        print("Your requirement is captured.")

    select = r.recognize_google(audio)
    try:
        if ("help" in select):
            pyttsx3.speak("I can create key pair.")
            print("I can create key pair.")
            pyttsx3.speak("I can create securty group as well.")
            print("I can create securyity group.")
            pyttsx3.speak(" i can help you in launching instances on aws cloud.")
            print("I can launch instances") 
            pyttsx3.speak(" i can create EBS volume as well as i can attach volume to instance. ")
            print("I can create EBS volume and also attach with instance.")
        elif ("create" in select) and ("key" in select):
            pyttsx3.speak("Enter name for key pair")
            key_name = input("enter key pair name : ")
            p = os.system("aws ec2 create-key-pair --key-name {0}".format(key_name))
            print(p)
            pyttsx3.speak("Key pair has been created.")
        elif ("create" in select) and ("security" in select):
            pyttsx3.speak("Enter name for security group")
            sec_gp_name = input("Enter name for security group : ")
            pyttsx3.speak("enter description for security group.")
            sec_disc = input("Enter discription for security group : ")
            s = os.system("aws ec2 create-security-group --group-name {0} --description {1}".format(sec_gp_name, sec_disc))
            print(s)
            pyttsx3.speak("security group has been created")
        elif ("launch" in select) and ("new" in select) and ("instance" in select):
            pyttsx3.speak("Enter image id here.")
            img_id = input("Enter image id : ")
            pyttsx3.speak("Enter type of image.")
            img_type = input("Enter image type : ")
            pyttsx3.speak("Enter subnet id :")
            subnet_id = input("Enter subnetId : ")
            pyttsx3.speak("Enter id of security group.")
            se_id = input("Enter security group id : ")
            pyttsx3.speak("Enter name of key.")
            key_name = input("Enter created  key name : ")
            i = os.system("aws ec2 run-instances --image-id {0} --instance-type {1} --subnet-id {2} --security-group-id {3} --key-name {4}".format(img_id, img_type, subnet_id, se_id, key_name))
            print(i)
            pyttsx3.speak("instance has been launched")
        elif ("create" in select) and ("volume" in select):
            pyttsx3.speak("give me volume type and size .")
            vt = input("Enter the type of volume : ")
            size = input("Enter the size of volume :")
            zone = input("Enter the name of avaiability zone :")
            e = os.system("aws ec2 create-volume --volume-type {0} --size {1}  --availability-zone {2}".format(vt, size, zone))
            print(e)
            pyttsx3.speak("volume has created")
        elif ("attach" in select) and ("volume" in select):
            pyttsx3.speak("please enter volume id and instance id.")
            vol_id = input("Enter volume id: ")
            instance_id = input("Enter instance id : ")
            dev_name = input("Enter device name or drive name : ")
            a = os.system(
                "aws ec2 attach-volume --volume-id {} --instance-id {} --device {}".format(vol_id, instance_id,dev_name))
            print(a)
            pyttsx3.speak("volume has attched succesfully.")
        elif ("show" in select) and ("pair" in select):
            wb.open("https://ap-south-1.console.aws.amazon.com/ec2/v2/home?region=ap-south-1#KeyPairs:")
        elif ("show" in select) and ("group" in select):
            wb.open("https://ap-south-1.console.aws.amazon.com/ec2/v2/home?region=ap-south-1#SecurityGroups:")
        elif ("launched" in select) and ("running" in select) and ("instance" in select):
            wb.open("https://ap-south-1.console.aws.amazon.com/ec2/v2/home?region=ap-south-1#Instances:")
        elif ("show" in select) and ("volume" in select):
            wb.open(
                "https://ap-south-1.console.aws.amazon.com/ec2/v2/home?region=ap-south-1#Volumes:sort=desc:createTime")
        elif ("thank" in select) or ("stop" in select):
            pyttsx3.speak("okay  bye have a nice day.")
            break
        else:
            pyttsx3.speak("I am not getting to you.please speak again.")
            print("Unable to understand")
    except KeyboardInterrupt:
        print("done")
