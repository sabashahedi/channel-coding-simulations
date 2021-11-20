import matplotlib.pyplot as plt

snr_ldpc_i20 = [1.00,    1.10,    1.20,    1.30,
                1.40,    1.50,    1.60,    1.70,    1.80]
BER_ldpc_i20 = [6.70e-02,    5.33e-02,    3.27e-02,    2.23e-02,
                9.72e-03,    2.96e-03,    5.93e-04,    9.55e-05,    5.25e-06]
FER_ldpc_i20 = [1.00e+00,    9.88e-01,    8.85e-01,    7.90e-01,
                4.98e-01,    1.88e-01,    5.57e-02,    1.06e-02,    1.26e-03]
THR_i20 = [0.02,           3.05,           3.23,           3.49,
           3.66,           4.19,           4.80,           5.29,           5.80]
snr_ldpc_i2000 = [1.00,      1.10,      1.20,
                  1.30,      1.40,      1.50,      1.60,      1.70]
BER_ldpc_i2000 = [6.09e-02,      3.47e-02,      1.69e-02,
                  5.45e-03,      9.40e-04,      1.09e-04,      9.23e-06,      4.26e-07]
FER_ldpc_i2000 = [8.49e-01,      5.29e-01,      2.75e-01,
                  8.86e-02,      1.55e-02,      1.87e-03,      1.57e-04,      7.37e-06]
THR_i2000 = [0.02,             0.07,             0.13,             0.37,
             1.43,             3.42,             4.72,             5.44]
plt.figure()
plt.xlabel("Eb/N0 (dB)")
plt.ylabel("BER")
plt.yscale("log")
plt.plot(snr_ldpc_i20, BER_ldpc_i20, label="LDPC 20 iterations")
plt.plot(snr_ldpc_i2000, BER_ldpc_i2000, label="LDPC 2000 iterations")
plt.legend()

plt.figure()
plt.xlabel("Eb/N0 (dB)")
plt.ylabel("FER")
plt.yscale("log")
plt.plot(snr_ldpc_i20, FER_ldpc_i20, label="LDPC 20 iterations")
plt.plot(snr_ldpc_i2000, FER_ldpc_i2000, label="LDPC 2000 iterations")
plt.legend()

plt.figure()
plt.xlabel("Eb/N0 (dB)")
plt.ylabel("Throughput (Mbps)")
# plt.yscale("log")
plt.plot(snr_ldpc_i20, THR_i20, label="LDPC 20 iterations")
plt.plot(snr_ldpc_i2000, THR_i2000, label="LDPC 2000 iterations")
plt.legend()

plt.show()
