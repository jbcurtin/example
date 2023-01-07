FROM debian:bullseye as django-base

RUN export LC_ALL="en_US.UTF-8"
RUN export LC_CTYPE="en_US.UTF-8"
RUN export DEBIAN_FRONTEND="noninteractive"

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install \
    apt-transport-https ca-certificates curl software-properties-common \
    git htop build-essential zlib1g-dev libffi-dev redis-tools libffi-dev lzma libbz2-dev liblzma-dev \
    libreadline-dev sqlite3 libsqlite3-dev virtualenv make build-essential libssl-dev zlib1g-dev libbz2-dev \
    libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
    xz-utils tk-dev libffi-dev liblzma-dev git python3-dev redis redis-server vim \
    libgdal-dev \
    -y
RUN apt-get update
RUN apt-get upgrade -y

RUN sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
RUN apt-get update
RUN apt-get install postgresql-server-dev-all -y
# RUN apt-get install libmariadbclient-dev -y
RUN apt-get install libmariadb-dev -y
# RUN apt-get install libmariadb3 -y
RUN apt-get update

ARG USER_HOME=/home/wonderful
ARG USERNAME=wonderful

COPY ./build-tools /opt/build-tools
# Create user home
RUN bash /opt/build-tools/create-user.sh
USER ${USERNAME}
WORKDIR ${USER_HOME}

# Install PYENV
RUN bash /opt/build-tools/install-pyenv.sh
ENV PYENV_ROOT ${USER_HOME}/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH

FROM django-base as sustainability-page-backend

ARG USER_HOME=/home/sustainability-page
ARG USERNAME=sustainability-page

# Service EntryPoint
FROM sustainability-page-backend

ARG USER_HOME=/home/sustainability-page
ARG USERNAME=sustainability-page

# WORKDIR /opt/frontend
# COPY --from=sustainability-page-frontend /opt/src/sustainability-page-frontend .

WORKDIR /opt/backend
COPY --chown=${USERNAME}:${USERNAME} ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt
RUN pip install gunicorn
COPY --chown=${USERNAME}:${USERNAME} ./sustainability_page .
COPY --chown=${USERNAME}:${USERNAME} ./build-tools/migrate-and-run-service.sh .

ENV MIGRATE_DB=
ENV PSQL_ENV=
ENV LEGACY_ENV=
ENV SERVE_FE=no
ENTRYPOINT bash ./migrate-and-run-service.sh
