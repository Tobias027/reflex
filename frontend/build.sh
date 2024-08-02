source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
reflex init
API_URL=http://app.example.com:8000 reflex export --frontend-only
rm -rf public
unzip frontend.zip -d public
rm -f frontend.zip
deactivate