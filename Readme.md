<!-- create virtual environment -->
<!-- first run this command -->
pip install uv
<!-- then run this -->
uv venv
.venv\Scripts\activate
uv pip install -r requirements.txt
cd main
python manage.py runserver