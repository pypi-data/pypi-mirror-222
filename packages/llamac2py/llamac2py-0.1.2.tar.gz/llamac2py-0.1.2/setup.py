from setuptools import setup, Extension
import os

# Get the absolute path to the directory containing setup.py
package_directory = os.path.abspath(os.path.dirname(__file__))

# Define the C extension module
c_extension = Extension(
    'llamac2py._c_module',  # The name of the C extension module
    sources=[os.path.join(package_directory, 'llamac2py', 'run.c')],
)


# Setup the Python package
setup(
    name='llamac2py',
    author='Adarsh Shirawalmath',
    version='0.1.2',  # Update the version number accordingly
    description="llamac2py is a Python package that provides a wrapper for running inference using the Llama-2 Transformer model. The package includes a C executable (run.c) from Karpathy's llama2.c that performs the inference, and the wrapper module (wrapper.py) allows easy integration of the C code into Python scripts.",
    long_description="llamac2py is a Python package that provides a wrapper for running inference using the Llama-2 Transformer model. The package includes a C executable (run.c) from Karpathy's llama2.c that performs the inference, and the wrapper module (wrapper.py) allows easy integration of the C code into Python scripts.",
    packages=['llamac2py'],
    ext_modules=[c_extension],  # Include the C extension module
    zip_safe=False,  # Set to False to ensure C extension is not placed in a zip archive
)
