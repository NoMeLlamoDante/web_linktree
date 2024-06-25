.venv/Scripts/activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
refle init
reflex export --frontend-only
rm -rf public
unzip frontend.zip -d public
rm -f frontend.zip
deactivate