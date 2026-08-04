output "api_repository_url" {
  value = aws_ecr_repository.api.repository_url
}

output "manifest_repository_url" {
  value = aws_ecr_repository.manifests.repository_url
}

output "registry_id" {
  value = aws_ecr_repository.api.registry_id
}