# ADR-01: Development Environment

**Status:** Accepted

## Context

This project aims to build a small RAG-based study assistant for CCNA preparation while exploring AI Engineering concepts.

The development environment should be simple, reproducible, and suitable for a Python-based CLI application.

## Decision

We will use Python 3.12, Visual Studio Code, and `uv` for dependency management and virtual environment creation.

Dependencies will be declared in `requirements.txt` and pinned in `requirements-lock.txt`.

Git and GitHub will be used for version control.

## Rationale

Python provides a mature ecosystem for LLM integration, embeddings, and vector search.

Python 3.12 offers a stable development environment with broad library compatibility.

VS Code is lightweight, supports Python, Git, and Docker, and provides an opportunity to gain experience with a different IDE.

`uv` offers fast dependency installation and reproducible environments through dependency locking.

A project-specific `.venv` keeps dependencies isolated from other Python projects.

## Alternatives Considered

- **PyCharm:** Excellent Python IDE, but VS Code was chosen to gain experience with a more versatile editor.
- **Python 3.13/3.14:** Newer versions, but Python 3.12 was preferred for its established compatibility with AI libraries.
- **pip + venv:** A valid standard approach, but `uv` offers faster dependency management and integrated locking.
- **Poetry:** Provides comprehensive project management, but introduces unnecessary configuration for this small project.
- **Conda:** Useful for scientific computing environments, but adds complexity that is not needed here.

## Consequences

The environment is simple and suitable for local development.

VS Code requires some initial configuration and Python extensions.

Dependencies and the virtual environment must be managed explicitly, but this provides greater understanding and control over the development setup.