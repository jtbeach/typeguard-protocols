# Install deps (requires poetry)

::

  poetry install

# Verify that mypy works

::

  poetry run mypy tests/ typeguard_test

# Verify that test success with no typeguard

::

  poetry run py.test tests/test_impl.py


# Verify that test fails with typeguard

::

  poetry run py.test --typeguard=typeguard_test tests/test_impl.py

