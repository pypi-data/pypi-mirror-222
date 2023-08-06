.. MatAn documentation master file, created by
   sphinx-quickstart on Fri Jun 16 22:21:57 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to MatAn's documentation!
=================================

Shortcut comes from Material Ananalysis - ultimately is should contains modules allowing user to calculate metals and polymers properties from tensile, HDT (polymers) and DSC tests, as well as the others. There are few similar packages in PyPI, but none of them I found good to me, so I wrote new one.

For now it includes:

* ISO:527-1 (polymers analysis)

Getting started
=================================

.. toctree::
   usage
  
Abstract
=================================

Nowadays, Python is one of the most popular programming languages, even in non-informatics fields like mechanical engineering, due to its simplicity, and computer analysis solvers using FEM methods are part of almost all components, albeit access to material data is sometimes hard due to inadequate data in the datasheets, problems with calculations, inconsistent information, etc. To overcome this problem, the Python package was created, which allows to calculate the stress, strains, tensile modulus, and other properties from force and elongation data from a machine. For now, it includes only polymer tests according to the ISO-527-1 standard, but in the future, other standards should be included.

Moreover, the package would need a graphical user interface, which could make it even simpler to use and, more importantly, allow users to upload their obtained results into OpenAccess databases and export plastic strains, tensile modulus, and other properties needed to perform FEM and other numerical analysis. That could make FEM methods even more accessible, which would lead to a decrease in the use of unnecessary materials and, due to this, less CO2 pollution.

Contents
=================================

.. toctree::
   
   api


Indexes and search  
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
  
