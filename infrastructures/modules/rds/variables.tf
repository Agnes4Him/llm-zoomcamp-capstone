variable "identifier" {
  type    = string
  default = "healthsecure-postgres"
}

variable "vpc_id" {
  type = string
}

variable "security_group_ids" {
  type = list(string)
}

variable "database_name" {
  type    = string
  default = "healthsecure"
}

variable "username" {
  type    = string
  default = "healthsecure_admin"
}

variable "password" {
  type      = string
  sensitive = true
}

variable "instance_class" {
  type    = string
  default = "db.t3.micro"
}

variable "private_subnet_ids" {
  type        = list(string)
  default     = []
  description = "description"
}
