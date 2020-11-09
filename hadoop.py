import os 
def hadoop():
    while True:
        os.system("tput setaf 7")
        print("\t\Install and configure Hadoop\n")
        os.system('tput setaf 7')
        print(" 1. Check if AWS CLI is installed
2. Install AWSCLI
3. Check if Hadoop is installed
4. Install Hadoop
5. Create a DataNode
6. Create a Namenode
")

        x = input("Enter Choice: ")
        if int(x)==1:
            os.system("aws --version")
        elif int(2)==2:
            list = ['''curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"''', "sudo yum install -y unzip","sudo unzip awscliv2.zip","sudo ./aws/install"]
            for i in list:
                os.system(i)
    
        elif int(x)==3:
            os.system("hadoop version")
	
        elif int(x)==4:
            hadooplink = input("Enter your s3 bucket link for hadoop")
            jdklink = input("Enter your s3 bucket link for jdk")
            hadooplink = "/usr/local/bin/aws s3 cp " + hadooplink
            jdklink = "/usr/local/bin/aws s3 cp " + jdklink
            list1 = ["sudo rpm -ivh jdk-8u171-linux-x64.rpm","sudo rpm -ivh jdk-8u171-linux-x64.rpm","sudo rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force"]
            for k in list1:
                os.system(k)
            os.system("")
        elif int(x)==5:
            masternode = input("Enter the IP of the masternode")
            masternode = '''sudo sed -i "7i <property>\n<name>fs.default.name</name>\n<value>hdfs://'''+masternode+''':9001</value>\n</property>>" core-site.xml'''
            list2=["mkdir /dn","cd /etc/hadoop/",'''sudo sed -i "7i <property>\n<name>dfs.data.dr</name>\n<value>/dn</value>\n</property>" hdfs-site.xml''','''sudo sed -i "11d" hdfs-site.xml''',masternode,'''sudo sed -i "11d" core-site.xml''',"sudo hadoop datanode -format","sudo hadoop-daemon.sh start datanode"]
            for l in list2:
                os.system(l)
        elif int(x)==6:
            list3 = ["mkdir /nn","cd /etc/hadoop",'''sudo sed -i "7i <property>\n<name>dfs.name.dr</name>\n<value>/nn</value>\n</property>" hdfs-site.xml''','''sudo sed -i "11d" hdfs-site.xml''','''sudo sed -i "7i <property>\n<name>fs.default.name</name>\n<value>hdfs://0.0.0.0:9001</value>\n</property>>" core-site.xml''','''sudo sed -i "11d" core-site.xml''',"sudo hadoop namenode -format","sudo hadoop-daemon.sh start namenode"]
            for m in list3:
                os.system(m)
        else:
            os.system("tput setaf 1")
            print("Invalid Option")
