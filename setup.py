import shutil
from setuptools import Command, setup

class CleanCommand(Command):

    """setuptools Clean"""
    description = "Clean directory"
    user_options = list(tuple())


    def initialize_options(self):
        
        """init options"""
        pass

    def finalize_options(self):

        """finalize options"""
        pass

    def remove_directory(self, top):
        shutil.rmtree(top)

    def run(self):
        tops = ['./build', './dist', './ZintPy.egg-info']
        for top in tops:
            self.remove_directory(top)




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
        cmdclass={
            'clean': CleanCommand,
            },
        entry_points={
            'console_scripts': [
                'zint = zintpy.scripts.main'
                ]
            },
        zip_safe=False)
