import cv2
import matplotlib.pyplot as plot
import numpy as np

class Spectrum:
    def __init__(self,image):
        self.image=image

    def show_spectrum_fft(self):
        fft = np.fft.fft2(self.image)
        fft_centered = np.fft.fftshift(fft)
        fft_decentered = np.fft.ifftshift(fft_centered)
        invert_fft = np.fft.ifft2(fft_decentered)

        plot.subplot(221), plot.imshow(self.image, 'gray'), plot.title("Original image in grayscale")
        plot.subplot(222), plot.imshow(np.log(1+np.abs(fft)), 'gray'), plot.title("Spectrum")
        plot.subplot(223), plot.imshow(np.log(1+np.abs(fft_centered)), 'gray'), plot.title("Centered spectrum")
        plot.subplot(224), plot.imshow(np.log(1+np.abs(invert_fft)), 'gray'), plot.title("Image after FFT inverse")
        plot.show()
