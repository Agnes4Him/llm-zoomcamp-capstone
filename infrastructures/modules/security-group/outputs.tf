output "rds_security_group_id" {
  value = aws_security_group.rds.id
}

output "ec2_security_group_id" {
  value = aws_security_group.main.id
}