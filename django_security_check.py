import os
import django
from django.conf import settings

def check_django_security():
    issues = []

    if settings.DEBUG:
        issues.append("❌ DEBUG mode is ON. Turn it OFF in production.")

    if not settings.ALLOWED_HOSTS or "*" in settings.ALLOWED_HOSTS:
        issues.append("❌ ALLOWED_HOSTS is not set properly.")

    if "django-insecure" in settings.SECRET_KEY:
        issues.append("❌ SECRET_KEY appears to be a dev key.")
    elif len(settings.SECRET_KEY) < 30:
        issues.append("⚠️ SECRET_KEY might be too short.")

    if not getattr(settings, "SECURE_SSL_REDIRECT", False):
        issues.append("❌ SECURE_SSL_REDIRECT is not enabled.")

    if not getattr(settings, "SESSION_COOKIE_SECURE", False):
        issues.append("❌ SESSION_COOKIE_SECURE is not set.")

    if not getattr(settings, "CSRF_COOKIE_SECURE", False):
        issues.append("❌ CSRF_COOKIE_SECURE is not set.")

    if getattr(settings, "SECURE_HSTS_SECONDS", 0) < 31536000:
        issues.append("❌ SECURE_HSTS_SECONDS is too low or not set.")

    if not getattr(settings, "X_FRAME_OPTIONS", "") in ["DENY", "SAMEORIGIN"]:
        issues.append("❌ X_FRAME_OPTIONS is not set securely.")

    if not getattr(settings, "AUTH_PASSWORD_VALIDATORS", []):
        issues.append("❌ No password validators set.")

    if getattr(settings, "SESSION_COOKIE_AGE", 999999) > 3600 * 4:
        issues.append("⚠️ SESSION_COOKIE_AGE is quite high. Consider reducing it.")

    if "csp.middleware.CSPMiddleware" not in settings.MIDDLEWARE:
        issues.append("⚠️ Content-Security-Policy (CSP) middleware not active.")

    print("\n🔒 Django Security Check")
    print("=" * 30)
    if issues:
        for issue in issues:
            print(issue)
    else:
        print("✅ No major security issues detected. Well done!")

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projeadi.settings")  # Buraya kendi Django ayarlarını yaz
    django.setup()
    check_django_security()
