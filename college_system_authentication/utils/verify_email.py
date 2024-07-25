from datetime import timezone
from django.shortcuts import redirect, render
from college_system_authentication.models import UserAccount


def verify_email(request, token):
    try:
        user = UserAccount.objects.get(token_email_validation=token)
        if user.token_expiration < timezone.now():
            return render(request, 'authentication/verification_failed.html', {'error': 'Token expirado'})
        user.email_verified = True  # Asegúrate de tener un campo para esto en tu modelo
        user.save()
        return redirect('login')
    except UserAccount.DoesNotExist:
        return render(request, 'authentication/verification_failed.html', {'error': 'Token inválido'})