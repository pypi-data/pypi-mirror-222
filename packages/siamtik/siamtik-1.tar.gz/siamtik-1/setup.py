from setuptools import setup, find_packages
setup(
    name='siamtik',
    packages=find_packages(),
    include_package_data=True,
    version="1",
    description='',
    author='SIAM RAHMAN',
    author_email='s14mbro1@gmail.com',
    long_description=(open("README.md","r")).read(),
    long_description_content_type="text/markdown",
   install_requires=['colorama','requests','prettytable','pyfiglet', 'random', 'bs4'],
 
    keywords=[],
    classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3',
            'Operating System :: OS Independent',
            'Environment :: Console',
    ],
    
    license='MIT',
    entry_points={
            'console_scripts': [
                'siamphisher = siam.siam:siam',
                
            ],
    },
    python_requires='>=3.6'
)
