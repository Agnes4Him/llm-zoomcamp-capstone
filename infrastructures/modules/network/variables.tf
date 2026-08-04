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
