# Az Image Converter Library

![Python](https://img.shields.io/badge/Python-3.x-blue.svg) 
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)


Az Image Converter is a Python library that provides a simple and convenient way to convert images between different formats using the Pillow library.

## Installation

```bash
pip install az_image_converter
```
## Features

- Convert JPG to PNG format.
- Convert PNG to JPG format.

## Usage

```python
from az_image_converter import JPGtoPNGConverter, PNGtoJPGConverter

# JPG to PNG conversion
input_jpg_file = "input_image.jpg"
output_png_file = "output_image.png"
converter = JPGtoPNGConverter(input_jpg_file, output_png_file)
converter.convert()

# PNG to JPG conversion
input_png_file = "input_image.png"
output_jpg_file = "output_image.jpg"
converter = PNGtoJPGConverter(input_png_file, output_jpg_file)
converter.convert()

```

## Dependencies

This library uses the Pillow library for image processing.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to create an issue or submit a pull request.

## Version
0.1.0 (see Changelog for release notes)



## Documentation

[Read Documentation](https://linktodocumentation)


## FAQ

#### What image formats does the Az Image Converter Library support for conversion?

The Az Image Converter Library currently supports the conversion of JPG to PNG format and PNG to JPG format. It leverages the Pillow library to handle the image processing tasks efficiently.

#### How do I install the Az Image Converter Library in my Python environment?

You can easily install the Az Image Converter Library using pip. Just run the following command in your terminal or command prompt:
```bash
pip install az_image_converter
```
#### Are there any external dependencies required to use the Image Converter Library?
Yes, the Image Converter Library relies on the ```Pillow``` library for image processing. It is a widely-used Python Imaging Library (PIL) that provides extensive support for various image formats.
#### Can I contribute to the Image Converter Library and suggest new features?
Absolutely! Contributions to the library are welcome. If you find any issues, have ideas for improvements, or want to add new features, feel free to create an issue on the project's GitHub repository or submit a pull request.
## Feedback

If you have any feedback, please reach out to us at https://github.com/azeemprogrammer


## Author

[Azeem Akhtar](https://github.com/azeemprogrammer)

[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://github.com/azeemprogrammer)

## 🛠 Skills
Python, Machine Learning, Deep Learning, Data Science, Django, and Artificial Intelligence

