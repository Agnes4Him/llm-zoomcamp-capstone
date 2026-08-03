resource "aws_db_instance" "postgres" {
    identifier="healthsecure-db"

    engine="postgres"

    engine_version="16"

    instance_class="db.t3.micro"

    allocated_storage=20


    username="healthsecure"

    password=random_password.db.result


    db_subnet_group_name=
    aws_db_subnet_group.main.name


    vpc_security_group_ids=[
    var.security_group_id
    ]


    skip_final_snapshot=true
}