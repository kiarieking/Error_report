# Introduction

Log Monitor is a lightweight Python script designed to automatically scan system and application log files, detect predefined error patterns, and extract relevant entries for reporting or alerting.

### Clone this repository into your prffered directory

    git clone https://github.com/kiarieking/Error_report.git

### Create virtual environment

Install curl and pyenv if you don't have them already. Note you can use other virtual environment tools.

    sudo apt install curl
    curl https://pyenv.run | bash

Add this to the end of your $HOME/.bashrc or $HOME/.zshrc file:

    export PYENV_ROOT="$HOME/.pyenv"
    command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"

Reload terminal to apply the changes.

Create the virtual environment. Use python 3.8+ as recommended.

    pyenv install 3.11.3
    pyenv virtualenv 3.8.3 test_env

### Install Requirements

    pip install -r requirements.txt

### Setup .env file

Create a .env file and add the following constants.

    SENDER_EMAIL = "your sender email"
    RECIPIENT_EMAIL = "your receipient email"
    APP_PASSWORD = "your gmail app password"
    POSTGRES_LOG = "/var/log/postgresql/postgresql-17-main.log"
    NGINX_LOG = "/var/log/nginx/access.log"
    ODOO_LOG = "/var/log/odoo15/odoo15.log"
    OUTPUT_FILE = "your output log file that will be sent as report"

N.B the script is focused on postgres,nginx and odoo logs. This can be adjusted depending on your needs.

### Run the script

    python3 /path/to/log_notifier/log_filter.py
