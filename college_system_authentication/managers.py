from django.db import models


class RoleManager(models.Manager):
    """
    Manager para el manejo de roles.
    """

    def get_groups(self):
        return self.get_queryset()


class AllRoleManager(models.Manager):

    def get_networks(self):
        return self.get_queryset()

    def create_role(self, role, company, validation_token, validated, **extra_fields):
        all_role = self.model()
        all_role.role = role
        all_role.company = company
        all_role.validation_token = validation_token
        all_role.is_validated = validated
        all_role.save()
        return all_role
