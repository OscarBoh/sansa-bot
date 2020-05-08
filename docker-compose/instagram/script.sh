#!/bin/bash
#d /var/lib/docker/volumes
#d $(ls -d */)/_data
#WEB_PATH=$(pwd)
echo 'test logs'
echo '<iframe width="600" height="800" src="'$1'embed" frameborder="0"></iframe>' > /opt/instagram/instagram.html
echo $(cat /opt/instagram/instagram.html)
