import cv2
import matplotlib.pyplot as plot
import numpy as np

class Spectrum:
    def __init__(self,image):
        self.image=image

    def show_spectrum_fft(self):
        fft = np.fft.fft2(self.image)
        fft_centered = np.fft.fftshift(fft)
        phase_spectrum = np.angle(fft_centered)

        plot.subplot(131), plot.imshow(self.image, 'gray'), plot.title("Original image in grayscale")
        plot.subplot(132), plot.imshow(np.log(1+np.abs(fft_centered)), 'gray'), plot.title("Centered spectrum")
        plot.subplot(133), plot.imshow(phase_spectrum, 'gray'), plot.title("Phase spectrum")

        plot.show()
