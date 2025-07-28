import uuid
from django.db import models

class WaitlistEntry(models.Model):
    """Represents a single user signup on the waitlist."""
    email = models.EmailField(unique=True)
    school_domain = models.CharField(max_length=255, blank=True)
    referral_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    # --- NEW FIELD ---
    # This links a user to the person who referred them.
    referred_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='referrals')
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Waitlist Entry"
        verbose_name_plural = "Waitlist Entries"
        ordering = ['created_at'] # Order by creation time

    def __str__(self):
        return self.email
