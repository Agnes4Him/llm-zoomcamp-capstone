module "network" {
  source = "./modules/network"

  project = var.project
}

module "iam" {
  source = "./modules/iam"

  project = var.project
}

module "security_group" {
  source = "./modules/security-group"

  vpc_id = module.network.vpc_id
}

module "ec2" {
  source = "./modules/ec2"

  subnet_id          = module.network.public_subnet_id
  security_group_id = module.security_group.id
  iam_instance_profile = module.iam.instance_profile

  project = var.project
}

module "rds" {
  source = "./modules/rds"

  vpc_id = module.network.vpc_id
  subnet_ids = module.network.private_subnet_ids

  security_group_id = module.security_group.id

  project = var.project
}
