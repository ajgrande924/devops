terraform {
  backend "s3" {
    bucket = "terraform-state-924"
    key = "terraform/vpc_ec2"
    region = "us-east-1"
  }
}