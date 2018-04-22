variable "access_key" {}

variable "secret_key" {}

variable "ssh_key_name" {}

variable "target_host" {}

variable "region" {
    default = "us-east-1"
}

variable "master_instance_type" {
    default = "t2.micro"
}

variable "slave_instance_type" {
    default = "t2.small"
}

variable "ami" {
    default = "ami-9e2685e3"
}

variable "num_slaves" {
    default = 2
}

variable "cluster_name" {
	default = "stress"
}

variable "test_file" {
	default = "test.py"
}

variable "vpc_cidr_block" {
}

variable "subnet_cidr_block" {
}