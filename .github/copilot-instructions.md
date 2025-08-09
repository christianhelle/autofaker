# AutoFaker Development Instructions

AutoFaker is a Python library designed to minimize the setup/arrange phase of unit tests by generating anonymous test data. It's inspired by AutoFixture and supports creating anonymous variables for built-in types, classes, dataclasses, and Pandas DataFrames.

Always reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.

## Working Effectively

### Bootstrap and Setup
- Check Python version: `python --version` (requires Python 3.8+)
- Install dependencies: `pip install -r requirements.txt` -- takes ~30 seconds
- Install package in development mode: `pip install -e . --user` -- takes ~7 seconds  
- **CRITICAL**: The Makefile `debug` target fails due to permission issues. Always use `pip install -e . --user` instead

### Running Tests 
- Run full test suite: `python -m pytest tests/ -v --cov --cov-report=xml --cov-report=term-missing` -- takes ~5 seconds. NEVER CANCEL.
- Run specific test file: `python -m pytest tests/test_specific_feature.py -v`
- Alternative: `make test` (but this fails due to the broken `debug` target)
- **556 tests** should pass with good coverage (~90%+)

### Building and Packaging
- Build distributions: `python setup.py sdist bdist_wheel` or `make package` -- takes ~1 second
- **NOTE**: Modern `python -m build` fails due to network timeouts in isolated environments
- Generated files go to `dist/` directory

### Validation Scenarios
Always test the core functionality after making changes:

#### Test Basic Data Generation
```python
from autofaker import Autodata
from dataclasses import dataclass
import datetime

# Test built-in types
print(f'string: {Autodata.create(str)}')
print(f'int: {Autodata.create(int)}')
print(f'datetime: {Autodata.create(datetime.datetime)}')

# Test dataclass
@dataclass
class TestData:
    id: int
    name: str
    
data = Autodata.create(TestData)
assert isinstance(data.id, int)
assert isinstance(data.name, str)
```

#### Test Fake Data Generation
```python
@dataclass
class PersonData:
    id: int
    first_name: str
    last_name: str
    email: str

person = Autodata.create(PersonData, use_fake_data=True)
# Should generate realistic fake names and emails
print(f'{person.first_name} {person.last_name} - {person.email}')
```

#### Test Decorator Functionality
```python
from autofaker import autodata, fakedata

class Calculator:
    def add(self, a: int, b: int) -> int:
        return a + b

@autodata(Calculator, int, int)
def test_calculator(calc, a, b):
    result = calc.add(a, b)
    assert result == a + b
```

#### Test DataFrame Creation
```python
from autofaker import Autodata

@dataclass
class DataRow:
    id: int
    name: str
    value: float

df = Autodata.create_pandas_dataframe(DataRow)
# Should create 3-row DataFrame with random data
assert len(df) == 3
```

## Key Project Structure

### Source Code (`src/autofaker/`)
- `autodata.py` - Main Autodata class entry point
- `generator.py` - Core data generation logic 
- `decorators.py` - @autodata and @fakedata decorators
- `builtins.py` - Built-in type generators (int, str, float, etc.)
- `dataframe.py` - Pandas DataFrame creation
- `fakes.py` - Fake data generation using Faker library
- `dates.py` - Date/datetime generators
- `enums.py` - Enum type support
- `literals.py` - typing.Literal support
- `factory.py` - Object factory pattern
- `attributes.py` - Class attribute handling
- `base.py` - Base classes and utilities

### Tests (`tests/`)
- `tests/` - unittest-style tests
- `tests/pytests/` - pytest-style tests  
- `tests/unittests/` - additional unittest files
- **556 total tests** covering all functionality

### Configuration Files
- `pyproject.toml` - Build system configuration
- `setup.py` - Package setup (legacy but required)
- `requirements.txt` - Development dependencies
- `Makefile` - Build targets (some broken due to permissions)

## Dependencies and Installation

### Core Dependencies
- `pandas` - DataFrame support
- `faker` - Fake data generation
- `typing_inspect` - Type introspection

