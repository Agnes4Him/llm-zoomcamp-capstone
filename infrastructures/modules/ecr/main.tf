resource "aws_ecr_repository" "api" {
  name = var.api_repository_name
  image_scanning_configuration {
    scan_on_push = true
  }

  image_tag_mutability = "MUTABLE"
  encryption_configuration {
    encryption_type = "AES256"
  }

  tags = {
    Name = var.api_repository_name
  }
}

resource "aws_ecr_repository" "manifests" {
  name = var.manifest_repository_name

  image_tag_mutability = "MUTABLE"
  encryption_configuration {
    encryption_type = "AES256"
  }

  tags = {
    Name = var.manifest_repository_name
  }
}