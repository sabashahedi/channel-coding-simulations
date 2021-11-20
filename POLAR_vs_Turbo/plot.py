import matplotlib.pyplot as plt
import numpy as np

snr_polar_1024 = np.arange(0, 2.6, 0.1)
BER_polar_1024 = [2.02e-01, 1.85e-01, 1.71e-01, 1.58e-01, 1.46e-01, 1.24e-01, 1.03e-01, 8.21e-02, 7.02e-02, 4.70e-02, 3.11e-02, 1.86e-02,
                  1.17e-02, 5.60e-03, 3.16e-03, 1.61e-03, 8.97e-04, 3.70e-04, 1.34e-04, 5.37e-05, 2.14e-05, 9.91e-06, 3.18e-06, 1.09e-06, 3.91e-07, 1.17e-07]
snr_polar_1723 = np.arange(0, 4.75, 0.25)
BER_polar_1723 = [1.11e-01, 1.05e-01, 9.91e-02, 9.39e-02, 8.89e-02, 8.42e-02, 7.82e-02, 7.27e-02, 6.29e-02,
                  5.21e-02, 3.14e-02, 1.33e-02, 3.14e-03, 4.85e-04, 7.07e-05, 1.02e-05, 2.22e-06, 3.97e-07, 8.34e-08]
snr_turbo = np.arange(0, 3.2, 0.2)
BER_turbo = [1.50e-01, 1.43e-01, 1.40e-01, 1.30e-01, 1.23e-01, 1.13e-01, 1.07e-01, 9.33e-02,
             6.15e-02, 3.42e-02, 9.55e-03, 1.28e-03, 6.65e-05, 2.17e-06, 3.01e-08, 1.19e-10]

plt.figure()
plt.xlabel("Eb/N0 (dB)")
plt.ylabel("BER")
plt.yscale("log")
plt.plot(snr_turbo, BER_turbo, label="Turbo(2256,1504)")
plt.plot(snr_polar_1723, BER_polar_1723, label="Polar(2048, 1723)")
plt.plot(snr_polar_1024, BER_polar_1024, label="Polar(2048, 1024)")
plt.legend()

# plt.figure()
# plt.xlabel("Eb/N0 (dB)")
# plt.ylabel("BER")
# plt.yscale("log")
# plt.plot(snr_BCH_15_11, BER_BCH_15_11, label="Turbo(2256,1504)")
# plt.plot(snr_RS_15_11, BER_RS_15_11, label="Polar(2048, 1723)")
# plt.plot(snr_RS_15_11, BER_RS_15_11, label="Polar(2048, 1024)")
# plt.legend()


plt.show()
