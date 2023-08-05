import os
from pathlib import Path
import tomli
import importlib.metadata
import pandas as pd


try:
    __version__ = importlib.metadata.version('sunpeek')
except importlib.metadata.PackageNotFoundError:
    try:
        with open(Path(__file__).parent.with_name('pyproject.toml'), 'rb') as f:
            t = tomli.load(f)
        __version__ = t['tool']['poetry']['version']
    except FileNotFoundError:    # Package is in a context where pyproject not available (e.g. pip installed)
        __version__ = os.environ['SUNPEEK_VERSION']

# Some calculations return Inf values (eg. CoolProp fluids when temperature exceeds allowed range). With this
# setting, all calculations can assume everything not a valid number is encoded as NaN and use pd.isna()
pd.set_option('mode.use_inf_as_na', True)


try:
    import plotly.io as pio
    pd.set_option("plotting.backend", "plotly")
    pio.renderers.default = 'browser'
except ModuleNotFoundError:
    print("WARNING: module 'plotly' not found. This is only important for development")
