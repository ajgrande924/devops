# vagrant

### usage

```sh
vagrant up
vagrant halt
vagrant destroy
vagrant box list
vagrant box remove ubuntu/xenial64
```

### ubuntu

  - `ubuntu/xenial64`
  - `ansible`
  - `awscli`
  - `terraform@0.11.7`
  - `packer@1.2.4`

### misc

```sh
# add vagrant scp plugin
vagrant plugin install vagrant-scp

# vagrant scp example
# vagrant scp <file> <box_id>:<target_location>
vagrant scp instance.tr 29c2765:/home/vagrant
```