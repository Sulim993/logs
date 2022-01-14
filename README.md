
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


Installing Ansible on Ubuntu
----------------------------
Ubuntu builds are available in a PPA here.

To configure the PPA on your machine and install Ansible run these commands:

$ sudo apt update
$ sudo apt install software-properties-common
$ sudo add-apt-repository --yes --update ppa:ansible/ansible
$ sudo apt install ansible
How to install and configure Ansible on your System
First, you need to install Ansible on your system. Just go to https://docs.ansible.com/ and follow the installation instructions for your Linux distribution. You can also set up this in a virtual machine or on Windows Subsystem for Linux.

I also installed 3 Ubuntu Servers in a virtual environment to demonstrate how Ansible is working.

Configuration
-------------
Before we can connect to the other 3 servers, we need to set up a general Ansible configuration file. This is very helpful, otherwise, we would need to enter all settings as options in our ansible commands. You can either edit the general Ansible Configuration file under “/etc/ansible/ansible.cfg” or create a new “ansible.cfg” in a project folder. By default, Ansible will check if there is an “ansible.cfg” file in your current folder which will overwrite the default settings.

You should always specify an inventory file, that you can place in your project folder. This inventory file contains all IP addresses and also configuration variables of the machines you want to control. I just named the inventory file “inventory” and place it in the project folder.

Next, you should think about how Ansible authenticates to your machines. There are generally two different methods. The first method is via usernames and passwords, which you can simply define either in the general “ansible.cfg” file. If some machines in your inventory require a different username and/or password you can also configure that separately in your inventory file by using the “[<name>:vars]” section. In this case, you also need to install the “sshpass” package on your Ansible machine and add “host_key_checking = False” in the default section of your ansible.cfg file.

Note it is not the best and most secure method and should not be used in production environments! In any production environment, you should create a corresponding private and public key pair for Ansible and upload the public key on all machines.

Example with username/password (don’t use in production)
--------------------------------------------------------
Ansible.cfg

[defaults]
inventory = inventory
host_key_checking = False
inventory

[nodes]
192.168.0.139
192.168.0.140

[master]
192.168.0.138

[master:vars]
ansible_ssh_user=master
ansible_ssh_pass=master

[nodes:vars]
ansible_ssh_user=vagrant
ansible_ssh_pass=vagrant
  
Example with private/public SSH key pair (recommended)
------------------------------------------------------
Ansible.cfg

[defaults]
inventory = inventory
host_key_checking = False
inventory

Ansible.cfg

[defaults]
inventory = inventory
host_key_checking = False[defaults]
inventory = inventory
[defaults]
inventory = inventory
host_key_checking = False
inventory

[nodes]
192.168.0.139
192.168.0.140

[master]
192.168.0.138

[nodes:vars]
ansible_ssh_user=christian
ansible_ssh_private_key_file=~/.ssh/ansible_id_rsa

[master:vars]
ansible_ssh_user=master
ansible_ssh_private_key_file=~/.ssh/ansible_id_rsa
  
Simple provisioning and controlling
-----------------------------------
Test the connection
  
Now that we have configured Ansible and can connect to our machines we can execute some test commands. This command will ping all machines that are in our inventory file.

ansible all -m ping

You can also change the “pattern” from “all” to a specific section you have defined in your inventory file. Let’s only ping the nodes, and exclude the master.

ansible nodes -m ping

Gather information
------------------
  
Now we want to execute a more complex command. You probably have noticed that the -m parameter will call an Ansible module. Modules are used to create an interface for specific programs on the machine. The “ping” module will just test a connection. Let’s execute a shell command using the “shell” module and pass the command as a module argument with the -a parameter.


These console commands are fine to perform one time commands or simple tests. But if you want to perform more complex actions or tasks we need something more structured. That is where Ansible playbooks come in.

Ansible playbooks
-----------------
Ansible playbooks can describe even complex automation tasks simply and effectively. It uses the YAML (Yet another markup language) standard, which is easily readable by humans and interpreted by machines. You can define a state where you want all your machines to be in. Ansible will take care of the rest and perform the necessary actions on the machines.

First, you need to start with a pattern of machines, you want to define a state for. You can also choose which user you want to use to execute any actions and if Ansible needs to execute commands with root privileges. For every pattern, you can describe one or more tasks to call Ansible modules. In the following example, we’re installing some software packages on the master server and nodes.

Install packages . YAML




hosts: nodes
become: yes
tasks:
    name: make sure net-tools are installed on all nodes
    apt:
      name: net-tools
      state: present
  
If you want to execute an Ansible playbook you need to use the command “ansible-playbook”. Note, that for installing software packages you need to become a root user. This can be done by the option “become”, which requires you to provide a “sudo” password either via the default or inventory configuration, or arguments in the command.

ansible-playbook installpackages.yaml -K

You can see that Ansible executed all tasks successfully, but it didn’t always change something. This is because some packages are already installed on the machines. Ansible only installs a package when it’s not installed already.

The list of possible automation and modules is huge. If you want to check out which modules you can use to automate tasks check out the Ansible docs. They are well documented with detailed explanations and examples.

