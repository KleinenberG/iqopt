# IQOPTION Prodaction
 Запуск виртуальных машин
-----------------------------------
### В корне проекта запускаем  
`vagrant up`
 
 Запуск Ansible playbooks
-----------------------------------
* `cd playbook` - *переходим в директорию с playbooks*
* `ansible-playbiik minio.yml` - *установка и запуск сеервера minio*
* `ansible-playbook nginx.yml` - *Установка, конфигурирование и запуск web севрера nginx*
