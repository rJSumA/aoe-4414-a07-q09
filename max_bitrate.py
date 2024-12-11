# max_bitrate.py
#
# Usage: python3 max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz
#  Calculation for maximum achievalble bitrate
#
# Parameters:
# tx_w: Transmission power------------ (Watts)
# tx_gain_db: Transmission gain------- (db)
# freq_hz: Transmission frequency----- (Hz)
# dist_km: Distance------------------- (km)
# rx_gain_db: Reciever gain----------- (db)
# n0_j: Constant
# bw_hz: Bandwith--------------------- (Hz)
#  ...
# Output:
#  Print the maximum achievable bitrate
#
# Written by Ryo Jumadiao
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import sys # argv
import math

# "constants"
c = 2.99792458*(10**8)

# initialize script arguments
tx_w = float('nan')
tx_gain_db = float('nan')
freq_hz = float('nan')
dist_km = float('nan')
rx_gain_db = float('nan')
n0_j = float('nan')
bw_hz = float('nan')

# parse script arguments
if len(sys.argv)==8:
    tx_w = float(sys.argv[1])
    tx_gain_db = float(sys.argv[2])
    freq_hz = float(sys.argv[3])
    dist_km = float(sys.argv[4])
    rx_gain_db = float(sys.argv[5])
    n0_j = float(sys.argv[6])
    bw_hz = float(sys.argv[7])
else:
    print(\
        'Usage: '\
        'python3 max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz'\
    )
    exit()

# write script below this line

lam = c/freq_hz
C = tx_gain_db * tx_w * ( (lam / (4*math.pi * (dist_km*1000) ) )**2 ) * rx_gain_db
N = bw_hz * n0_j
r_max = bw_hz * math.log2(1 + C/N)

print(math.floor(r_max))