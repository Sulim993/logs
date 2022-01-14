
Role Name
=========

logs v1.0.0

Role Variables
--------------

Collect logs on Inspur server,it takes about 1m.

Dependencies
------------

copy the collected logs to folder 
ths is the first version of the script 

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

  tasks:
    - logs:  
Ansible Setup - Gather Facts - https://docs.ansible.com/ansible/latest/modules/setup_module.html

It is very important when prompted for your username that you use username@MY.DOMAIN.COM. This whole string is case sensitive and the domain portion must be in upper case.

Install steps - CentOS
Update yum
$ sudo yum -y update

Install Ansible
$ sudo yum install epel-release $ sudo yum install ansible

Install node.js 12
$ curl -sL https://rpm.nodesource.com/setup_12.x | sudo bash - $ sudo yum install -y gcc-c++ make $ sudo yum install -y nodejs

Install Mark Map
$ npm install markmap-lib -g

Install steps - Ubuntu
Update Ubuntu - this step will take some time.
$ sudo apt update $ sudo apt-get upgrade -y

Make sure Python is installed.
$ sudo apt-get install python -y

Install Ansible.
$ sudo apt-add-repository ppa:ansible/ansible $ sudo apt-get update $ sudo apt-get install ansible -y

Install node.js
$ sudo apt install npm

Install Mark Map
$ npm install markmap-lib -g

Instructions for Windows Users
Windows Prequisites
These playbooks require the Windows Subsystems for Linux and the Ubuntu OS from the Microsoft Store. Aside from this requirement, the Linux prequisites similarly apply to Windows 10.

Install Steps - Windows 10
Right-click the Windows Start icon - select Apps and Features.
image

In the Apps and Features window - click Programs and Features under Related Settings on the right side of Apps and Features.
image

Click Turn Windows Features On or Off in the left (with the shield icon) side of the Programs and Features window.
image

Scroll to bottom of the Features window and put a check mark beside Windows Subsytem for Linux; Click Ok and close the open windows.
image

Launch the Microsoft Store.
image

Search for Ubuntu - click the first result.
image

Click Install.
image

Wait for Ubuntu to install.

Press Windows Key and start typing Ubuntu - click and launch Ubuntu.

The first time Ubuntu launches it has to setup - give this some time.

Enter your username and password for Ubuntu.

Update Ubuntu - this step will take some time.

$ sudo apt update

$ sudo apt-get upgrade -y

Make sure Python is installed.
$ sudo apt-get install python -y

Install Ansible.
$ sudo apt-add-repository ppa:ansible/ansible

$ sudo apt-get update

$ sudo apt-get install ansible -y

Install node.js.
$ sudo apt install npm

Install Mark Map.
$ sudo npm install markmap-lib -g
