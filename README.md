
Role Name
=========

check-logs



Role Variables
--------------

Collect logs on Inspur server,it takes about 5 minutes.

Dependencies
------------

copy the collected logs to folder 

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    tasks:
       - name: "Collect logs"
         inspur.sm.collect_log:
         file_url: "/home/collected-logs/test.tar"
         provider: "{{ *** }}"


## Return Values

Common return values are documented here, the following are the fields unique to this module:

Key	Returned	Description

Check to see if a change was made on the device.

Messages returned after module execution.

Status after module execution.
