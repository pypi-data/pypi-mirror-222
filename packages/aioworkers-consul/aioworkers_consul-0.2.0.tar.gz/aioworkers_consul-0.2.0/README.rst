aioworkers-consul
=================

.. image:: https://img.shields.io/pypi/v/aioworkers-consul.svg
  :target: https://pypi.org/project/aioworkers-consul

.. image:: https://github.com/aioworkers/aioworkers-consul/workflows/Tests/badge.svg
  :target: https://github.com/aioworkers/aioworkers-consul/actions?query=workflow%3ATests

.. image:: https://codecov.io/gh/aioworkers/aioworkers-consul/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/aioworkers/aioworkers-consul
  :alt: Coverage

.. image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v0.json
  :target: https://github.com/charliermarsh/ruff
  :alt: Code style: ruff

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
  :target: https://github.com/psf/black
  :alt: Code style: black

.. image:: https://img.shields.io/badge/types-Mypy-blue.svg
  :target: https://github.com/python/mypy
  :alt: Code style: Mypy

.. image:: https://readthedocs.org/projects/aioworkers-consul/badge/?version=latest
  :target: https://github.com/aioworkers/aioworkers-consul#readme
  :alt: Documentation Status

.. image:: https://img.shields.io/pypi/pyversions/aioworkers-consul.svg
  :target: https://pypi.org/project/aioworkers-consul
  :alt: Python versions

.. image:: https://img.shields.io/pypi/dm/aioworkers-consul.svg
  :target: https://pypi.org/project/aioworkers-consul

.. image:: https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg
  :alt: Hatch project
  :target: https://github.com/pypa/hatch

About
=====

Integration with `Hashicorp Consul <https://www.consul.io>`_.

Use
---

.. code-block:: yaml

    consul:
      host: localhost:8500  # optional
      service:              # optional
        name: my
        tags:
          - worker


Development
-----------

Check code:

.. code-block:: shell

    hatch run lint:all


Format code:

.. code-block:: shell

    hatch run lint:fmt


Run tests:

.. code-block:: shell

    hatch run pytest


Run tests with coverage:

.. code-block:: shell

    hatch run cov
