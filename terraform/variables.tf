variable "resource_group_name" {
  type        = string
  default     = "sftp-resources"
  description = "Name of the resource group where all resources will be deployed."
}

variable "location" {
  type        = string
  description = "Azure region where resources will be deployed."
}

variable "container_name" {
  type        = string
  description = "Name of the container instance."
}

variable "container_image" {
  type        = string
  description = "Docker image to use for the container instance."
}

variable "container_cpu" {
  type        = number
  default     = 1
  description = "Amount of CPU allocated to the container instance."
}

variable "container_memory" {
  type        = number
  default     = 1.5
  description = "Amount of memory (in GB) allocated to the container instance."
}

variable "tenant_id" {
  type        = string
  description = "Azure AD Tenant ID, required if using a service principal for authentication."
}

variable "client_id" {
  type        = string
  description = "Azure AD Client ID for authentication with a service principal."
}

variable "client_secret" {
  type        = string
  sensitive   = true
  description = "Azure AD Client Secret for authentication with a service principal. This variable is marked as sensitive to prevent its value from being exposed in logs."
}

variable "subscription_id" {
  type        = string
  description = "Azure Subscription ID under which all resources will be provisioned."
}
