provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "secure_bucket" {
  bucket = "vineet-secure-bucket-demo-123"

  tags = {
    Name = "SecureBucket"
  }
}

resource "aws_s3_bucket_versioning" "versioning" {
  bucket = aws_s3_bucket.secure_bucket.id

  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "encryption" {
  bucket = aws_s3_bucket.secure_bucket.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

resource "aws_s3_bucket_public_access_block" "secure_public_access" {
  bucket = aws_s3_bucket.secure_bucket.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_security_group" "secure_sg" {
  name        = "secure-security-group"
  description = "Allow SSH only from trusted IP"

  ingress {
    description = "Restricted SSH access"

    from_port   = 22
    to_port     = 22
    protocol    = "tcp"

    cidr_blocks = ["192.168.1.10/32"]
  }
}
