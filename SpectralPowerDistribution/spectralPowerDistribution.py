from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import math
import numpy as np

class VLCModel:
    def __init__(self, lx, ly, lz, h, leds_positions, P_totals, FOV_deg=55, theta_deg=60):
        self.lx = lx
        self.ly = ly
        self.lz = lz
        self.h = h
        self.leds_positions = leds_positions
        self.P_totals = P_totals

        self.theta_deg = theta_deg
        self.m = -math.log10(2) / math.log10(math.cos(math.radians(theta_deg)))

        self.FOV_deg = FOV_deg
        self.FOV_rad = FOV_deg * math.pi / 180
        self.index = 1.5
        self.G_Con = (self.index ** 2) / (math.sin(self.FOV_rad) ** 2)

        self.Adet = 10 ** -3
        self.Ts = 1
        self.Nx = lx * 10
        self.Ny = ly * 10

        self.XR, self.YR = np.meshgrid(
            np.arange(0, self.lx + 0.1, self.lx / self.Nx),
            np.arange(0, self.ly + 0.1, self.ly / self.Ny),
        )

    def calculate_distances(self, XT, YT):
        return np.sqrt((self.XR - XT) ** 2 + (self.YR - YT) ** 2 + self.h ** 2)

    def calculate_cos_theta(self, D):
        return self.h / D

    def calculate_H_A(self, cos_theta_A, cos_phi_A, D):
        return ((self.m + 1) * self.Adet * cos_theta_A ** self.m * cos_phi_A) / (
            2 * math.pi * D ** 2
        )

    def simulate(self):
        P_rec = np.zeros((self.Nx + 1, self.Ny + 1))

        for (XT, YT), P_total in zip(self.leds_positions, self.P_totals):
            D = self.calculate_distances(XT, YT)
            cos_theta_A = self.calculate_cos_theta(D)
            cos_phi_A = cos_theta_A.copy()
            cos_phi_A[cos_phi_A < math.cos(math.radians(self.FOV_deg))] = 0

            H_A = self.calculate_H_A(cos_theta_A, cos_phi_A, D)
            P_rec += P_total * H_A

        P_rec *= self.Ts * self.G_Con
        P_rec_dBm = 10 * np.log10(P_rec)

        return P_rec_dBm

    def plot(self, z):
        fig = plt.figure()
        ax1 = Axes3D(fig)
        ax1.plot_surface(self.XR, self.YR, z, rstride=1, cstride=1, cmap="viridis", edgecolor="none")
        plt.title('Distribution of Optical Power')
        plt.xlabel('Length (m)')
        plt.ylabel('Width (m)')
        plt.show()


# Uso de la clase VLCModel
leds_positions = [(1, 0.45), (2, 0.45), (2, 1.15), (1, 1.15), (2, 1.85), (1, 1.85), (2, 2.25), (1, 2.55)]
P_totals = [500 for _ in range(8)]

vlc_model = VLCModel(3, 3, 3, 2.5, leds_positions, P_totals)
P_rec_dBm = vlc_model.simulate()
vlc_model.plot(P_rec_dBm)
