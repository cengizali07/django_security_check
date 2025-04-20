# 🔐 Django Güvenlik Kontrol Scripti

Bu script, Django projelerinizin güvenlik ayarlarını otomatik olarak denetler ve olası açıklara karşı sizi uyarır.  
Django'nun önerdiği `deploy` ayarları da dahil olmak üzere birçok güvenlik politikasını kontrol eder.

---

## 🚀 Özellikler (Türkçe)

✅ `DEBUG = False` kontrolü  
✅ `ALLOWED_HOSTS` düzgün ayarlanmış mı?  
✅ `SECRET_KEY` güvende mi?  
✅ HTTPS ve HSTS zorunluluğu  
✅ CSRF & Session cookie güvenliği  
✅ Parola güvenliği politikaları  
✅ X-Frame-Options kontrolü  
✅ Content-Security-Policy var mı?

---

## ⚙️ Kullanım (Türkçe)

1. Django projenizin dizinine bu script'i yerleştirin.
2. Script'te `projeadi.settings` satırını kendi `settings.py` konumunuza göre düzenleyin.
3. Aşağıdaki komutu çalıştırın:

```bash
python django_security_check.py


🌍 Django Security Check Script

This script automatically audits your Django project's security configurations
and warns you about potential vulnerabilities.

It checks common security settings Django recommends for production environments.
🚀 Features (English)

✅ Ensures DEBUG = False
✅ Checks if ALLOWED_HOSTS is properly set
✅ Validates the SECRET_KEY usage
✅ HTTPS enforcement & HSTS support
✅ CSRF & Session cookie security
✅ Password policy checks
✅ X-Frame-Options validation
✅ Checks for Content-Security-Policy middleware
⚙️ Usage (English)

    Place this script inside your Django project.

    Set the correct DJANGO_SETTINGS_MODULE (e.g. "yourproject.settings").

    Run it via:

python django_security_check.py
