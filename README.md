## Introduction
---------------

Make_Image generates an image from the byte information of a given file,
and can reverse the process, creating a file from a supplied image.

* To submit bug reports or feature requests, or to contribute to the code
  directly, visit the GitHub project page:
  (https://github.com/dzamie/Make_Image/)

## Requirements
---------------

This script requires the following:

* Python 3.6.0 (http://www.python.org/)
  * and included modules `argparse` and `math`
  * other versions not tested
* Pillow module 4.0.0 (http://python-pillow.org/)
  * other versions not tested

## Troubleshooting/FAQ
----------------------

Q: Can the images be used to view data, or is it just encryption?

A: The original purpose of this tool was to facilitate finding patterns in hex
   data. Each pixel represents one byte, with the value encoded in the Red and
   Green values of the pixel (e.g. 0x3e0a becomes #33ee00 and #00aa00). It is
   also possible to edit images to change the encoded file through visual
   means rather than text.

Q: Why does the last row of colors in one image have a string of the same
   bluish green?

A: #00ff88 is the color used to pad out the remainder of the last row, when the
   filesize is not divisible by the image width. It has no affect on the
   decoder, which will treat the color as an End of File.

Q: After using the image-to-file option, the resulting file is corrupted. How is
   this fixed?

A: Please ensure you have checked the following, then raise an Issue on the
   GitHub project page. Include Python and Pillow version, as well as the
   filetype you are trying to convert to and from.

* You have not mistyped the input image file or the output filetype.
* You have not made any undesired changes to the image before conversion.
* Any changes made to the image would not corrupt the resulting file.

Q: The tool throws a KeyError, what happened?

A: You likely tried to use an image type unsupported by Pillow. The supported
   image types can be found here:
   (https://pillow.readthedocs.io/en/latest/handbook/image-file-formats.html)
