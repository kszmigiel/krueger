# krueger
My research project. The point is to create some "Ansible-like" DevOps tool, but simpler ;)

Here is how to use it:

`$ python3 krueger.py config.ini /home/user/.ssh/id_rsa.pub`

Where `config.ini` is your config file, written in INI format,
and `/home/user/.ssh/id_rsa.pub` is path to your public RSA key, which should be added to every remote host you want to work with.