### Development Dependencies  
- `pytest` - Test framework
- `pytest-cov` - Coverage reporting

### Installation Commands (All Validated)
```bash
# Install dependencies (30 seconds)
pip install -r requirements.txt

# Install in development mode (7 seconds) 
pip install -e . --user

# Run tests (5 seconds)
python -m pytest tests/ -v --cov --cov-report=xml --cov-report=term-missing

# Build package (1 second)
python setup.py sdist bdist_wheel
```

## Common Tasks

### After Making Code Changes
1. **ALWAYS** run the validation scenarios above to ensure functionality works
2. Run full test suite: `python -m pytest tests/ -v --cov --cov-report=xml --cov-report=term-missing`
3. Test the example code from README.md to ensure documentation stays accurate
4. Build package to verify no import errors: `python setup.py sdist bdist_wheel`

### Adding New Data Type Support
1. Check existing patterns in `builtins.py`, `dates.py`, `enums.py`
2. Add generator logic to appropriate file or create new module
3. Update `generator.py` to handle the new type
4. Add comprehensive tests in both `tests/` and `tests/pytests/`
5. Update README.md with examples if user-facing
6. Test with both anonymous and fake data modes

### Adding New Features
1. Follow existing patterns in decorators or core classes
2. Maintain backward compatibility
3. Add both unittest and pytest style tests
4. Test with real scenarios, not just unit tests
5. Update documentation and examples

## Timing Expectations and Warnings

- **Dependency installation**: ~30 seconds - NEVER CANCEL
- **Package installation**: ~7 seconds - NEVER CANCEL  
- **Test execution**: ~5 seconds - NEVER CANCEL
- **Package building**: ~1 second
- **Full validation**: ~1 minute total

## Known Issues and Workarounds

### Makefile Issues
- `make debug` fails with permission errors
- **Workaround**: Use `pip install -e . --user` instead
- `make test` depends on broken debug target
- **Workaround**: Use `python -m pytest` commands directly

### Build Tool Issues
- `python -m build` fails with network timeouts in isolated environments
- **Workaround**: Use `python setup.py sdist bdist_wheel` for packaging

### Setup.py Deprecation Warnings
- Modern Python shows deprecation warnings for setup.py usage
- This is expected and can be ignored - the package still builds correctly
- The project uses both setup.py and pyproject.toml for compatibility

## Testing Strategy

### Coverage Requirements
- Maintain 90%+ test coverage  
- All new functionality must include comprehensive tests
- Test both success and failure scenarios

### Test Organization
- Use both unittest.TestCase and pytest patterns
- Place tests in appropriate subdirectory (`tests/`, `tests/pytests/`, `tests/unittests/`)
- Test files follow `test_` prefix convention

### Manual Validation Required
After any changes, always manually test:
1. Basic data generation for primitive types
2. Dataclass creation with both anonymous and fake data
3. Decorator functionality with real test methods
4. DataFrame creation and content validation
5. Error handling for unsupported types

## CI/CD Integration

The repository has extensive GitHub Actions workflows for:
- Python 3.8-3.13 on Linux, macOS, Windows
- Test execution with coverage reporting
- SonarCloud quality analysis
- PyPI publishing

Your local changes should pass the same validations as CI:
1. All tests pass
2. Coverage maintained
3. No import errors
4. Examples in documentation work correctly

## Performance Considerations

- Data generation is designed to be fast for test scenarios
- Faker integration adds some overhead but provides realistic data
- DataFrame creation scales with requested row count (default: 3 rows)
- Memory usage is minimal for typical test scenarios

## Frequently Referenced Commands

```bash
# Quick validation sequence
pip install -r requirements.txt
pip install -e . --user  
python -m pytest tests/ -v --cov --cov-report=term-missing

# Test specific functionality
python -c "from autofaker import Autodata; print(Autodata.create(str))"

# Run subset of tests
python -m pytest tests/test_create_anonymous_builtins.py -v

# Build check
python setup.py sdist bdist_wheel
```