from django.contrib.auth import get_user_model, user_logged_in
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from charity_app.accounts.models import CharityUserProfile, OrganizationUserProfile

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def create__user_profile__or__organization_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 'U':
            CharityUserProfile.objects.create(user=instance)
        # Logic when user_type == Organization (O)
        else:
            OrganizationUserProfile.objects.create(user=instance)


@receiver(post_save, sender=UserModel)
def save__user_profile__or__organization_profile(sender, instance, **kwargs):
    if instance.user_type == 'U':
        instance.charityuserprofile.save()
    # Logic when user_type == Organization (O)
    else:
        instance.organizationuserprofile.save()


@receiver(user_logged_in)
def save__last_login_date(sender, request, user, **kwargs):
    user.last_login = timezone.now()
    user.save()


@receiver(post_save, sender=UserModel)
def delete__user_automatically_if_not_log_in_more_than_year(sender, instance, **kwargs):
    if instance.last_login is not None:
        days_inactive = (timezone.now() - instance.last_login).days
        if days_inactive > 365:
            instance.delete()
