from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import WaitlistForm
from .models import WaitlistEntry

# This data defines the schools we recognize for custom UI.
# It should be kept in a single source of truth, like here in the views.
SCHOOL_DATA = {
    'harvard.edu': {'name': 'Harvard', 'logo': 'logos/harvard.png'},
    'stanford.edu': {'name': 'Stanford University', 'logo': 'logos/stanford.png'},
    'mit.edu': {'name': 'Massachusetts', 'logo': 'logos/mit.png'},
    # ... Add your other 18 schools here ...
    'yale.edu': {'name': 'Yale University', 'logo': 'logos/yale.png'}
}
def waitlist_signup_view(request):
    ref_code = request.GET.get('ref')
    referrer = None
    if ref_code:
        try:
            referrer = WaitlistEntry.objects.get(referral_code=ref_code)
        except WaitlistEntry.DoesNotExist:
            referrer = None

    if request.method == 'POST':
        form = WaitlistForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.school_domain = entry.email.split('@')[1]
            # --- NEW: Link the new user to the referrer if they exist ---
            if referrer:
                entry.referred_by = referrer
            entry.save()
            
            position = entry.id 
            referral_code = entry.referral_code

            success_url = reverse('success_page')
            return redirect(f'{success_url}?domain={entry.school_domain}&pos={position}&ref={referral_code}')
    else:
        form = WaitlistForm()

    waitlist_count = WaitlistEntry.objects.count()

    context = {
        'form': form,
        'school_data': SCHOOL_DATA,
        'waitlist_count': waitlist_count,
        'ref_code': ref_code, 
    }
    return render(request, 'index.html', context)

def success_page_view(request):
    domain = request.GET.get('domain')
    position = request.GET.get('pos')
    referral_code = request.GET.get('ref') # Get referral code from URL
    school_info = SCHOOL_DATA.get(domain)
    
    # Construct the full referral link
    referral_link = request.build_absolute_uri(reverse('waitlist_signup')) + f'?ref={referral_code}'

    context = {
        'school': school_info,
        'position': position,
        'referral_link': referral_link,
    }
    return render(request, 'success.html', context)
