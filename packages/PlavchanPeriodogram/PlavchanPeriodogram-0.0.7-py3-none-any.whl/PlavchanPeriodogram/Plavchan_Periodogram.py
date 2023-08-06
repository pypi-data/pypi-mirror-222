import lightkurve as lk
import numpy as np

class Plavchan_Periodogram:
    def __init__(self, time, flux, num_outliers=10, phase_box_size=0.05):
        self.time = time
        self.flux = flux
        self.num_outliers = num_outliers
        self.phase_box_size = phase_box_size

    def compute_periodogram(self, trial_periods):
        periodogram = []
        for period in trial_periods:
            phase = (self.time % period) / period
            smoothed_flux = self._box_car_smoothing(phase)
            squared_residuals = (self.flux - smoothed_flux)**2
            worst_fit_indices = np.argsort(squared_residuals)[-self.num_outliers:]
            normalization = np.sum(squared_residuals[worst_fit_indices])
            power = normalization / np.sum(squared_residuals)
            periodogram.append(power)

        return np.array(periodogram)

    def _box_car_smoothing(self, phase):
        smoothed_flux = []
        for i in range(len(phase)):
            box_start = phase[i] - self.phase_box_size / 2
            box_end = phase[i] + self.phase_box_size / 2
            in_box = (phase >= box_start) & (phase <= box_end)
            smoothed_flux.append(np.mean(self.flux[in_box]))

        return np.array(smoothed_flux)