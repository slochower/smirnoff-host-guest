#!/usr/bin/env bash
source $AMBERHOME/amber.sh
cp eqnpt.100.rst md.000.rst

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.000.rst -i mdin -o mdout.001 -r md.001.rst -x traj.001.nc -inf mdinfo.001 -e mden.001 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.001.rst -i mdin -o mdout.002 -r md.002.rst -x traj.002.nc -inf mdinfo.002 -e mden.002 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.002.rst -i mdin -o mdout.003 -r md.003.rst -x traj.003.nc -inf mdinfo.003 -e mden.003 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.003.rst -i mdin -o mdout.004 -r md.004.rst -x traj.004.nc -inf mdinfo.004 -e mden.004 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.004.rst -i mdin -o mdout.005 -r md.005.rst -x traj.005.nc -inf mdinfo.005 -e mden.005 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.005.rst -i mdin -o mdout.006 -r md.006.rst -x traj.006.nc -inf mdinfo.006 -e mden.006 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.006.rst -i mdin -o mdout.007 -r md.007.rst -x traj.007.nc -inf mdinfo.007 -e mden.007 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.007.rst -i mdin -o mdout.008 -r md.008.rst -x traj.008.nc -inf mdinfo.008 -e mden.008 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.008.rst -i mdin -o mdout.009 -r md.009.rst -x traj.009.nc -inf mdinfo.009 -e mden.009 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.009.rst -i mdin -o mdout.010 -r md.010.rst -x traj.010.nc -inf mdinfo.010 -e mden.010 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.010.rst -i mdin -o mdout.011 -r md.011.rst -x traj.011.nc -inf mdinfo.011 -e mden.011 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.011.rst -i mdin -o mdout.012 -r md.012.rst -x traj.012.nc -inf mdinfo.012 -e mden.012 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.012.rst -i mdin -o mdout.013 -r md.013.rst -x traj.013.nc -inf mdinfo.013 -e mden.013 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.013.rst -i mdin -o mdout.014 -r md.014.rst -x traj.014.nc -inf mdinfo.014 -e mden.014 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.014.rst -i mdin -o mdout.015 -r md.015.rst -x traj.015.nc -inf mdinfo.015 -e mden.015 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.015.rst -i mdin -o mdout.016 -r md.016.rst -x traj.016.nc -inf mdinfo.016 -e mden.016 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.016.rst -i mdin -o mdout.017 -r md.017.rst -x traj.017.nc -inf mdinfo.017 -e mden.017 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.017.rst -i mdin -o mdout.018 -r md.018.rst -x traj.018.nc -inf mdinfo.018 -e mden.018 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.018.rst -i mdin -o mdout.019 -r md.019.rst -x traj.019.nc -inf mdinfo.019 -e mden.019 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.019.rst -i mdin -o mdout.020 -r md.020.rst -x traj.020.nc -inf mdinfo.020 -e mden.020 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.020.rst -i mdin -o mdout.021 -r md.021.rst -x traj.021.nc -inf mdinfo.021 -e mden.021 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.021.rst -i mdin -o mdout.022 -r md.022.rst -x traj.022.nc -inf mdinfo.022 -e mden.022 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.022.rst -i mdin -o mdout.023 -r md.023.rst -x traj.023.nc -inf mdinfo.023 -e mden.023 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.023.rst -i mdin -o mdout.024 -r md.024.rst -x traj.024.nc -inf mdinfo.024 -e mden.024 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.024.rst -i mdin -o mdout.025 -r md.025.rst -x traj.025.nc -inf mdinfo.025 -e mden.025 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.025.rst -i mdin -o mdout.026 -r md.026.rst -x traj.026.nc -inf mdinfo.026 -e mden.026 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.026.rst -i mdin -o mdout.027 -r md.027.rst -x traj.027.nc -inf mdinfo.027 -e mden.027 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.027.rst -i mdin -o mdout.028 -r md.028.rst -x traj.028.nc -inf mdinfo.028 -e mden.028 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.028.rst -i mdin -o mdout.029 -r md.029.rst -x traj.029.nc -inf mdinfo.029 -e mden.029 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.029.rst -i mdin -o mdout.030 -r md.030.rst -x traj.030.nc -inf mdinfo.030 -e mden.030 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.030.rst -i mdin -o mdout.031 -r md.031.rst -x traj.031.nc -inf mdinfo.031 -e mden.031 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.031.rst -i mdin -o mdout.032 -r md.032.rst -x traj.032.nc -inf mdinfo.032 -e mden.032 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.032.rst -i mdin -o mdout.033 -r md.033.rst -x traj.033.nc -inf mdinfo.033 -e mden.033 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.033.rst -i mdin -o mdout.034 -r md.034.rst -x traj.034.nc -inf mdinfo.034 -e mden.034 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.034.rst -i mdin -o mdout.035 -r md.035.rst -x traj.035.nc -inf mdinfo.035 -e mden.035 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.035.rst -i mdin -o mdout.036 -r md.036.rst -x traj.036.nc -inf mdinfo.036 -e mden.036 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.036.rst -i mdin -o mdout.037 -r md.037.rst -x traj.037.nc -inf mdinfo.037 -e mden.037 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.037.rst -i mdin -o mdout.038 -r md.038.rst -x traj.038.nc -inf mdinfo.038 -e mden.038 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.038.rst -i mdin -o mdout.039 -r md.039.rst -x traj.039.nc -inf mdinfo.039 -e mden.039 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.039.rst -i mdin -o mdout.040 -r md.040.rst -x traj.040.nc -inf mdinfo.040 -e mden.040 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.040.rst -i mdin -o mdout.041 -r md.041.rst -x traj.041.nc -inf mdinfo.041 -e mden.041 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.041.rst -i mdin -o mdout.042 -r md.042.rst -x traj.042.nc -inf mdinfo.042 -e mden.042 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.042.rst -i mdin -o mdout.043 -r md.043.rst -x traj.043.nc -inf mdinfo.043 -e mden.043 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.043.rst -i mdin -o mdout.044 -r md.044.rst -x traj.044.nc -inf mdinfo.044 -e mden.044 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.044.rst -i mdin -o mdout.045 -r md.045.rst -x traj.045.nc -inf mdinfo.045 -e mden.045 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.045.rst -i mdin -o mdout.046 -r md.046.rst -x traj.046.nc -inf mdinfo.046 -e mden.046 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.046.rst -i mdin -o mdout.047 -r md.047.rst -x traj.047.nc -inf mdinfo.047 -e mden.047 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.047.rst -i mdin -o mdout.048 -r md.048.rst -x traj.048.nc -inf mdinfo.048 -e mden.048 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.048.rst -i mdin -o mdout.049 -r md.049.rst -x traj.049.nc -inf mdinfo.049 -e mden.049 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.049.rst -i mdin -o mdout.050 -r md.050.rst -x traj.050.nc -inf mdinfo.050 -e mden.050 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.050.rst -i mdin -o mdout.051 -r md.051.rst -x traj.051.nc -inf mdinfo.051 -e mden.051 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.051.rst -i mdin -o mdout.052 -r md.052.rst -x traj.052.nc -inf mdinfo.052 -e mden.052 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.052.rst -i mdin -o mdout.053 -r md.053.rst -x traj.053.nc -inf mdinfo.053 -e mden.053 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.053.rst -i mdin -o mdout.054 -r md.054.rst -x traj.054.nc -inf mdinfo.054 -e mden.054 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.054.rst -i mdin -o mdout.055 -r md.055.rst -x traj.055.nc -inf mdinfo.055 -e mden.055 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.055.rst -i mdin -o mdout.056 -r md.056.rst -x traj.056.nc -inf mdinfo.056 -e mden.056 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.056.rst -i mdin -o mdout.057 -r md.057.rst -x traj.057.nc -inf mdinfo.057 -e mden.057 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.057.rst -i mdin -o mdout.058 -r md.058.rst -x traj.058.nc -inf mdinfo.058 -e mden.058 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.058.rst -i mdin -o mdout.059 -r md.059.rst -x traj.059.nc -inf mdinfo.059 -e mden.059 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.059.rst -i mdin -o mdout.060 -r md.060.rst -x traj.060.nc -inf mdinfo.060 -e mden.060 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.060.rst -i mdin -o mdout.061 -r md.061.rst -x traj.061.nc -inf mdinfo.061 -e mden.061 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.061.rst -i mdin -o mdout.062 -r md.062.rst -x traj.062.nc -inf mdinfo.062 -e mden.062 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.062.rst -i mdin -o mdout.063 -r md.063.rst -x traj.063.nc -inf mdinfo.063 -e mden.063 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.063.rst -i mdin -o mdout.064 -r md.064.rst -x traj.064.nc -inf mdinfo.064 -e mden.064 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.064.rst -i mdin -o mdout.065 -r md.065.rst -x traj.065.nc -inf mdinfo.065 -e mden.065 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.065.rst -i mdin -o mdout.066 -r md.066.rst -x traj.066.nc -inf mdinfo.066 -e mden.066 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.066.rst -i mdin -o mdout.067 -r md.067.rst -x traj.067.nc -inf mdinfo.067 -e mden.067 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.067.rst -i mdin -o mdout.068 -r md.068.rst -x traj.068.nc -inf mdinfo.068 -e mden.068 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.068.rst -i mdin -o mdout.069 -r md.069.rst -x traj.069.nc -inf mdinfo.069 -e mden.069 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.069.rst -i mdin -o mdout.070 -r md.070.rst -x traj.070.nc -inf mdinfo.070 -e mden.070 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.070.rst -i mdin -o mdout.071 -r md.071.rst -x traj.071.nc -inf mdinfo.071 -e mden.071 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.071.rst -i mdin -o mdout.072 -r md.072.rst -x traj.072.nc -inf mdinfo.072 -e mden.072 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.072.rst -i mdin -o mdout.073 -r md.073.rst -x traj.073.nc -inf mdinfo.073 -e mden.073 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.073.rst -i mdin -o mdout.074 -r md.074.rst -x traj.074.nc -inf mdinfo.074 -e mden.074 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.074.rst -i mdin -o mdout.075 -r md.075.rst -x traj.075.nc -inf mdinfo.075 -e mden.075 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.075.rst -i mdin -o mdout.076 -r md.076.rst -x traj.076.nc -inf mdinfo.076 -e mden.076 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.076.rst -i mdin -o mdout.077 -r md.077.rst -x traj.077.nc -inf mdinfo.077 -e mden.077 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.077.rst -i mdin -o mdout.078 -r md.078.rst -x traj.078.nc -inf mdinfo.078 -e mden.078 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.078.rst -i mdin -o mdout.079 -r md.079.rst -x traj.079.nc -inf mdinfo.079 -e mden.079 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.079.rst -i mdin -o mdout.080 -r md.080.rst -x traj.080.nc -inf mdinfo.080 -e mden.080 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.080.rst -i mdin -o mdout.081 -r md.081.rst -x traj.081.nc -inf mdinfo.081 -e mden.081 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.081.rst -i mdin -o mdout.082 -r md.082.rst -x traj.082.nc -inf mdinfo.082 -e mden.082 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.082.rst -i mdin -o mdout.083 -r md.083.rst -x traj.083.nc -inf mdinfo.083 -e mden.083 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.083.rst -i mdin -o mdout.084 -r md.084.rst -x traj.084.nc -inf mdinfo.084 -e mden.084 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.084.rst -i mdin -o mdout.085 -r md.085.rst -x traj.085.nc -inf mdinfo.085 -e mden.085 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.085.rst -i mdin -o mdout.086 -r md.086.rst -x traj.086.nc -inf mdinfo.086 -e mden.086 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.086.rst -i mdin -o mdout.087 -r md.087.rst -x traj.087.nc -inf mdinfo.087 -e mden.087 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.087.rst -i mdin -o mdout.088 -r md.088.rst -x traj.088.nc -inf mdinfo.088 -e mden.088 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.088.rst -i mdin -o mdout.089 -r md.089.rst -x traj.089.nc -inf mdinfo.089 -e mden.089 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.089.rst -i mdin -o mdout.090 -r md.090.rst -x traj.090.nc -inf mdinfo.090 -e mden.090 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.090.rst -i mdin -o mdout.091 -r md.091.rst -x traj.091.nc -inf mdinfo.091 -e mden.091 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.091.rst -i mdin -o mdout.092 -r md.092.rst -x traj.092.nc -inf mdinfo.092 -e mden.092 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.092.rst -i mdin -o mdout.093 -r md.093.rst -x traj.093.nc -inf mdinfo.093 -e mden.093 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.093.rst -i mdin -o mdout.094 -r md.094.rst -x traj.094.nc -inf mdinfo.094 -e mden.094 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.094.rst -i mdin -o mdout.095 -r md.095.rst -x traj.095.nc -inf mdinfo.095 -e mden.095 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.095.rst -i mdin -o mdout.096 -r md.096.rst -x traj.096.nc -inf mdinfo.096 -e mden.096 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.096.rst -i mdin -o mdout.097 -r md.097.rst -x traj.097.nc -inf mdinfo.097 -e mden.097 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.097.rst -i mdin -o mdout.098 -r md.098.rst -x traj.098.nc -inf mdinfo.098 -e mden.098 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.098.rst -i mdin -o mdout.099 -r md.099.rst -x traj.099.nc -inf mdinfo.099 -e mden.099 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.099.rst -i mdin -o mdout.100 -r md.100.rst -x traj.100.nc -inf mdinfo.100 -e mden.100 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.100.rst -i mdin -o mdout.101 -r md.101.rst -x traj.101.nc -inf mdinfo.101 -e mden.101 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.101.rst -i mdin -o mdout.102 -r md.102.rst -x traj.102.nc -inf mdinfo.102 -e mden.102 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.102.rst -i mdin -o mdout.103 -r md.103.rst -x traj.103.nc -inf mdinfo.103 -e mden.103 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.103.rst -i mdin -o mdout.104 -r md.104.rst -x traj.104.nc -inf mdinfo.104 -e mden.104 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.104.rst -i mdin -o mdout.105 -r md.105.rst -x traj.105.nc -inf mdinfo.105 -e mden.105 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.105.rst -i mdin -o mdout.106 -r md.106.rst -x traj.106.nc -inf mdinfo.106 -e mden.106 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.106.rst -i mdin -o mdout.107 -r md.107.rst -x traj.107.nc -inf mdinfo.107 -e mden.107 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.107.rst -i mdin -o mdout.108 -r md.108.rst -x traj.108.nc -inf mdinfo.108 -e mden.108 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.108.rst -i mdin -o mdout.109 -r md.109.rst -x traj.109.nc -inf mdinfo.109 -e mden.109 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.109.rst -i mdin -o mdout.110 -r md.110.rst -x traj.110.nc -inf mdinfo.110 -e mden.110 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.110.rst -i mdin -o mdout.111 -r md.111.rst -x traj.111.nc -inf mdinfo.111 -e mden.111 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.111.rst -i mdin -o mdout.112 -r md.112.rst -x traj.112.nc -inf mdinfo.112 -e mden.112 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.112.rst -i mdin -o mdout.113 -r md.113.rst -x traj.113.nc -inf mdinfo.113 -e mden.113 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.113.rst -i mdin -o mdout.114 -r md.114.rst -x traj.114.nc -inf mdinfo.114 -e mden.114 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.114.rst -i mdin -o mdout.115 -r md.115.rst -x traj.115.nc -inf mdinfo.115 -e mden.115 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.115.rst -i mdin -o mdout.116 -r md.116.rst -x traj.116.nc -inf mdinfo.116 -e mden.116 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.116.rst -i mdin -o mdout.117 -r md.117.rst -x traj.117.nc -inf mdinfo.117 -e mden.117 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.117.rst -i mdin -o mdout.118 -r md.118.rst -x traj.118.nc -inf mdinfo.118 -e mden.118 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.118.rst -i mdin -o mdout.119 -r md.119.rst -x traj.119.nc -inf mdinfo.119 -e mden.119 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.119.rst -i mdin -o mdout.120 -r md.120.rst -x traj.120.nc -inf mdinfo.120 -e mden.120 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.120.rst -i mdin -o mdout.121 -r md.121.rst -x traj.121.nc -inf mdinfo.121 -e mden.121 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.121.rst -i mdin -o mdout.122 -r md.122.rst -x traj.122.nc -inf mdinfo.122 -e mden.122 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.122.rst -i mdin -o mdout.123 -r md.123.rst -x traj.123.nc -inf mdinfo.123 -e mden.123 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.123.rst -i mdin -o mdout.124 -r md.124.rst -x traj.124.nc -inf mdinfo.124 -e mden.124 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.124.rst -i mdin -o mdout.125 -r md.125.rst -x traj.125.nc -inf mdinfo.125 -e mden.125 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.125.rst -i mdin -o mdout.126 -r md.126.rst -x traj.126.nc -inf mdinfo.126 -e mden.126 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.126.rst -i mdin -o mdout.127 -r md.127.rst -x traj.127.nc -inf mdinfo.127 -e mden.127 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.127.rst -i mdin -o mdout.128 -r md.128.rst -x traj.128.nc -inf mdinfo.128 -e mden.128 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.128.rst -i mdin -o mdout.129 -r md.129.rst -x traj.129.nc -inf mdinfo.129 -e mden.129 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.129.rst -i mdin -o mdout.130 -r md.130.rst -x traj.130.nc -inf mdinfo.130 -e mden.130 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.130.rst -i mdin -o mdout.131 -r md.131.rst -x traj.131.nc -inf mdinfo.131 -e mden.131 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.131.rst -i mdin -o mdout.132 -r md.132.rst -x traj.132.nc -inf mdinfo.132 -e mden.132 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.132.rst -i mdin -o mdout.133 -r md.133.rst -x traj.133.nc -inf mdinfo.133 -e mden.133 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.133.rst -i mdin -o mdout.134 -r md.134.rst -x traj.134.nc -inf mdinfo.134 -e mden.134 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.134.rst -i mdin -o mdout.135 -r md.135.rst -x traj.135.nc -inf mdinfo.135 -e mden.135 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.135.rst -i mdin -o mdout.136 -r md.136.rst -x traj.136.nc -inf mdinfo.136 -e mden.136 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.136.rst -i mdin -o mdout.137 -r md.137.rst -x traj.137.nc -inf mdinfo.137 -e mden.137 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.137.rst -i mdin -o mdout.138 -r md.138.rst -x traj.138.nc -inf mdinfo.138 -e mden.138 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.138.rst -i mdin -o mdout.139 -r md.139.rst -x traj.139.nc -inf mdinfo.139 -e mden.139 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.139.rst -i mdin -o mdout.140 -r md.140.rst -x traj.140.nc -inf mdinfo.140 -e mden.140 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.140.rst -i mdin -o mdout.141 -r md.141.rst -x traj.141.nc -inf mdinfo.141 -e mden.141 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.141.rst -i mdin -o mdout.142 -r md.142.rst -x traj.142.nc -inf mdinfo.142 -e mden.142 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.142.rst -i mdin -o mdout.143 -r md.143.rst -x traj.143.nc -inf mdinfo.143 -e mden.143 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.143.rst -i mdin -o mdout.144 -r md.144.rst -x traj.144.nc -inf mdinfo.144 -e mden.144 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.144.rst -i mdin -o mdout.145 -r md.145.rst -x traj.145.nc -inf mdinfo.145 -e mden.145 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.145.rst -i mdin -o mdout.146 -r md.146.rst -x traj.146.nc -inf mdinfo.146 -e mden.146 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.146.rst -i mdin -o mdout.147 -r md.147.rst -x traj.147.nc -inf mdinfo.147 -e mden.147 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.147.rst -i mdin -o mdout.148 -r md.148.rst -x traj.148.nc -inf mdinfo.148 -e mden.148 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.148.rst -i mdin -o mdout.149 -r md.149.rst -x traj.149.nc -inf mdinfo.149 -e mden.149 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.149.rst -i mdin -o mdout.150 -r md.150.rst -x traj.150.nc -inf mdinfo.150 -e mden.150 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.150.rst -i mdin -o mdout.151 -r md.151.rst -x traj.151.nc -inf mdinfo.151 -e mden.151 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.151.rst -i mdin -o mdout.152 -r md.152.rst -x traj.152.nc -inf mdinfo.152 -e mden.152 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.152.rst -i mdin -o mdout.153 -r md.153.rst -x traj.153.nc -inf mdinfo.153 -e mden.153 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.153.rst -i mdin -o mdout.154 -r md.154.rst -x traj.154.nc -inf mdinfo.154 -e mden.154 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.154.rst -i mdin -o mdout.155 -r md.155.rst -x traj.155.nc -inf mdinfo.155 -e mden.155 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.155.rst -i mdin -o mdout.156 -r md.156.rst -x traj.156.nc -inf mdinfo.156 -e mden.156 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.156.rst -i mdin -o mdout.157 -r md.157.rst -x traj.157.nc -inf mdinfo.157 -e mden.157 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.157.rst -i mdin -o mdout.158 -r md.158.rst -x traj.158.nc -inf mdinfo.158 -e mden.158 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.158.rst -i mdin -o mdout.159 -r md.159.rst -x traj.159.nc -inf mdinfo.159 -e mden.159 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.159.rst -i mdin -o mdout.160 -r md.160.rst -x traj.160.nc -inf mdinfo.160 -e mden.160 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.160.rst -i mdin -o mdout.161 -r md.161.rst -x traj.161.nc -inf mdinfo.161 -e mden.161 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.161.rst -i mdin -o mdout.162 -r md.162.rst -x traj.162.nc -inf mdinfo.162 -e mden.162 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.162.rst -i mdin -o mdout.163 -r md.163.rst -x traj.163.nc -inf mdinfo.163 -e mden.163 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.163.rst -i mdin -o mdout.164 -r md.164.rst -x traj.164.nc -inf mdinfo.164 -e mden.164 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.164.rst -i mdin -o mdout.165 -r md.165.rst -x traj.165.nc -inf mdinfo.165 -e mden.165 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.165.rst -i mdin -o mdout.166 -r md.166.rst -x traj.166.nc -inf mdinfo.166 -e mden.166 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.166.rst -i mdin -o mdout.167 -r md.167.rst -x traj.167.nc -inf mdinfo.167 -e mden.167 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.167.rst -i mdin -o mdout.168 -r md.168.rst -x traj.168.nc -inf mdinfo.168 -e mden.168 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.168.rst -i mdin -o mdout.169 -r md.169.rst -x traj.169.nc -inf mdinfo.169 -e mden.169 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.169.rst -i mdin -o mdout.170 -r md.170.rst -x traj.170.nc -inf mdinfo.170 -e mden.170 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.170.rst -i mdin -o mdout.171 -r md.171.rst -x traj.171.nc -inf mdinfo.171 -e mden.171 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.171.rst -i mdin -o mdout.172 -r md.172.rst -x traj.172.nc -inf mdinfo.172 -e mden.172 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.172.rst -i mdin -o mdout.173 -r md.173.rst -x traj.173.nc -inf mdinfo.173 -e mden.173 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.173.rst -i mdin -o mdout.174 -r md.174.rst -x traj.174.nc -inf mdinfo.174 -e mden.174 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.174.rst -i mdin -o mdout.175 -r md.175.rst -x traj.175.nc -inf mdinfo.175 -e mden.175 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.175.rst -i mdin -o mdout.176 -r md.176.rst -x traj.176.nc -inf mdinfo.176 -e mden.176 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.176.rst -i mdin -o mdout.177 -r md.177.rst -x traj.177.nc -inf mdinfo.177 -e mden.177 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.177.rst -i mdin -o mdout.178 -r md.178.rst -x traj.178.nc -inf mdinfo.178 -e mden.178 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.178.rst -i mdin -o mdout.179 -r md.179.rst -x traj.179.nc -inf mdinfo.179 -e mden.179 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.179.rst -i mdin -o mdout.180 -r md.180.rst -x traj.180.nc -inf mdinfo.180 -e mden.180 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.180.rst -i mdin -o mdout.181 -r md.181.rst -x traj.181.nc -inf mdinfo.181 -e mden.181 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.181.rst -i mdin -o mdout.182 -r md.182.rst -x traj.182.nc -inf mdinfo.182 -e mden.182 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.182.rst -i mdin -o mdout.183 -r md.183.rst -x traj.183.nc -inf mdinfo.183 -e mden.183 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.183.rst -i mdin -o mdout.184 -r md.184.rst -x traj.184.nc -inf mdinfo.184 -e mden.184 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.184.rst -i mdin -o mdout.185 -r md.185.rst -x traj.185.nc -inf mdinfo.185 -e mden.185 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.185.rst -i mdin -o mdout.186 -r md.186.rst -x traj.186.nc -inf mdinfo.186 -e mden.186 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.186.rst -i mdin -o mdout.187 -r md.187.rst -x traj.187.nc -inf mdinfo.187 -e mden.187 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.187.rst -i mdin -o mdout.188 -r md.188.rst -x traj.188.nc -inf mdinfo.188 -e mden.188 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.188.rst -i mdin -o mdout.189 -r md.189.rst -x traj.189.nc -inf mdinfo.189 -e mden.189 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.189.rst -i mdin -o mdout.190 -r md.190.rst -x traj.190.nc -inf mdinfo.190 -e mden.190 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.190.rst -i mdin -o mdout.191 -r md.191.rst -x traj.191.nc -inf mdinfo.191 -e mden.191 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.191.rst -i mdin -o mdout.192 -r md.192.rst -x traj.192.nc -inf mdinfo.192 -e mden.192 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.192.rst -i mdin -o mdout.193 -r md.193.rst -x traj.193.nc -inf mdinfo.193 -e mden.193 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.193.rst -i mdin -o mdout.194 -r md.194.rst -x traj.194.nc -inf mdinfo.194 -e mden.194 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.194.rst -i mdin -o mdout.195 -r md.195.rst -x traj.195.nc -inf mdinfo.195 -e mden.195 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.195.rst -i mdin -o mdout.196 -r md.196.rst -x traj.196.nc -inf mdinfo.196 -e mden.196 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.196.rst -i mdin -o mdout.197 -r md.197.rst -x traj.197.nc -inf mdinfo.197 -e mden.197 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.197.rst -i mdin -o mdout.198 -r md.198.rst -x traj.198.nc -inf mdinfo.198 -e mden.198 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.198.rst -i mdin -o mdout.199 -r md.199.rst -x traj.199.nc -inf mdinfo.199 -e mden.199 

pmemd.cuda -O -p smirnoff.prmtop -ref smirnoff.inpcrd -c md.199.rst -i mdin -o mdout.200 -r md.200.rst -x traj.200.nc -inf mdinfo.200 -e mden.200 

