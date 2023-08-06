import matplotlib.pyplot as plt
import astropy.units as u

from arcesetc import plot_order_sn

sptype = 'WN8h'
wavelength = 6562 * u.Angstrom
signal_to_noise = 30
V = 14

fig, ax, exp_time = plot_order_sn(sptype, wavelength, V, signal_to_noise=signal_to_noise)
plt.show()