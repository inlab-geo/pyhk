# pyhk

This repository contains ctypes based Python wrappers for calculataion 
of receiver functions. The code was originally written by Brian Kennet and 
then adapted by Lupei Zhu and Sheng Wang and released by Lupei Zhu as the hk 
package.

## Installation
```
pip install git+https://github.com/inlab-geo/pyhk
```

## Documentation


```python
import pyhk
import numpy as np

my_model_thicknesses = [10, 20, 0]
my_model_vs = [3.3, 3.4, 4.5]
my_model_vp_vs_ratio = [1.732, 1.732, 1.732]
my_ray_param_s_km = 0.07
my_time_shift = 5
my_time_duration = 50
my_time_sampling_interval = 0.1
my_gauss = 1.0

data_rf = pyhk.rfcalc(
    ps=0, 
    thik=my_model_thicknesses, 
    beta=my_model_vs, 
    kapa=my_model_vp_vs_ratio, 
    p=my_ray_param_s_km, 
    duration=my_time_duration, 
    dt=my_time_sampling_interval, 
    shft=my_time_shift, 
    gauss=my_gauss
)
data_times = np.arange(data_rf.size) * my_time_sampling_interval - my_time_shift

# if you'd like to visualise it
import matplotlib.pyplot as plt

plt.scatter(data_times, data_rf)
plt.show()
```


## Licensing
The python wrapper for the original `hk` package is released as BSD-2-Clause licence


## Citations and Acknowledgments

The hk package upon which this is based is available on  Lupei Zhu's website

https://www.eas.slu.edu/People/LZhu/home.html
