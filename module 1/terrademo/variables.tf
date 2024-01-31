variable "credentials" {
  description = "my credentials"
  default ="./keys/my-creds.json"
}


variable "project" {
  description = "my terra project"
  default = "terrademo-412700"
}


variable "region" {
  description = "region"
  default = "EU"
}


variable "location" {
  description = "my project location"
  default = "EU"
}


variable "bq_dataset_name" {
  description = "my BigQuery dataset"
  default = "terra_dataset"
}


variable "gcs_bucket_name" {
  description = "my storage bucket"
  default = "terrademo-412700-bucket"
}


variable "gcs_storage_class" {
  description = "bucket storage class"
  default = "STANDARD"
}