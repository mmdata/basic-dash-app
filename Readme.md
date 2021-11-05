## Intro

Basic Dash app to predict sentiment. It is NOT ready for actual use!
To run localy:
- `python3 -m venv env`
- `source env/bin/activate`
- `python3 -m pip install -r requirements.txt`

Then you can run the app with the development server:
- `python3 app.py`
- Check http://127.0.0.1:8050/

Or you can run the app with gunicorn:
- `python3 -m gunicorn app:server`
- Check `http://127.0.0.1:8000`