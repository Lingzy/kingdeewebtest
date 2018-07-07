import yaml

f = open('settings.yaml',encoding='utf-8')
x = yaml.load(f)
print(x)