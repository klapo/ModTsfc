# netcdf/numpy/xray/stats
import numpy as np
from datetime import datetime, timedelta
import pandas as pd
import xarray as xr
from scipy.stats.stats import pearsonr

# OS interaction
import sys, pickle, os

# import plotting
import seaborn as sns
import matplotlib
from matplotlib.pyplot import subplots
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.basemap import Basemap

import summapy

# Customize
sns.set_style("whitegrid")
sns.set_context('paper')
%matplotlib inline

# --------------------------------------------------------------------------------------------------------------------
# Directory Lists
# Unix
if 'linux' in sys.platform:
    dir_pre = '/home/lapok/gdrive/'
# Mac
elif 'darwin' in sys.platform:
    dir_pre = '/Users/karllapo/gdrive/'

# Project specific directories
dirProj = dir_pre + 'SnowHydrology/proj/ModTsfc/'
dirPrint = dirProj + 'Graphics'
dirData = dirProj + 'data'

# Summa specific directories/names
dirSumma = dirProj + 'summa/'
projName = 'summaTestCases'

# Set up other paths
# Format for calling the docker version of summa (from Bart's shell script)
# run_exe      = "docker run -v " + ${BASEDIR} + ":/" + ${summaTestCases} + " bartnijssen/summa:docker"
run_exe      = "docker run -v " + dirSumma + ":/" + projName + " bartnijssen/summa:docker"

dirSettings = dirSumma + "settings/"
dirInput = dirSumma + "input/"
dirOutput = dirSumma + "output/"

# Arguments that will eventually be passed to this function
nRuns = 1
siteName = 'CDP'
os.chdir(dirData)
dat = xr.open_dataset('CDP.ModTsfc.ModelForcing_wy2006.nc')

myDecisions = {'astability': 'louisinv'}
summapy.summaFileManager.decision(myDecisions,
                            '/Users/karllapo/gdrive/SnowHydrology/proj/ModTsfc/summa/ModTsfc_summa/settings',
                            siteName, 'test', '2005-10-01', '2006-09-30')
