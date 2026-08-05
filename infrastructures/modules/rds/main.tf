resource "aws_db_subnet_group" "postgres" {
  name       = "${var.identifier}-subnet-group"
  subnet_ids = var.private_subnet_ids
}


resource "aws_db_instance" "postgres" {
  identifier        = var.identifier
  engine            = "postgres"
  engine_version    = "16"
  instance_class    = var.instance_class
  allocated_storage = 20

  db_name  = var.database_name
  username = var.username
  password = var.password

  db_subnet_group_name   = aws_db_subnet_group.postgres.name
  vpc_security_group_ids = var.security_group_ids
  publicly_accessible    = false
  storage_encrypted      = true

  backup_retention_period = 7
  skip_final_snapshot     = true
  deletion_protection     = false

}