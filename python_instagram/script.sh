#!/bin/bash
cd /var/lib/docker/volumes
cd $(ls -d */)/_data
WEB_PATH=$(pwd)
echo $WEB_PATH
echo '<iframe width="600" height="800" src="'$1'embed" frameborder="0"></iframe>' > $WEB_PATH/instagram.html
