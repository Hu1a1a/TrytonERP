trytond
=======

The server of Tryton.
Tryton is business software, ideal for companies of any size, easy to use,
complete and 100% Open Source.
It provides modularity, scalability and security.

=======

First time: run pip install .


=======

virtual env: run & c:\Proyecto\TrytonERP\venv\Scripts\Activate.ps1  
Start server: run python bin/trytond -c trytond.conf
Set DB: run python bin/trytond-admin -c trytond.conf -d trytond_db -p
Update DB: run python bin/trytond-admin -c trytond.conf -d trytond_db --add