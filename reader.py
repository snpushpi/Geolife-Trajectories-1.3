
import read_geolife
import pandas as pd
import numpy as np
import pptk
df = read_geolife.read_all_users('Data')
df.to_pickle('geolife.pkl')
df = pd.read_pickle('geolife.pkl')
p = np.c_[df['lon'], df['lat'], np.zeros(len(df))]
v = pptk.viewer(p)
v.attributes(df['alt'])
