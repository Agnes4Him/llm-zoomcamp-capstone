variable "aws_region" {
  type        = string
  default     = "eu-west-2"
  description = "AWS Region"
}

variable "project_name" {
  type        = string
  description = "The name of the project"
}

variable "ami_id" {
  type        = string
  default     = "ami-07f936ee1f9a0de0e"
  description = "The AMI ID for the EC2 instance"
}

variable "instance_type" {
  type        = string
  default     = "t3.medium"
  description = "The instance type for the EC2 instance"
}

variable "subnet_id" {
  type        = string
  description = "The subnet ID for the EC2 instance"
}

variable "security_group_id" {
  type        = string
  description = "The security group ID for the EC2 instance"
}

variable "public_key_path" {
  type = string
}

variable "role_name" {
  type        = string
  description = "The IAM role name for the EC2 instance profile"
}