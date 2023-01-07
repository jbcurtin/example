#!/usr/bin/env bash

set -e
mkdir -p $USER_HOME
useradd --system --shell /bin/bash --home-dir $USER_HOME $USERNAME
chown $USERNAME:$USERNAME $USER_HOME
