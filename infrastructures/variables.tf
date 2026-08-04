variable "aws_region" {
  type        = string
  default     = "eu-west-2"
  description = "AWS Region"
}

variable "project_name" {
  type        = string
  default     = "healthsecure"
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

variable "key_name" {
  type        = string
  default     = "llm-project"
  description = "The key pair name for the EC2 instance"
}

variable "vpc_cidr_block" {
  type        = string
  default     = "10.0.0.0/16"
  description = "The CIDR block for the VPC"
}

variable "public_subnet_cidr_blocks" {
  type        = list(string)
  default     = ["10.0.0.0/24", "10.0.1.0/24"]
  description = "The CIDR blocks for the public subnets"
}

variable "private_subnet_cidr_blocks" {
  type        = list(string)
  default     = ["10.0.2.0/24", "10.0.3.0/24"]
  description = "The CIDR blocks for the private subnets"
}

variable "availability_zones" {
  type        = list(string)
  default     = ["eu-west-2a", "eu-west-2b"]
  description = "The availability zones for the subnets"
}

variable "identifier" {
  type    = string
  default = "healthsecure-postgres"
}

variable "database_name" {
  type    = string
  default = "healthsecure"
}

variable "username" {
  type    = string
  default = "healthsecure_user"
}

variable "password" {
  type      = string
  sensitive = true
}

variable "instance_class" {
  type    = string
  default = "db.t3.micro"
}

variable "api_repository_name" {
  type    = string
  default = "healthsecure-api"
}

variable "manifest_repository_name" {
  type    = string
  default = "healthsecure-manifests"
}