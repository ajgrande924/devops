variable "AWS_REGION" {
  default = "us-east-1"
}
variable "AMIS" {
  type = "map"
  default = {
    us-east-1 = "ami-0cfee17793b08a293"
    us-west-1 = "ami-09eb5e8a83c7aa890"
    us-east-2 = "ami-0f93b5fd8f220e428"
    us-west-2 = "ami-0b37e9efc396e4c38"
  }
}
