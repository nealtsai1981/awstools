import sys
import os

def awsls():
    cmd = "aws s3 ls "

    for i in range(1, len(sys.argv)):
    	cmd = cmd + "s3://" if i == 1 and sys.argv[i].find("s3://") == False else cmd
        cmd = cmd + sys.argv[i] + " "
    os.system(cmd)

def awscp():
    cmd = "aws s3 cp "

    for i in range(1, len(sys.argv)):
    	# cmd = cmd + "s3://" if (i == 1 and sys.argv[i].find("s3://") < 0) or (i == 2 and sys.argv[i].find("s3://") < 0) else cmd
        cmd = cmd + sys.argv[i] + " "
    print cmd
    os.system(cmd)

def awsvim():
    #cmd_list = sys.argv[1].split("/")
    cmd = "vim https://s3-ap-northeast-1.amazonaws.com/%s" % sys.argv[1]
    # for i in range(1, len(cmd_list)):
    #     cmd = cmd + "/" + cmd_list[i]
    print cmd
    os.system(cmd)
