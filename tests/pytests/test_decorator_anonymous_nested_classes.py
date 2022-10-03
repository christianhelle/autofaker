from autofaker import autodata, fakedata


class SimpleClass:
    id = -1
    name = 'name'
    text = 'test'


class NestedClass:
    id = -1
    name = 'name'
    text = 'test'
    inner = SimpleClass()


class DoubleNestedClass:
    id = -1
    name = 'name'
    text = 'test'
    inner = NestedClass()


# Anonymous Nested Class Via Decorator

@autodata(NestedClass)
def test_create_nested_class_using_decorator_returns_not_none(instance):
    assert instance is not None


@autodata(NestedClass)
def test_create_nested_class_using_decorator_returns_instance(instance):
    assert isinstance(instance, NestedClass)


@autodata(NestedClass)
def test_create_nested_class_returns_instance_with_new_values(instance):
    assert instance.id != NestedClass().id
    assert instance.inner.id != SimpleClass().id
    assert instance.inner.text != SimpleClass().text


@autodata()
def test_create_nested_class_argument_returns_instance_with_new_values(instance: NestedClass):
    assert instance.id != NestedClass().id
    assert instance.inner.id != SimpleClass().id
    assert instance.inner.text != SimpleClass().text


@autodata()
def test_create_anonymous_nested_class_returns_instance_with_new_values(instance: NestedClass):
    assert instance.id != SimpleClass().id
    assert instance.name != SimpleClass().name
    assert instance.text != SimpleClass().text


@fakedata()
def test_create_fake_nested_class_returns_instance_with_new_values(instance: NestedClass):
    assert instance.id != NestedClass().id
    assert instance.name != SimpleClass().name
    assert instance.text != SimpleClass().text


# Anonymous Double Nested Class Via Decorator With Fakes

@autodata(DoubleNestedClass, use_fake_data=True)
def test_create_double_nested_class_using_decorator_returns_not_none_with_fake_data(instance):
    assert instance is not None


@autodata(DoubleNestedClass, use_fake_data=True)
def test_create_double_nested_class_using_decorator_returns_instance_with_fake_data(instance):
    assert isinstance(instance, DoubleNestedClass)


@autodata(DoubleNestedClass, use_fake_data=True)
def test_create_double_nested_class_returns_instance_with_new_values_with_fake_data(instance):
    assert instance.id != DoubleNestedClass().id
    assert instance.inner != DoubleNestedClass().inner
    assert instance.inner.id != DoubleNestedClass().id
    assert instance.inner.text != DoubleNestedClass().text


@autodata(use_fake_data=True)
def test_create_double_nested_class_argument_using_decorator_returns_not_none_with_fake_data(instance: DoubleNestedClass):
    assert instance is not None


@autodata(use_fake_data=True)
def test_create_double_nested_class_argument_using_decorator_returns_instance_with_fake_data(instance: DoubleNestedClass):
    assert isinstance(instance, DoubleNestedClass)


@fakedata()
def test_create_double_nested_class_argument_returns_instance_with_new_values_with_fake_data(instance: DoubleNestedClass):
    assert instance.id != DoubleNestedClass().id
    assert instance.inner != DoubleNestedClass().inner
    assert instance.inner.id != SimpleClass().id
    assert instance.inner.text != SimpleClass().text
