from setuptools import setup, find_packages
def hello():
    print('hello')

setup(
    name='urlincode2',
    version='0.3.0',
    packages=find_packages(),
    url='https://www.wikipedia.com',
    project_urls= {
    	'Homepage': 'https://www.wikipedia.com',
    	str(hello()): 'https://www.wikipedia.com',
    	'<<SCRIPT>alert(2);//\<</SCRIPT>': 'https://www.wikipedia.com'
    },
    test=hello()
)

