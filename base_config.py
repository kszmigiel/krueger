import configparser

cfg = configparser.ConfigParser()

cfg.read('cfg.ini')

print(cfg.sections())

for section in cfg.sections():
    for val in cfg[section]:
        print(val)
