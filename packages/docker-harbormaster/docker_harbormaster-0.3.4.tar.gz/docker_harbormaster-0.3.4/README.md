Harbormaster
============

Do you have apps you want to deploy to a server, but Kubernetes is way too much?
Harbormaster is for you.

Harbormaster is a small and simple container orchestrator that lets you easily deploy
multiple Docker-Compose applications on a single host.

It does this by taking a list of git repository URLs that contain Docker
Compose files and running the Compose apps they contain. It will also handle
updating/restarting the apps when the repositories change.

Please [visit the documentation](https://harbormaster.readthedocs.io/en/latest/) for
more details.


## Rationale

Do you have a home server you want to run a few apps on, but don't want everything to
break every time you upgrade the OS? Do you want automatic updates but don't want to buy
an extra 4 servers so you can run Kubernetes?

Do you have a work server that you want to run a few small services on, but don't want
to have to manually manage it? Do you find that having every deployment action be in
a git repo more tidy?

Harbormaster is for you.

At its core, Harbormaster takes a YAML config file with a list of git repository URLs
containing Docker Compose files, clones/pulls them, and starts the services they
describe.

You run Harbormaster on a timer, pointing it to a directory, and it updates all the
repositories in its configuration, and restarts the Compose services if they have
changed. That's it!

It also cleanly stores data for all apps in a single `data/` directory, so you always
have one directory that holds all the state, which you can easily back up and restore.

See more details in [the documentation](https://harbormaster.readthedocs.io/en/latest/).

# Changelog


## v0.3.4 (2023-07-31)

### Features

* Add the `HM_` vars to the environment so they can be used in Compose v2 files. [Stavros Korokithakis]

### Fixes

* Fix wrong paths when launching Docker Compose. [Stavros Korokithakis]


## v0.3.3 (2023-07-23)

### Fixes

* Add missing crond invocation back. [Stavros Korokithakis]

* Don't complain about the directory if we restart the container. [Stavros Korokithakis]


## v0.3.2 (2023-07-23)

### Fixes

* Fix tests. [Stavros Korokithakis]

* Fix the Harbormaster Docker container. [Stavros Korokithakis]

* Fix issue with the Harbormaster Docker image not being able to find the data dir. [Stavros Korokithakis]

* Add docker-cli-compose to the Dockerfile. [Stavros Korokithakis]


## v0.3.1 (2023-07-22)

### Features

* Add git-crypt to the Docker image. [Stavros Korokithakis]

### Fixes

* Change Compose filename. [Stavros Korokithakis]

* Don't restart apps when their configuration hasn't been updated. [葛上昌司]

* Move the --version command to the right place. [Stavros Korokithakis]


## v0.3.0 (2023-03-01)

### Features

* Add docker image with webhook support. [Jonas Seydel]

### Fixes

* Upgrade Click (fixes #9) [Stavros Korokithakis]

* Be more defensive when loading the config. [Stavros Korokithakis]

* Fix the configuration directory having the wrong relative path base (fixes #12) [Stavros Korokithakis]


