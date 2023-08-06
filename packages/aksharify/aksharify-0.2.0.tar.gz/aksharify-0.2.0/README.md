<a name="readme-top"></a>

# __Aksharify__

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
[![PyPI - Downloads][Downloads-shield]](https://pypistats.org/packages/aksharify)

<br />

## About The Module

Aksharify is an open-source python package hosted on GitHub that allows you to effortlessly transform images into captivating ASCII art representations. With Aksharify, you can convert your favorite images into an artistic arrangement of ASCII characters, adding a unique and nostalgic touch to your projects.

Start transforming your photos into captivating ASCII art with Aksharify and unleash your creativity in the world of visual representation!
## Key Features

- Convert photos and images into ASCII art with a single function call.

- Fine-tune the output by adjusting parameters such as character set, resolution etc.

- Support for various character sets, allowing you to customize the style of the generated ASCII art.

- Export the ASCII art as plain text or save it as an image file for easy sharing and integration.

## What is AsciiArt

ASCII art is a style of art in which people make graphics and designs by using letters, numbers, and symbols from a unique set of characters known as ASCII. ASCII painters create intriguing images by arranging these characters in patterns and forms rather than using colours and brushes as in traditional art. They meticulously select the appropriate characters and combine them to produce images of animals, people, or even landscapes. It's almost as if you're sketching with letters and symbols! ASCII art is a fun way for artists to express themselves using only the basic characters present on a computer keyboard.

<!-- ABOUT THE PROJECT -->
## Motivation

The inspiration for this module came from a Numberphile video called "The Trinity Hall Prime," which I first saw in high school days. It motivated me to explore the possibilities of such a prime number. I created a Python module that uses a predetermined character set to turn photos into ASCII art. It manipulates images using the PIL package, transforming them to grayscale before mapping pixel values to ASCII letters. Users can change the character set to get different effects.

<!-- GETTING STARTED -->
## Getting Started

Before we begin, make sure you have one of recent versions of Python installed on your computer.

### Installation

```sh
python -m pip install aksharify
```

## Usage

```python
from aksharify import AksharArt
from aksharify.image import Image
from aksharify.distributions import Linear
from aksharify.outputs import SVG
```

```python
image = Image("images\julia1.png")
image.set_dim(200)
image.show()
```

```python
lin = Linear("01")
lin.show()
```

```python
art = AksharArt(image, lin)
art.aksharify(show=True)
```

```python
config = SVG()
config.file_name = "art"
config.bold = True
```

```python
art.export(config)
```

_For examples from user community, please refer to the [primepatel.github.io/aksharify](https://primepatel.github.io/aksharify)_


<!-- ROADMAP -->
## Roadmap

- [x] NumberiFy
- [ ] Predifined order of characters
- [ ] Getting images from URL
- [ ] EmojiFy

See the [open issues](https://github.com/github_username/repo_name/issues) for a full list of proposed features (and known issues).

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such a wonderful place to learn, be inspired, and create. Any contributions you make are `appreciated greatly`.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<!-- CONTACT -->
## Contact

Prime Patel - [@primepatel](https://twitter.com/primespatel) - primespatel@gmail.com

Project Link: [https://github.com/primepatel/aksharify](https://github.com/primepatel/aksharify)


<!-- ACKNOWLEDGMENTS -->
<!-- ## Acknowledgments

* []()
* []()
* []() -->

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/primepatel/Aksharify.svg?style=for-the-badge
[contributors-url]: https://github.com/primepatel/Aksharify/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/primepatel/Aksharify.svg?style=for-the-badge
[forks-url]: https://github.com/primepatel/Aksharify/network/members
[stars-shield]: https://img.shields.io/github/stars/primepatel/Aksharify.svg?style=for-the-badge
[stars-url]: https://github.com/primepatel/Aksharify/stargazers
[issues-shield]: https://img.shields.io/github/issues/primepatel/Aksharify.svg?style=for-the-badge
[issues-url]: https://github.com/primepatel/Aksharify/issues
[license-shield]: https://img.shields.io/github/license/primepatel/Aksharify.svg?style=for-the-badge
[license-url]: https://github.com/primepatel/Aksharify/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/primepatel
[Downloads-shield]: https://img.shields.io/pypi/dm/aksharify?style=for-the-badge