pip install uv
uv venv
.venv\Scripts\activate
uv pip install -r requirements.txt
cd main
python manage.py runserver