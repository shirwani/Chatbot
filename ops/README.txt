#####################################################
# SETTING UP THE LOCAL DEV MACHINE TO RUN THE SCRIPTS
    brew install python@3.12
#####################################################
    cd Chatbot
    which python3 # -> shoud point to python 3.10 on the system
    python3 -m venv venv
    alias python="venv/bin/python3.12"
    alias pip="venv/bin/pip3.12"
    source venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
