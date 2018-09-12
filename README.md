# Tomcat
An Ansible role for Apache-tomcat installation and configuration on Centos 7.

* Downloads latets build for given tomcat major version (tomcat_version variable)
* installs it to /opt directory.
* sets up tomcat's manager page
* downloads latest postgresql jdbc driver.

All variables are optional or supplied via defaults file.

* tomcat_version - defines tomcat major version to be downloaded and installed (default - 8)
* tomcat_user - tomcat's user (default - tomcat)
* tomcatXmx - tomcat's memory settings (default 1/2 of system's RAM)
* tomcatXms - tomcat's memory settings (default 1/2 of system's RAM)
* root_dir - root direcrory for application (default - /opt)
* manager_user - user for tomcat's manager page (default - tomcat)
* manager_password - password for manager user (should be moved to vault)

Result: tomcat up and running on port 8080
