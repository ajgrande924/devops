# terraform

Time difference between the host machine and aws machine causes an authentication failure. To sync the time, run:

```sh
# for ubuntu host machine
sudo apt-get install ntpdate # can add to the vagrant install script
sudo ntpdate ntp.ubuntu.com
```

To test what infrastructure would be built bases on our terraform files:
```sh
terraform plan
```
To execute the changes:
```sh
terraform apply
```
To keep the changes in an out file, then apply those changes to the infrastructure:
```sh
terraform plan -out changes.terraform
terraform apply changes.terraform
```
To destroy the infrastructure:
```sh
terraform destroy
```

Terraform is:
  
  - a tool to automate the provisioning of infrastructure
  - a tool that can keep a history of all infrastructure changes
  - a tool that can be used to collaborate in a team on infrastructure automation
  - a tool that keeps the remote state of your infrastructure

Terraform is not:

  - a tool to do configuration management on the software on your machines

Ansible/Chef/Puppet/Salt are better alternatives for that. Terraform can work together with these tools to provide you CI on your machines. Terraform provides Configuration Management on an infrastructure level, not on the level of software of your machines. 

### examples

The `provisioning` example:

```sh
# files

backend.tf # configure remote state
instance.tf # define aws instance
provider.tf # define aws provider
vars.tf # define variables
script.sh # startup script to install + start nginx
terraform.tfvars # aws credentials
```

```sh
# commands

# generate key pair: mykey (private) and mykey.pub (public) in current directory
ssh-keygen -f mykey

# terraform
terraform init
terraform plan
terraform apply
terraform destroy
```

What happens after `terraform apply`:

  - creates a `t2.micro` instance in `us-east-1` (default)
  - provisions `script.sh`
  - executes `script.sh` which installs + starts nginx
  - console will output `ip` variable
  - public ip will be saved in local file `public_ips.txt`
  - state will be saved and versioning in s3 bucket

Once instance is up and running, you can ssh by running:

```sh
ssh ubuntu@<public_ip> -i mykey
```
