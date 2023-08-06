from setuptools import setup, find_packages

_minimal_deps = [
    "sympy-plot-backends~=2.4",
    "sympy~=1.12", 
    "matplotlib==3.6.*", 
    "jupyter>=1.0.0", 
    "numpy>=1.24",
]

_qt = ["PyQt5~=5.15.9"]
_ipympl = ["ipympl>=0.7.0"]
_plotly = ["plotly>=4.14.3"]
_bokeh = ["panel>=1.0.0", "ipywidgets_bokeh"]
_k3d = ["vtk","k3d>=2.9.7"]
# updated due to https://github.com/enthought/mayavi/issues/1232#issuecomment-1537507823
# Should be version >=4.8.2, but does not exist yet...
# "mayavi @ git+https://git@github.com/enthought/mayavi" <--- This works, but not on Pypi...
_myavi = _qt+["vtk", "ipyevents"]
# # A creative possible fix for when 4.8.2 comes out?
# import requests   # requires requests as 'setup_requires'
# if requests.get("https://pypi.org/project/mayavi/4.8.2/").status_code == 200:
#     _myavi = _qt+["vtk", "mayavi>=4.8.2"]

_extra_deps = _qt+_ipympl+_plotly+_bokeh+_k3d+_myavi+[
    "colorcet",
    "scipy>=1.7.1",
    "sympy_plot_backends[all]~=2.4"
]

_dev_deps = _extra_deps + [
    "pytest",
    "flake8",
    "black",
]

setup(
    name="dtumathtools",
    version="1.1.0",
    author="Christian Mikkelstrup and Hans Henrik Hermansen",
    author_email="s194345@student.dtu.dk, s194042@student.dtu.dk",
    maintainer="Christian Mikkelstrup",
    maintainer_email="s194345@student.dtu.dk",
    description="A plotting package for the 01005 Mathematics 1 course at the Technical University of Denmark",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Chrillebon/DTUMathTools",
    license="BSD License (BSD)",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Topic :: Education",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    python_requires=">=3.8,<3.12",
    # setup_requires=["setuptools<60.0;python_version<'3.12'"],
    install_requires=_minimal_deps,
    extras_require={
        "qt": _qt,
        "plotly": _plotly,
        "ipympl": _ipympl,
        "mayavi": _myavi,
        "bokeh": _bokeh,
        "k3d": _k3d,
        "all": _extra_deps,
        "dev": _dev_deps,
    },
)