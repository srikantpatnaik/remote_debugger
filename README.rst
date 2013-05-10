Remote_debugger - A web2py application
======================================

Steps to install remote_debugger in a virtualenv
------------------------------------------------

#. Download, untar the virtualenv. `cd` to virtualenv dir and create new virtualenv project ::
	
	python virtualenv.py web2pyProject

#. `cd` to `web2pyProject` and start virtualenv ::

	source bin/activate

#. Now download web2py source and unzip in same directory, remove the zip file later.

#. Also download and install `ipython` and `pymysql` in the virtualenv either by source or using ::

	pip install ipython pymysql

#. `cd` to `applications` directory and clone this repository ::

	git clone http://github.com/srikantpatnaik/remote_debugger.git

#. Now, `cd` to `remote_debugger/databases` and remove all files if present. Now come to parent 
   directory(web2py) and start web2py server ::

	python web2py.py &

#. Login `mysql` as root and create database `rt_db` (say) ::

	mysql -u root -p

   create db as ::

	create database rt_db;

   grant permission to desired user ::

	GRANT ALL ON <database>.* TO <user>@localhost IDENTIFIED BY '<password>';

#. Next goto `controllers` -> `appadmin.py` -> `index` -> `db.auth_group` and create two new records and also
   give relevant descriptions(optional) ::

	Role -> techie and client

#. Now, goto web browser and edit your application. First change `db.py` in models ::

    db = DAL('mysql://<mysql-user>:<mysql-passwd>@localhost/rt_db')

   In the same file look for `auth.settings.everybody_group_id`	and update it with the group id of newly 
   created `client group` ::
	
	auth.settings.everybody_group_id = 2

#. In `controllers` -> `default.py` -> `access()` change `redirect` function IP to desired one. 

	
