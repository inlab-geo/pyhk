import numpy as np
import pyhk


def test_rfcalc():
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
    
def test_respknt():
    my_model_thicknesses = [10, 20, 0]
    my_model_vs = [3.3, 3.4, 4.5]
    my_model_vp_vs_ratio = [1.732, 1.732, 1.732]
    my_ray_param_s_km = 0.07
    my_time_duration = 50
    my_time_sampling_interval = 0.1

    data_rf = pyhk.rfcalc(
        ps=0, 
        thik=my_model_thicknesses, 
        beta=my_model_vs, 
        kapa=my_model_vp_vs_ratio, 
        p=my_ray_param_s_km, 
        duration=my_time_duration, 
        dt=my_time_sampling_interval, 
    )
    
    data_times = np.arange(data_rf.size) * my_time_sampling_interval 
    

if __name__ == "__main__":
	test_respknt()
	print
