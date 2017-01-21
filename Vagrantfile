# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "hollywood-0bb4a643.box”
  config.vm.box_url = "file://hollywood-0bb4a643.box"
  config.vm.provision "shell", path: "bin/box-setup.sh"
end
