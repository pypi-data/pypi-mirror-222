from setuptools import setup, find_packages

setup(
    name='TSolLum',
    version='23.07',
    author='JoHpt',
    description='TSolLum is a Python package designed to analyze the optical properties of a smart window coating material called vanadium dioxide.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/JoHpt/TSolLum',
    packages=find_packages(),
    package_data={
        '': ['d65', 'v-lambda', 'astm_g_173'],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    install_requires=["numpy", "scipy", "pandas", "matplotlib"],
)
