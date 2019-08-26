terraform {
  backend "s3" {
    bucket = "terraform-state-924"
    key = "terraform/provisioning"
  }
}