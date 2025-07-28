# فروشگاه آنلاین - مستندات فنی


## 🏪 معرفی پروژه

این پروژه یک فروشگاه آنلاین کامل است که با استفاده از فریم‌ورک Django توسعه یافته است. این سیستم شامل مدیریت محصولات، سبد خرید، پرداخت آنلاین، مدیریت کاربران و سایر قابلیت‌های ضروری یک فروشگاه الکترونیکی می‌باشد.

## 🛠 تکنولوژی‌های استفاده شده

### Backend
- **Django 3.2.8** - فریم‌ورک اصلی وب
- **Python 3.x** - زبان برنامه‌نویسی
- **SQLite** - پایگاه داده (قابل تغییر به PostgreSQL/MySQL)
- **Django MPTT** - مدیریت ساختار درختی دسته‌بندی‌ها
- **Treebeard** - مدیریت درخت‌های سلسله‌مراتبی

### Frontend
- **HTML5/CSS3** - ساختار و استایل صفحات
- **JavaScript** - تعاملات سمت کلاینت
- **Bootstrap** - فریم‌ورک CSS (بر اساس ساختار فایل‌ها)
- **Django Templates** - سیستم قالب‌بندی

### ابزارهای توسعه
- **Django Admin** - پنل مدیریت
- **Django Forms** - فرم‌های وب
- **Django ORM** - مدیریت پایگاه داده
- **Django Sessions** - مدیریت نشست‌ها

## 🏗 معماری سیستم

### الگوی معماری
این پروژه از الگوی **Model-View-Template (MVT)** Django استفاده می‌کند:

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Templates     │    │     Views       │    │     Models      │
│   (Presentation)│◄──►│   (Controller)  │◄──►│   (Data Layer)  │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### لایه‌های سیستم
1. **لایه ارائه (Presentation Layer)**
   - Templates HTML
   - Static Files (CSS, JS, Images)
   - Responsive Design

2. **لایه منطق کسب‌وکار (Business Logic Layer)**
   - Views
   - Forms
   - Custom Managers

3. **لایه داده (Data Layer)**
   - Models
   - Database
   - File Storage

## 📁 ساختار پروژه

```
eshop/
├── eshop/                     # تنظیمات اصلی پروژه
│   ├── settings.py           # تنظیمات Django
│   ├── urls.py               # URL های اصلی
│   ├── views.py              # View های اصلی
│   └── wsgi.py               # WSGI Configuration
├── eshop_account/            # مدیریت حساب کاربری
├── eshop_products/           # مدیریت محصولات
├── eshop_product_category/   # دسته‌بندی محصولات
├── eshop_order/              # مدیریت سفارشات
├── eshop_news/               # اخبار و مقالات
├── eshop_contact/            # تماس با ما
├── eshop_settings/           # تنظیمات سایت
├── eshop_brand/              # مدیریت برندها
├── eshop_tag/                # تگ‌های محصولات
├── eshop_sliders/            # اسلایدرهای صفحه اصلی
├── templates/                # قالب‌های HTML
├── assets/                   # فایل‌های استاتیک
│   ├── css/
│   ├── js/
│   ├── images/
│   └── fonts/
├── static_cdn/               # فایل‌های استاتیک تولید شده
└── manage.py                 # ابزار مدیریت Django
```

## 🚀 نصب و راه‌اندازی

### پیش‌نیازها
- Python 3.7+
- pip
- virtualenv (توصیه می‌شود)

### مراحل نصب

1. **کلون کردن پروژه**
```bash
git clone [repository-url]
cd eshop
```

