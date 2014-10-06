from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='ZintPy',
        version='0.0.2',
        description='A Python wrapper for libzint, the open source barcode library',
        long_description=readme(),
        classifiers=[
            'Development Status :: 3 - Alpha',
            'License :: OSI Approved :: BSD License',
            'Programming Language :: Python :: 2.7',
            'Topic :: Multimedia :: Graphics :: Graphics Conversion',
            'Topic :: Multimedia :: Graphics :: Presentation',
            'Topic :: Utilities',
            ],
        keywords='barcode qrcode',
        url='http://github.com/esbullington/zint-py',
        author='Eric S. Bullington',
        author_email='eric.s.bullington@gmail.com',
        license='BSD',
        packages=['zintpy'],
        zip_safe=False)
