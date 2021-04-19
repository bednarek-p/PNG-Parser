# E-media

### Arguments
| Option String | Required |  Default| Option Summary |  
|---------------|----------|--------|----------------|  
| ['-p', '--path'] | True | None | Image file path | 
| ['-l', '--chunk_list'] | False | None | Display chunks type list | 
| ['--ihdr'] | False | None | Display information of iHDR chunk | 
| ['--srgb'] | False | None | Display information of sRGB chunk | 
| ['--idat'] | False | None | Display information of iDAT chunk | 
| ['--iend'] | False | None | Display information of iEND chunk | 
| ['--gama'] | False | None | Display information of gAMA chunk | 
| ['--chrm'] | False | None | Display information of cHRM chunk | 
| ['--plte'] | False | None | Display information of pLTE chunk |
| ['--text'] | False | None | Display information of tEXt chunk | 
| ['--fft'] | False | None | Procede Fast Fourier Transformate on png | 
| ['-a', '--anonymization'] | False | None | Procede anonymization | 

### Bibliography
1. http://www.libpng.org/pub/png/spec/1.2/PNG-Contents.html 
2. https://pyokagan.name/blog/2019-10-14-png/ 
3. https://hicraigchen.medium.com/digital-image-processing-using-fourier-transform-in-python-bcb49424fd82
