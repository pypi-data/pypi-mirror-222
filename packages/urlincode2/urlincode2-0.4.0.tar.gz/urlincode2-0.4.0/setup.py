from setuptools import setup, find_packages
def hello():
    print('hello')
    return 'hello'
setup(
    name='urlincode2',
    version='0.4.0',
    packages=find_packages(),
    url='https://www.wikipedia.com',
    project_urls= {
    	'Homepage': 'https://www.wikipedia.com'
    },
    test=hello()
)

