# Ansible: Tomcat
## An Ansible role for Apache-tomcat installation and configuration on Centos 7.

* Downloads latets build for given tomcat major version (tomcat_version variable)
* Installs it to /opt directory.
* Sets up tomcat's manager page
* Downloads latest postgresql jdbc driver.

## All variables are optional or supplied via defaults file.

* tomcat_version - defines tomcat major version to be downloaded and installed (default - 9)
* tomcat_user - tomcat's OS user (default - tomcat)
* tomcatXmx - tomcat's memory settings (default 1/2 of system's RAM)
* tomcatXms - tomcat's memory settings (default 1/2 of system's RAM)
* root_dir - root direcrory for application (default - /opt)
* manager_user - user for tomcat's manager page (default - tomcat)
* manager_password - password for manager user (should be moved to vault)

## Result:
Apache-tomcat up and running on port 8080 with manger page and latest postgresql driver

## Example Playbook.

```
---
- hosts: tomcat
  remote_user: root
  become: yes

  roles:
    - tomcat
```

## TODO:
[ ] fully variablize setenv to fit various projects

