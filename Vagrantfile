Vagrant.configure('2') do |config|
 config.ssh.insert_key = false
 config.vm.box = "ubuntu/xenial64"
# config.vm.box = "debian/stretch64"
 

# config.vm.define "node_1" do |node_1|
##  node_1.vm.network "private_network", ip: "192.168.10.11", auto_config: false
##  node_1.vm.network "private_network", ip: "192.168.10.11"	
##  node_1.vm.network "private_network", type: "dhcp", virtualbox__vboxnet0: true
#  node_1.vm.network "private_network", ip: "192.168.10.11", virtualbox__vboxnet0: true, auto_config: false
##  node_1.vm.network "private_network", ip: "192.168.10.11", virtualbox__vboxnet0: true	
## node_1.vm.provision "shell", run: "always", inline: "ifconfig enp0s8 192.168.10.11/24 up"
# node_1.vm.provision "shell", run: "always", inline: "sudo dhclient enp0s8"
# end


 config.vm.define "node_1" do |node_1|
  node_1.vm.network "private_network", ip: "192.168.10.11", virtualbox__vboxnet0: true, auto_config: false
  node_1.vm.provision "shell", run: "always", inline: "sudo dhclient enp0s8"
 end

 config.vm.define "node_2" do |node_2|
  node_2.vm.network "private_network", ip: "192.168.10.12", virtualbox__vboxnet0: true, auto_config: false
  node_2.vm.provision "shell", run: "always", inline: "sudo dhclient enp0s8"
 end

 config.vm.define "node_3" do |node_3|
  node_3.vm.network "private_network", ip: "192.168.10.13", virtualbox__vboxnet0: true, auto_config: false
  node_3.vm.provision "shell", run: "always", inline: "sudo dhclient enp0s8"
 end




# config.vm.define "node_4" do |node_4|
#  node_4.vm.network "private_network", type: "dhcp", virtualbox__vboxnet0: true,  auto_config: false
#  node_4.vm.provision "shell", run: "always", inline: "ifconfig enp0s8 192.168.10.11/24 up"
#  node_4.vm.provision "shell", run: "always", inline: "sudo dhclient enp0s8"
# end

#
# config.vm.define "node_2" do |node_2|
#  node_2.vm.network "private_network", type: "dhcp", auto_config: false
#  node_2.vm.provision "shell", run: "always", inline: "ifconfig enp0s8 192.168.10.12/24 up"
# end
#
# config.vm.define "node_3" do |node_3|
#  node_3.vm.network "private_network", type: "dhcp", auto_config: false
#  node_3.vm.provision "shell", run: "always", inline: "ifconfig enp0s8 192.168.10.13/24 up"
# end
end
