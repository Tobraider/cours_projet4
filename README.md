ETAPE POUR EXECUTER LE SCRIPT
1. Installation et execution de l'environnement virtuel :

    Pour windows
    sh`python -m venv env`
    `.\env\Scripts\activate`
    `pip install -r .\requirements.txt`

    (Linux/Mac)
    sh`python3 -m venv env`
    `.` `source env/bin/activate`
    `pip install -r requirements.txt`


2. Execution du script :

    sh`.\proj.py`


3. Une fois le script terminer vous pouvez quitter l'environnement virutel :

    sh`deactivate`


Pour lancer flake8 : 
    sh `flake8 --format=html --htmldir=flake-report`