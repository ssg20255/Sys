# Order Management System (Flask)

A full-featured Order Management System built with Flask, SQLite (default), Jinja templates, Bootstrap, and JavaScript.
Features:
- Single-page Dashboard with filters, search, and export to Excel.
- Multi-step Order Form with dynamic item addition and autosave (draft per user).
- Two-panel live template preview with real-time updates and PDF export.
- Role-based access: Admin, CSE, PE, Customer, Management.
- Notifications via Email and Telegram (configurable per user).
- Versioning and Admin revert support.
- Multi-language support (English + Arabic). Numbers always use English numerals.
- Error-proof fallbacks: PDF/Excel/Notifications degrade gracefully when dependencies or credentials are missing.

This repository is designed to run out-of-the-box on Replit and deploy on PythonAnywhere.

--------------------------------------------------------------------------------
Quick start (local / Replit / PythonAnywhere)

1. Create a virtualenv (optional) and install requirements:
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

2. Copy `.env.example` to `.env` and edit values (email SMTP, telegram token/chat_id optional).
   On PythonAnywhere, configure environment variables via the web UI.

3. Initialize database and create default accounts:
   python init_db.py

   Default accounts created:
   - Admin: admin@example.com / password: adminpass
   - CSE: cse@example.com / password: csepass
   - PE: pe@example.com / password: pepass
   - Customer: customer@example.com / password: custpass
   - Management: mgmt@example.com / password: mgmtpass

4. Run the app:
   flask run
   or
   python run.py

5. Open http://127.0.0.1:5000 and login.

--------------------------------------------------------------------------------
Deploy notes

- Replit: import the project, set environment variables (SECRET_KEY etc.), run `python run.py`.
- PythonAnywhere: upload files, configure WSGI to point to `run.app`, set environment variables, and ensure static files are served.

--------------------------------------------------------------------------------
Files of interest

- run.py: entry point.
- init_db.py: create DB schema and seed users.
- app/: Flask application package (models, views, templates, static assets).
- app/utils.py: helpers for PDF, Excel, notifications (with robust fallbacks).
- requirements.txt: Python dependencies.

--------------------------------------------------------------------------------
Important design choices & fallbacks

- PDF: tries WeasyPrint first. If missing, falls back to xhtml2pdf (pisa). If both fail, provides HTML download fallback.
- Excel: tries `pandas` + `openpyxl`. If missing, serves CSV as fallback.
- Emails: uses Flask-Mail; if SMTP misconfigured, logs to console and stores notification in DB.
- Telegram: calls Telegram Bot API using `requests`; if not configured, logs to console and stores notification in DB.
- Autosave: saved every few seconds as the user edits; drafts visible only to author and Admin.
- Versioning: every autosave stores a version snapshot for Admin browsing and revert.

--------------------------------------------------------------------------------
Security notes

- Change default passwords before production.
- SECRET_KEY must be set in environment.
- For production, use PostgreSQL/MySQL; set DATABASE_URL env var and the app will use it.

--------------------------------------------------------------------------------
Support & troubleshooting

If any feature fails due to missing packages or external credentials, the system will provide a clear fallback and log the error to `app/logs/error.log`. Check console logs for details.

--------------------------------------------------------------------------------
License

MIT
