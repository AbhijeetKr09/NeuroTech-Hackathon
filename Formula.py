from scipy.signal import welch
import numpy as np
import json

import json


class ADHDScorer:
    def __init__(self, fs):
        self.fs = fs

    def calculate_theta_power_per_epoch(self, data):
        n_samples_per_epoch = self.fs
        n_epochs = len(data) // n_samples_per_epoch
        theta_power_per_epoch = np.zeros(n_epochs)

        for i in range(n_epochs):
            epoch_data = data[i*n_samples_per_epoch : (i+1)*n_samples_per_epoch]
            nperseg = min(len(epoch_data), 256)  # Add this line
            freqs, psd = welch(epoch_data, self.fs, nperseg=nperseg)  # Modify this line
            theta_band = np.where((freqs >= 4) & (freqs <= 8))

            # Check if the slice is empty
            if psd[theta_band].size > 0:
                theta_power_per_epoch[i] = np.mean(psd[theta_band])
            else:
                theta_power_per_epoch[i] = np.nan  # Or any other default value

        return theta_power_per_epoch

    def calculate_adhd_score(self, focused_data, unfocused_data):
        focused_theta_power_per_epoch = self.calculate_theta_power_per_epoch(focused_data)
        unfocused_theta_power_per_epoch = self.calculate_theta_power_per_epoch(unfocused_data)

        focused_theta_power = np.mean(focused_theta_power_per_epoch)
        unfocused_theta_power = np.mean(unfocused_theta_power_per_epoch)

        adhd_score = focused_theta_power - unfocused_theta_power

        return adhd_score


if __name__ == "__main__":

# Open the JSON file
    with open('focused_data.json', 'r') as f:
        # Load the data
        Focused_data = json.load(f)

    with open('unfocused_data.json', 'r') as f:
        # Load the data
        unFocused_data = json.load(f)

    scorer = ADHDScorer(250)
    # scorer.calculate_adhd_score(Focused_data, unFocused_data)
    focused_theta_power_per_epoch = scorer.calculate_theta_power_per_epoch(Focused_data)
