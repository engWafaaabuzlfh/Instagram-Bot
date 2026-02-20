# Instagram Bot (Flask + Webhook)

مشروع تجريبي لبوت إنستغرام يعتمد على Webhook عبر `Flask` مع أمثلة بسيطة للتعامل مع Graph API.

## الملفات بعد إعادة التسمية

- `instagram_webhook_app.py`: التطبيق الرئيسي (Webhook + استقبال الرسائل + رفع ملف نصي).
- `fetch_facebook_pages.py`: مثال لجلب الصفحات/الحسابات المرتبطة عبر Graph API.
- `instagram_messaging_examples.py`: أمثلة لجلب المحادثات وإرسال رسالة.
- `templates/upload_panel.html`: واجهة HTML بسيطة لرفع ملف.

## المتطلبات

- Python 3.9+
- مكتبات بايثون:
  - `flask`
  - `requests`
  - `pillow`

يمكن التثبيت عبر:

```bash
pip install flask requests pillow
```

## إعداد القيم الحساسة

عدّل القيم داخل `instagram_webhook_app.py`:

- `VERIFY_TOKEN`
- `PAGE_ACCESS_TOKEN`

وكذلك عدّل مفاتيح الوصول داخل:

- `fetch_facebook_pages.py`
- `instagram_messaging_examples.py`

## التشغيل

لتشغيل التطبيق الرئيسي:

```bash
python instagram_webhook_app.py
```

سيعمل افتراضيًا على المنفذ `5000`.

## ملاحظات

- التطبيق يستورد `gemini_pil`، لذا يجب أن يكون الملف/الموديول موجودًا في المشروع.
- ملفات الأمثلة تحتوي Tokens ثابتة حاليًا، والأفضل نقلها إلى متغيرات بيئة قبل الاستخدام في الإنتاج.
