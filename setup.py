import setuptools

setuptools.setup(
    name='pyautodata',
    version='0.1.0',
    url='https://github.com/christianhelle/pyautodata',
    license='MIT License',
    author='Christian Helle',
    author_email='christian.helle@outlook.com',
    description='Python library designed to minimize the setup/arrange phase of your unit tests',
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src')
)
