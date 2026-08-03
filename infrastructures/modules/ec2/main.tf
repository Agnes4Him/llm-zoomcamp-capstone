resource "aws_instance" "server" {

  ami = var.ami_id

  instance_type = var.instance_type

  subnet_id = var.subnet_id

  vpc_security_group_ids = [
    var.security_group_id
  ]

  key_name = var.key_name

  iam_instance_profile = var.iam_instance_profile


  user_data = templatefile(
    "${path.module}/user-data.sh.tpl",
    {
      flux_repo = file("${path.root}/kubernetes/bootstrap/flux-oci-repository.yaml")
      flux_kustomization = file("${path.root}/kubernetes/bootstrap/flux-kustomization.yaml")
      gateway = file("${path.root}/kubernetes/bootstrap/gateway.yaml")
      secret_store = file("${path.root}/kubernetes/bootstrap/secret-store.yaml")
      external_secret = file("${path.root}/kubernetes/bootstrap/externalsecret.yaml")
    }
  )


  tags = {
    Name = "healthsecure-k3s"
  }
}