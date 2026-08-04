resource "aws_iam_role" "ec2" {
    name = "${var.project_name}-ec2-role"

    assume_role_policy = jsonencode({
        Version="2012-10-17"
        Statement=[{

            Effect="Allow"

            Principal={
            Service="ec2.amazonaws.com"
            }
            Action="sts:AssumeRole"
        }]
    })
}

resource "aws_iam_role_policy_attachment" "ec2_ecr_readonly" {
  role       = aws_iam_role.ec2.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly"
}

resource "aws_iam_policy" "secrets_manager_read" {
  name = "${var.project_name}-secrets-manager-read"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "secretsmanager:GetSecretValue",
          "secretsmanager:DescribeSecret"
        ]
        Resource = "*"
      }
    ]
  })
}


resource "aws_iam_role_policy_attachment" "ec2_secrets_manager_read" {
  role = aws_iam_role.ec2.name
  policy_arn = aws_iam_policy.secrets_manager_read.arn
}