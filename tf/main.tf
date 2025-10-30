terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "7.9.0"
    }
  }
}

variable "project_id" {
  type = string
}

variable "project_region" {
  type = string
  default = "us-west2"
}

provider "google" {
  project = var.project_id
  region = var.project_region
}

resource "google_project_service" "cloud_build" {
  project = var.project_id
  service = "cloudbuild.googleapis.com"
  disable_dependent_services = true
}

resource "google_project_service" "cloud_run" {
  project = var.project_id
  service = "run.googleapis.com"
  disable_dependent_services = true
}
