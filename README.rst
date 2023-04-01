
METIS for Python (with support for PyTorch CSR tensors)
================

The following is a version of the "METIS wrapper using ctypes" that was
originally written by Ken Watford (kwatford@gmail.com). The original contents of the 
README file from his repository (https://github.com/kw/metis-python) are included at the end
of this document. All modifications are made under this software's original MIT
license, and no guarantee is provided as to their correctness.


This package is modified to support PyTorch tensors as input to make it more convienient to partition 
graphs in PyTorch. Presently, this repository is primarily intended to be used in conjunction with the software
for SALIENT++ for performing graph partitioning. 


Original README : METIS for Python
================
Wrapper for the METIS library for partitioning graphs (and other stuff).

This library is unrelated to PyMetis, except that they wrap the same library.
PyMetis is a Boost Python extension, while this library is pure python and will
run under PyPy and interpreters with similarly compatible ctypes libraries.

NetworkX_ is recommended for representing graphs for use with this wrapper,
but it isn't required. Simple adjacency lists are supported as well.

.. _NetworkX: http://networkx.lanl.gov/

Please see the full documentation_ for examples or the GitHub repository_ for bug reports

.. _documentation: http://metis.readthedocs.org
.. _repository: https://github.com/kw/metis-python
