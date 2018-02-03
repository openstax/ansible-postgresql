ansible-postgres
=========

An ansible role used to install the postgresql database locally on a server or used to create databases and users on an Amazon RDS.

Requirements
------------

N/A

Role Variables
--------------





| Name                            | Default Value    | Description                                                                      |
| ------------------------------- | ---------------- | -------------------------------------------------------------------------------- |
|`pg_version`| 9.5 | the postgresql database server and client version to install |
|`pg_rds`| false | if the database server is an aws rds instance |
|`pg_host` | localhost | the host where the database server is located |
|`pg_port` | 5432 | the port the database server is running on |
|`pg_admin_user` | postgres | the database user that has SUPERUSER privilages |
|`pg_admin_password` | omitted | the password for the `pg_admin_user`" |
|`pg_admin_group` | `pg_admin_user` | the group the database admin should be a part of |
|`pg_service_name`| postgresql | the service name for the postgresql database |
|`pg_service_user`| `pg_admin_user` | the name of user that runs the database service |
|`pg_service_group` | `pg_admin_user` | the group of the user that runs the database service |
|`pg_service_enabled` | true | if the database service should be enabled |
|`pg_ssl_dest_cert_file` | /etc/ssl/certs/ssl-cert-snakeoil.pem | the location of database ssl certificate file |
|`pg_ssl_dest_key_file` | /etc/ssl/private/ssl-cert-snakeoil.key | the location of database ssl key file |
|`pg_locale` | en_US.UTF-8 | the locale setting for the database |
|`pg_default_roles` | [CREATEDB] | default roles to apply to any configured database users |
|`pg_databases` | [] | a list of databases to be created in the database |
|`pg_users` | []

Dependencies
------------

N/A

Example Playbook
----------------

    - hosts: servers
      hosts: all
        vars:
          pg_rds: no
          pg_is_master_server: yes
          pg_databases:
            - name: testing
              port: 5432
              host: 127.0.0.1
            - name: testing2
          pg_users:
            - name: master_splinter
              db: testing
              password: imakeanotherfunny
              roles:
                - SUPERUSER
            - name: leonerdo
              db: testing2
              password: ninjavanish
        roles:
          - role: ansible-postgresql

License
-------

GPLv2

Development & Testing
---------------------

This project uses [Molecule](http://molecule.readthedocs.io/) to aid in the
development and testing; the role is unit tested using
[Testinfra](http://testinfra.readthedocs.io/) and
[pytest](http://docs.pytest.org/).

To develop or test you'll need to have installed the following:

* Linux (e.g. [Ubuntu](http://www.ubuntu.com/))
* [Docker](https://www.docker.com/)
* [Python](https://www.python.org/) (including python-pip)
* [Ansible](https://www.ansible.com/)
* [Molecule](http://molecule.readthedocs.io/)

To run the role

```bash
molecule test
```
