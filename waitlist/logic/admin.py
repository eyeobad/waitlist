from django.contrib import admin
from .models import WaitlistEntry

@admin.register(WaitlistEntry)
class WaitlistEntryAdmin(admin.ModelAdmin):
    """Admin view for managing waitlist entries."""
    list_display = ('id', 'email', 'school_domain', 'referred_by', 'referral_count', 'created_at', 'is_verified')
    list_filter = ('school_domain', 'is_verified', 'created_at')
    search_fields = ('email', 'school_domain', 'referral_code__exact')
    readonly_fields = ('created_at', 'referral_code', 'referral_count')
    list_display_links = ('id', 'email')
    # --- NEW: Make the referred_by field a link for easy navigation ---
    raw_id_fields = ('referred_by',)

    @admin.display(description='Referral Count')
    def referral_count(self, obj):
        """Calculates and displays the number of successful referrals."""
        return obj.referrals.count()
