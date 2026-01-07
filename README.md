
#  Simple password Generator & Evaluator (Python):

This project is a learning-oriented password generator and robustness evaluator,
designed to document my progression in Python development, code structuring,
and security-related reasoning.

The goal is not to provide a production-ready security tool,
but to iteratively build and improve a coherent project.

All content below refers to the v0.3 :

## Current Features:

- Random password generation
- User-provided password evaluation
- Basic robustness estimation (3 levels)
- Modular architecture:
  - `random_password_generation.py`
  - `robustness_evaluator.py`
  - `main.py`

## Design Choices:

- The project is intentionally split into multiple modules to ensure
  separation of concerns and future extensibility.
- The robustness evaluator currently relies on simple heuristics
  (length, character diversity).
- No entropy-based or probabilistic model is used at this stage.

## Known Limitations:

- The robustness evaluation is rudimentary and not cryptographically accurate
- No entropy calculation or real-world attack modeling yet
- UI is minimal and console-based

## Planned Improvements:

- Implement entropy-based password strength estimation
- Add configurable password policies
- Improve UI clarity and user feedback
- Add automated tests
- Refactor evaluator into a more extensible scoring system

## Project Intent

This repository serves as a portfolio project to demonstrate:
- Progressive learning
- Code structuring and maintainability
- Security-related reasoning
- Ability to iterate on a project over time
- 
## Versions

This project is versioned using Git tags.

- `v0.1` — first working prototype
- `v0.2` — functional password generator, seperation of features in module
- `v0.3` — Command-based UI, standardized docstring, extensible main architecture

Older versions can be accessed via GitHub tags.
