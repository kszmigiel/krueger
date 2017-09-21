# krueger
My research project. The point is to create some "Ansible-like" DevOps tool, but simpler ;)

Here is how to use it:

`$ python3 krueger.py config.ini /home/user/.ssh/id_rsa.pub`

Where `config.ini` is your config file, written in INI format,
and `/home/user/.ssh/id_rsa.pub` is path to your public RSA key, which should be added to every remote host you want to work with.
In repo you can find `config.ini` file, which contains exemplary configuration. It's recommended to read it, before attempting to write
your's own ;)

If you want to copy some files to remote host, remember to include `source` and `dest` paths in your config file.
To actually copy files, add `-f` flag at the end of command:
`$ python3 krueger.py config.ini /home/user/.ssh/id_rsa.pub -f`
