# Squad Decisions

## Active Decisions

### Migrate to pyproject.toml

**Context**
Issue #59 flagged `setup.py develop` as deprecated. Modern Python tooling encourages `pyproject.toml` for project metadata and configuration.

**Decision**
- Moved all metadata from `setup.py` to `pyproject.toml`.
- Reduced `setup.py` to a minimal shim (`from setuptools import setup; setup()`).
- Updated `Makefile` and GitHub Actions workflows to use:
  - `pip install -e .` for editable installs.
  - `python -m build` for packaging.
- Updated release workflows to patch version in `pyproject.toml`.

**Consequences**
- Standardized build process.
- Removed deprecated warnings.
- Release process now depends on `pyproject.toml` structure.

### Python Version Policy for Release Workflows

**Date:** 2025-05-28
**Author:** Deckard
**Status:** Proposed

**Context**
PR #92 attempted to update release and quality gate workflows to use Python 3.14 (currently alpha/development).

**Decision**
- We will **not** use pre-release Python versions (alpha/beta/rc) for:
  - Release workflows (`release.yml`)
  - Pre-release workflows (`pre-release.yml`)
  - Quality gates (`sonar-cloud.yml`, `codecov.yml`)
- These critical paths must run on stable, supported Python versions (currently 3.8 - 3.13).
- Experimental versions may be added to the test matrix in `build-for-os.yml` but must not be the primary runner.

**Consequences**
- PR #92 needs to be revised or closed.
- Stability of releases is prioritized over bleeding-edge support.

### PR Review Strategy for #88 and #87

**Date:** 2023-10-25
**Author:** Rachael
**Status:** Decided

**Context**
PR #88 (Fix warnings) includes bug fixes, test improvements, and also the dependency update from PR #87 (Artifacts v7).

**Decision**
- Approve PR #88 as the primary merge candidate. It encompasses the fixes and the dependency update.
- Approve PR #87 but note redundancy. If #88 lands first, #87 is obsolete.

**Rationale**
- PR #88 is more comprehensive and fixes actual bugs affecting user experience.
- The duplication of the dependency update is acceptable and simplifies the merge process if #88 goes in first.

### Verification: pyproject.toml Migration

**Status:** Verified / Passed

**Findings**
- `pytest` passed (727 tests).
- `python -m build` successfully created sdist and wheel.
- `pip install -e .` works as expected.
- `setup.py` shim is functioning correctly.

**Recommendation**
- Proceed with `pyproject.toml` as the source of truth.
- Consider removing `setup.py` entirely in a future major release if editable install support via `pyproject.toml` (PEP 660) is fully adopted by all team tooling.

## Governance

- All meaningful changes require team consensus
- Document architectural decisions here
- Keep history focused on work, decisions focused on direction