2. **ایجاد محیط مجازی**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# یا
venv\Scripts\activate     # Windows
```

3. **نصب وابستگی‌ها**
```bash
pip install django==3.2.8
pip install django-mptt
pip install treebeard
pip install django-render-partial
```

4. **اجرای مایگریشن‌ها**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **ایجاد کاربر ادمین**
```bash
python manage.py createsuperuser
```

6. **اجرای سرور توسعه**
```bash
python manage.py runserver
```

### تنظیمات محیط
- فایل `settings.py` را برای تنظیمات محیط تولید ویرایش کنید
- متغیر `SECRET_KEY` را تغییر دهید
- `DEBUG = False` را برای محیط تولید تنظیم کنید
- `ALLOWED_HOSTS` را تنظیم کنید

## ✨ ویژگی‌های سیستم

### مدیریت محصولات
- ✅ افزودن، ویرایش و حذف محصولات
- ✅ مدیریت تصاویر محصولات
- ✅ دسته‌بندی سلسله‌مراتبی محصولات
- ✅ سیستم تگ‌گذاری
- ✅ مدیریت برندها
- ✅ جستجوی پیشرفته محصولات

### مدیریت سفارشات
- ✅ سبد خرید
- ✅ ثبت سفارش
- ✅ پیگیری وضعیت سفارش
- ✅ تاریخچه سفارشات

### سیستم کاربران
- ✅ ثبت‌نام و ورود
- ✅ پروفایل کاربری
- ✅ مدیریت اطلاعات شخصی

### محتوای سایت
- ✅ مدیریت اخبار و مقالات
- ✅ اسلایدرهای صفحه اصلی
- ✅ صفحه تماس با ما
- ✅ صفحه درباره ما

### امنیت
- ✅ احراز هویت کاربران
- ✅ محافظت CSRF
- ✅ اعتبارسنجی فرم‌ها
- ✅ مدیریت نشست‌ها

## 🔌 API ها

### URL های اصلی
- `/` - صفحه اصلی
- `/products/` - لیست محصولات
- `/news/` - اخبار و مقالات
- `/account/` - مدیریت حساب کاربری
- `/contact-us/` - تماس با ما
- `/admin/` - پنل مدیریت

### API های پرداخت
- `/request/` - ارسال درخواست پرداخت
- `/verify/` - تایید پرداخت

## 🔒 امنیت

### اقدامات امنیتی پیاده‌سازی شده
- **CSRF Protection**: محافظت در برابر حملات CSRF
- **Session Security**: مدیریت امن نشست‌ها
- **Password Validation**: اعتبارسنجی قوی رمز عبور
- **SQL Injection Protection**: محافظت در برابر تزریق SQL
- **XSS Protection**: محافظت در برابر حملات XSS

### توصیه‌های امنیتی
- تغییر `SECRET_KEY` در محیط تولید
- استفاده از HTTPS
- تنظیم `DEBUG = False` در محیط تولید
- محدود کردن `ALLOWED_HOSTS`
- استفاده از فایروال مناسب

## 🌐 نشر و استقرار

### محیط توسعه
```bash
python manage.py runserver
```

### محیط تولید
1. **تنظیمات سرور**
   - استفاده از WSGI Server (Gunicorn/uWSGI)
   - تنظیم Web Server (Nginx/Apache)
   - استفاده از CDN برای فایل‌های استاتیک

2. **تنظیمات پایگاه داده**
   - استفاده از PostgreSQL یا MySQL
   - تنظیم Connection Pooling
   - پشتیبان‌گیری منظم

3. **تنظیمات امنیتی**
   - استفاده از HTTPS
   - تنظیم Headers امنیتی
   - محدود کردن دسترسی‌ها

### متغیرهای محیطی
```bash
export SECRET_KEY="your-secret-key"
export DEBUG=False
export ALLOWED_HOSTS="your-domain.com"
export DATABASE_URL="postgresql://..."
```

## 📊 عملکرد و بهینه‌سازی

### بهینه‌سازی پایگاه داده
- استفاده از Index ها
- بهینه‌سازی Query ها
- استفاده از Select_related و Prefetch_related

### بهینه‌سازی Frontend
- فشرده‌سازی CSS و JavaScript
- بهینه‌سازی تصاویر
- استفاده از CDN

### مانیتورینگ
- لاگ‌گیری مناسب
- مانیتورینگ خطاها
- بررسی عملکرد

## 🤝 مشارکت

برای مشارکت در توسعه این پروژه:

1. Fork کردن پروژه
2. ایجاد Branch جدید
3. اعمال تغییرات
4. ارسال Pull Request

## 📞 پشتیبانی

برای دریافت پشتیبانی یا گزارش مشکلات:
- ایجاد Issue در GitHub
- تماس از طریق صفحه تماس با ما

## 📄 لایسنس

این پروژه تحت لایسنس [MIT License](LICENSE) منتشر شده است.

---


**نسخه**: 1.0.0 