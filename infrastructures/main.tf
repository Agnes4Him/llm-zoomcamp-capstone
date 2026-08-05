module "network" {
  source = "./modules/network"

  vpc_cidr_block             = var.vpc_cidr_block
  public_subnet_cidr_blocks  = var.public_subnet_cidr_blocks
  private_subnet_cidr_blocks = var.private_subnet_cidr_blocks
  availability_zones         = var.availability_zones
}

module "iam" {
  source = "./modules/iam"

  project_name = var.project_name
}

module "security_group" {
  source = "./modules/security-group"

  project_name = var.project_name
  vpc_id       = module.network.vpc_id
}

module "ec2" {
  source = "./modules/ec2"

  role_name         = module.iam.ec2_role_name
  public_key        = var.public_key
  ami_id            = var.ami_id
  instance_type     = var.instance_type
  subnet_id         = module.network.public_subnet_id
  security_group_id = module.security_group.ec2_security_group_id
  project_name      = var.project_name
}

module "rds" {
  source = "./modules/rds"

  identifier         = var.identifier
  vpc_id             = module.network.vpc_id
  private_subnet_ids = module.network.private_subnet_ids
  security_group_ids = [module.security_group.rds_security_group_id]
  database_name      = var.database_name
  username           = var.username
  password           = var.password
}

module "ecr" {
  source = "./modules/ecr"

  api_repository_name      = var.api_repository_name
  manifest_repository_name = var.manifest_repository_name
}
