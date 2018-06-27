#!/usr/bin/env python
# find postgresql latest jdbc driver
# inspired by https://github.com/galaxyproject/ansible-postgresql/blob/master/files/get_repo_rpm_release.py

import re
import sys
import urllib2


url = "https://jdbc.postgresql.org/download.html"

try:
    distro = urllib2.urlopen(url)
except urllib2.HTTPError, e:
    print >>sys.stderr, "Failed to fetch directory list from %s" % url
    raise

latest_version = re.findall(".*download/postgresql-\d*.*\.jar",distro.read())[0]
latest_version = re.sub('<p><a href="','',latest_version)
latest_version_url = "https://jdbc.postgresql.org/" + latest_version  

print latest_version_url.replace("\\r\\n", "")
sys.exit(0)
