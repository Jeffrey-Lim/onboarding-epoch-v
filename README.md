# Onboarding Team Epoch V

A practice repository for the new engineers of Team Epoch V.

[![Epoch](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FJeffrey-Lim%2Fepoch-dvdscreensaver%2Fmaster%2Fbadge.json)](https://teamepoch.ai/)
[![Python Version](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![Rye](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/rye/main/artwork/badge.json)](https://rye-up.com)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/Jeffrey-Lim/onboarding-epoch-v/main.svg)](https://results.pre-commit.ci/latest/Jeffrey-Lim/onboarding-epoch-v/main)
[![codecov](https://codecov.io/gh/Jeffrey-Lim/onboarding-epoch-v/graph/badge.svg?token=uZo7ykrgXY)](https://codecov.io/gh/Jeffrey-Lim/onboarding-epoch-v)

## Getting started

Make sure [Rye](https://rye-up.com/guide/installation/) is installed on your machine first. Then run:

```bash
rye sync
```

Alternatively, you can install the dependencies from `requirements-dev.lock` using the following command:

```bash
pip install -r requirements-dev.lock
```

## pre-commit

This repository uses [pre-commit](https://pre-commit.com/) for code quality checks and auto-formatting.
To install the pre-commit hooks, run:

```bash
pre-commit install
```

To run the pre-commit checks on all files, run:

```bash
pre-commit run --all-files
```
