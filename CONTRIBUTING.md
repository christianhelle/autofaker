# Contributing to AutoFaker

Thank you for your interest in contributing to AutoFaker! This document provides guidelines and information for contributors to help maintain code quality and consistency.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Code Style and Patterns](#code-style-and-patterns)
- [Testing Guidelines](#testing-guidelines)
- [Pull Request Guidelines](#pull-request-guidelines)
- [Documentation Guidelines](#documentation-guidelines)
- [Issue Reporting](#issue-reporting)

## Code of Conduct

Please be respectful and considerate in all interactions. We aim to maintain a welcoming and inclusive environment for all contributors.

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/your-username/autofaker.git
   cd autofaker
   ```
3. Add the upstream repository:
   ```bash
   git remote add upstream https://github.com/christianhelle/autofaker.git
   ```

## Development Setup

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. Install development dependencies:
   ```bash
   make prepare
   ```

2. Install the package in development mode:
   ```bash
   python setup.py develop --user
   ```
   
   **Note**: If you encounter permission errors with the Makefile targets, you can run commands individually:
   ```bash
   pip install -r requirements.txt
   python setup.py develop --user
   ```

### Available Make Targets

- `make prepare`: Install development dependencies
- `make debug`: Install package in development mode
- `make test`: Run all tests with coverage
- `make package`: Build distribution packages
- `make all`: Run complete build pipeline

## Code Style and Patterns

### Use Existing Code Patterns

When contributing, please follow the established patterns in the codebase:

#### 1. Class Structure
Follow the existing patterns for creating data generators:

```python
# Example from existing codebase
class ExampleGenerator:
    def create(self, t: type, use_fake_data: bool = False):
        # Implementation here
        pass
```

#### 2. Decorator Patterns
When adding new decorators, follow the existing pattern:

```python
def example_decorator(*types: object, use_fake_data: bool = False):
    def decorator(function):
        def wrapper(*args):
            # Implementation following existing pattern
            pass
        return wrapper
    return decorator
```

#### 3. Test Patterns
Use both unittest and pytest patterns as established:

```python
import unittest
from autofaker import Autodata, autodata

class ExampleTestCase(unittest.TestCase):
    def test_example_functionality(self):
        # Test implementation
        self.assertIsNotNone(result)

    @autodata(str, int)
    def test_with_decorator(self, text, number):
        # Test using decorator pattern
        self.assertIsInstance(text, str)
        self.assertIsInstance(number, int)
```

#### 4. Type Hints
Use type hints consistently, following existing patterns:

```python
from typing import List, Optional, Union

def create_example(data_type: type, count: int = 3) -> List[object]:
    # Implementation with proper type hints
    pass
```

#### 5. Docstrings
Include docstrings for public methods and classes:

```python
def create_anonymous_data(data_type: type) -> object:
    """
    Creates anonymous data for the specified type.
    
    Args:
        data_type: The type to create anonymous data for
        
    Returns:
        An instance of the specified type with anonymous data
    """
    pass
```

### Naming Conventions

- Use snake_case for functions and variables
- Use PascalCase for classes
- Use descriptive names that reflect functionality
- Follow existing naming patterns in the codebase

### Import Organization

Organize imports following the existing pattern:
1. Standard library imports
2. Third-party imports
3. Local imports

```python
import unittest
from typing import List
from dataclasses import dataclass

import pandas

from autofaker import Autodata
```

## Testing Guidelines

### Test Coverage Requirements

- All new functionality must include comprehensive tests
- Maintain or improve existing test coverage
- Tests should cover both success and failure scenarios

### Test Patterns

1. **Unit Tests**: Use unittest.TestCase for traditional unit testing
2. **Decorator Tests**: Use the @autodata and @fakedata patterns
3. **Integration Tests**: Test complete workflows
4. **Exception Tests**: Test error conditions and edge cases

### Running Tests

```bash
# Run all tests
python -m pytest tests/ -v --cov --cov-report=term-missing

# Alternative: use make if you have proper permissions
make test

# Run specific test file
python -m pytest tests/test_specific_feature.py -v

# Run with coverage
python -m pytest tests/ -v --cov --cov-report=term-missing
```

### Test Organization

- Place tests in the `tests/` directory
- Name test files with `test_` prefix
- Group related tests in the same file
- Use descriptive test method names

## Pull Request Guidelines

### PR Description Requirements

**Pull Request descriptions must be as verbose as possible** and include:

#### Required Information

1. **Summary**: Clear, concise description of what the PR accomplishes
2. **Motivation**: Why this change is needed
3. **Changes Made**: Detailed list of all changes, including:
   - New features added
   - Bug fixes implemented
   - Code refactoring performed
   - Documentation updates
4. **Testing**: Description of how the changes were tested
5. **Breaking Changes**: Any backwards incompatible changes
6. **Additional Notes**: Any other relevant information

#### PR Description Template

```markdown
## Summary
[Provide a clear summary of the changes]

## Motivation
[Explain why this change is needed]

## Changes Made
- [ ] Feature A: Description of feature A
- [ ] Bug fix B: Description of bug fix B
- [ ] Documentation updates for X
- [ ] Added tests for Y

## Testing
- [ ] Added unit tests for new functionality
- [ ] Verified existing tests pass
- [ ] Tested on Python versions: [list versions]
- [ ] Manual testing performed: [describe scenarios]

## Breaking Changes
[List any breaking changes or write "None"]

## Additional Notes
[Any other relevant information]
```

### Before Submitting a PR

1. **Update Documentation**: If your changes affect user-facing functionality
2. **Run Tests**: Ensure all tests pass locally
3. **Check Coverage**: Verify test coverage is maintained
4. **Update README**: If adding new features or changing existing behavior
5. **Add Examples**: Include usage examples for new features

### PR Submission Process

1. Create a feature branch from main:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes following the established patterns

3. Test your changes thoroughly:
   ```bash
   python -m pytest tests/ -v --cov --cov-report=term-missing
   ```

4. Commit with descriptive messages:
   ```bash
   git commit -m "Add feature X with comprehensive tests"
   ```

5. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

6. Create a Pull Request with verbose description

## Documentation Guidelines

### Keep README Up to Date

**All changes that affect user-facing functionality must include README updates:**

1. **New Features**: Add examples and documentation
2. **API Changes**: Update existing examples
3. **New Supported Types**: Update the "Supported data types" section
4. **Installation Changes**: Update installation instructions

### Documentation Standards

- Use clear, concise language
- Include code examples for new features
- Ensure examples are tested and work correctly
- Update both README.md and docs/pypi.md if applicable

### Example Documentation

When adding new features, include examples like:

```python
# Create anonymous data using new feature
from autofaker import Autodata

result = Autodata.create_new_feature(YourClass)
print(f'Result: {result}')
```

## Issue Reporting

When reporting issues:

1. **Use Issue Templates**: Follow any provided templates
2. **Provide Context**: Include Python version, OS, and package version
3. **Include Examples**: Provide minimal reproducible examples
4. **Check Existing Issues**: Search for similar issues first

## Development Best Practices

1. **Small, Focused Changes**: Keep PRs focused on single features or fixes
2. **Maintain Backwards Compatibility**: Avoid breaking existing functionality
3. **Follow Existing Patterns**: Consistency is key
4. **Test Thoroughly**: Include comprehensive tests
5. **Document Changes**: Update documentation for user-facing changes

## Getting Help

If you need help or have questions:

1. Check existing documentation and issues
2. Create an issue with the "question" label
3. Be specific about what you're trying to accomplish

Thank you for contributing to AutoFaker! Your contributions help make this library better for everyone.