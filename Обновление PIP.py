import subprocess as sbp
import pip
pkgs = eval(str(sbp.run("pip3 list -o --format=json", shell=True, stdout=sbp.PIPE).stdout, encoding='utf-8'))
for pkg in pkgs:
    print('установка(обновление) ', pkg['name'])
    sbp.run("pip3 install --upgrade " + pkg['name'], shell=True)
print('Конец установки')