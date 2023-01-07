#!/usr/bin/env bash

set -e
git clone https://github.com/pyenv/pyenv.git $USER_HOME/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> $USER_HOME/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> $USER_HOME/.bashrc
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> $USER_HOME/.bashrc
source $USER_HOME/.bashrc
pyenv install 3.9.5
pyenv global 3.9.5
pip install -U setuptools
pip install -U pip
