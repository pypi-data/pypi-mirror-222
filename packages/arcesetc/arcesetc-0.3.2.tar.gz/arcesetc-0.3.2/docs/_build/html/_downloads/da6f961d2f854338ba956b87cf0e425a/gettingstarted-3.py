import matplotlib.pyplot as plt
import astropy.units as u

from arcesetc import plot_order_sn

sptype = 'B3V'
wavelength = 3990 * u.Angstrom
signal_to_noise = 100
V = 5

fig, ax, exp_time = plot_order_sn(sptype, wavelength, V, signal_to_noise=signal_to_noise)
plt.show()