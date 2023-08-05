import matplotlib.pyplot as plt
import astropy.units as u

from arcesetc import plot_order_counts, plot_order_sn

sptype = 'G4V'
wavelength = 6562 * u.Angstrom
exp_time = 30 * u.min
V = 10

fig, ax, exp_time = plot_order_sn(sptype, wavelength, V, exp_time=exp_time)
plt.show()