variable "project_name" {
  type        = string
  description = "The name of the project"
}

variable "ami_id" {
  type        = string
  default     = "ami-0c55b159cbfafe1f0"
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

variable "key_name" {
  type        = string
  description = "The key pair name for the EC2 instance"
}

variable "role_name" {
  type        = string
  description = "The IAM role name for the EC2 instance profile"
}