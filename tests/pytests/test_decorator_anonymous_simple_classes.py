from autofaker import autodata, fakedata


class SimpleClass:
    id = -1
    name = 'name'
    text = 'test'


# Anonymous Simple Class Via Decorator

@autodata(SimpleClass)
def test_create_simple_class_using_decorator_returns_not_none(instance):
    assert instance is not None


@autodata(SimpleClass)
def test_create_simple_class_using_decorator_returns_instance(instance):
    assert isinstance(instance, SimpleClass)


@autodata(SimpleClass)
def test_create_simple_class_returns_instance_with_new_values(instance):
    assert instance.id != SimpleClass().id
    assert instance.name != SimpleClass().name
    assert instance.text != SimpleClass().text


@autodata()
def test_create_simple_class_argument_returns_instance_with_new_values(instance: SimpleClass):
    assert instance.id != SimpleClass().id
    assert instance.name != SimpleClass().name
    assert instance.text != SimpleClass().text


@autodata()
def test_create_anonymous_simple_class_returns_instance_with_new_values(instance: SimpleClass):
    assert instance.id != SimpleClass().id
    assert instance.name != SimpleClass().name
    assert instance.text != SimpleClass().text


@fakedata()
def test_create_fake_simple_class_returns_instance_with_new_values(instance: SimpleClass):
    assert instance.id != SimpleClass().id
    assert instance.name != SimpleClass().name
    assert instance.text != SimpleClass().text
