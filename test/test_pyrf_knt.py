from pyrf_knt.wrapper import rf_calc

# Test parameters
ps = 1
thik = [10.0, 20.0, 30.0]
beta = [3.5, 4.0, 4.5]
kapa = [1.0, 1.5, 2.0]
p = 0.06
duration = 10.0
dt = 0.01
gauss = 5.0
shft = 0.0
db = 0.0
dh = 0.0

# Call the wrapper
result = rf_calc(ps, thik, beta, kapa, p, duration, dt, gauss, shft, db, dh)

# Print the result
print("Result:", result)

