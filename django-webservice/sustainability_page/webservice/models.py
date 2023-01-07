import uuid

from django.contrib.auth import models as auth_models, validators as auth_validators
from django.contrib.contenttypes.models import ContentType
from django.contrib.gis.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class SusPageUser(auth_models.AbstractUser):
    username_validator = auth_validators.UnicodeUsernameValidator()
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=False,
        help_text=_(
            "Not Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={"unique": _("A user with that username already exists.")},
    )
    guid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    email = models.EmailField(_("email address"), unique=True)
    first_name = models.EmailField(
        _("first name"), max_length=1024, blank=False, null=True
    )
    last_name = models.CharField(
        _("last name"), max_length=1024, blank=False, null=True
    )

    # Profile Details
    newsletterAgree = models.BooleanField(default=False)
    business_name = models.CharField(max_length=1024, blank=True, null=True)
    industry = models.CharField(max_length=1024, blank=True, null=True)

LOCALE_CHOICES = (
    ('en', _('english')),
    ('jp', _('japanese')),
)


class InitiativeGroup(models.Model):
    guid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=1024)
    class Meta:
        verbose_name = _('Initiative Group')
        verbose_name_plural = _('Initiative Groups')

class Initiative(models.Model):
    guid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=1024)
    slug = models.SlugField()
    details = models.TextField(null=True)
    locale = models.CharField(max_length=1024, choices=LOCALE_CHOICES, verbose_name=_('experiance locale'))
    group = models.ForeignKey(InitiativeGroup, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _('Initiative')
        verbose_name_plural = _('Initiatives')


class InitiativeImage(models.Model):
    guid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    initiative = models.ForeignKey(Initiative, on_delete=models.CASCADE)
    image_source = models.ImageField(upload_to='initiative-source-images')
    image = ProcessedImageField(
            upload_to='initiative-images',
            processors=[ResizeToFill(1280, 960)],
            format='JPEG', options={'quality': 60})
    image_type = models.CharField(max_length=1024)
    primary = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.host.name

    class Meta:
        verbose_name = _('Initiative Image')
        verbose_name_plural = _('Initiative Images')

@receiver(post_save, sender=InitiativeGroup)
def sync_initiative_group(sender: 'cls', instance: InitiativeGroup, created: bool, **kwargs):
    if created:
        for locale, rest in LOCALE_CHOICES:
            Initiative.objects.create(
                    title=f'{instance.name} title',
                    details=f'{instance.name} details',
                    group=instance,
                    locale=locale)

class Establishment:
    guid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=1024)
    address = models.TextField()
    website = models.CharField(max_length=1024)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _('Establishment')
        verbose_name_plural = _('Establishments')