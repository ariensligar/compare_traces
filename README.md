<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/ariensligar/compare_traces">
    <img src="images/logo.png" alt="Logo" width="585" height="169">
  </a>

<h3 align="center">Ansys Compare Traces Wizard</h3>

  <p align="center">
    project_description
    <br />
    <a href="https://github.com/ariensligar/compare_traces"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/ariensligar/compare_traces">View Demo</a>
    ·
    <a href="https://github.com/ariensligar/compare_traces/issues">Report Bug</a>
    ·
    <a href="https://github.com/ariensligar/compare_traces/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#known-issues">Known Issues</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

The Compare Traces Wizard is a tool that can be used to extract data from an Ansys Electronics Desktop (currently only HFSS design types), perform math operations across multiple traces and plot results. The wizard can operate on any trace or report, within any open project/design.

[![Product Name Screen Shot][product-screenshot]](https://github.com/ariensligar/compare_traces)


## Using the Wizard

Calculations can be performed on several traces simultaneously or individual traces. Populate the GUI by browsing for existing traces within reports. Once populated, the data for this trace will be assigned to the corresponding label (A, B, C...etc). These labels can then be used in the calculation window to simplify the input of expressions. For example, an expression could simply be entered as A+B in the calculation window, and the results would reflect whatever data was defined for the A and B traces.

Entering calculations can use standard python syntax, or utilize the Numpy library (imported as np) for more complex calculations. For example, np.fft.fft(A) would take the FFT of the data stored in A.

Multiple calculations can be done simply by creating a new line (hitting enter). Each line will be evaluated independently.


<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [python](https://python.org/)
* [pyAEDT](https://github.com/pyansys/pyaedt)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Download stand-alone executable from releases (right hand side of screen), or clone repository to run scripts directly.

### Prerequisites

To run the Compare Traces Wizard, you must have a local licenced copy of AEDT 2022 R1/R2 or 2023 R1.


### Installation

The Compare Traces wizard can be run by executing the standalone compare_traces.exe or running the main.py script with the appropriate python environment

1. Clone the repo
   ```sh
   git clone https://github.com/ariensligar/compare_traces.git
   ```

If you want to run the compare traces wizard as a script (not using the executable), a python environment will need to be configured. See README_python_env.txt for an example of how to setup a python environment. If you want to re-build the application as an exe, see README_creating_application.txt.


Standalone Executable with GUI:
   ```sh
	compare_traces.exe
   ```
Script with GUI:
   ```sh
	main.py
   ```


### Known Issues

There is current issue with the stand-alone .exe, very slow to launch on some systems. This is a result of a virus scanner, or windows defender scanning the file and all the extracted temporary files everytime it is launched. A solution is to either add this to exclusions, or move all the contents of the installation to a folder the exclusions list. To see folders that are excluded, Start > Settings > Update & Security > Windows Security > Virus & threat protection Settings > Manage Settings. From within manage settings, under Exclusions, select Add or remove exclusions. If an exclusion cannot be added, try moving the 5G wizard and all folder to a folder that is already included in the exclusions list, often C:\Program Files\AnsysEM\ is already excluded and can be used.


<p align="right">(<a href="#top">back to top</a>)</p>


See the [open issues](https://github.com/ariensligar/compare_traces/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Arien Sligar - arien.sligar@ansys.com

Project Link: [https://github.com/ariensligar/compare_traces](https://github.com/ariensligar/compare_traces)

<p align="right">(<a href="#top">back to top</a>)</p>








<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/ariensligar/compare_traces.svg?style=for-the-badge
[contributors-url]: https://github.com/ariensligar/compare_traces/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ariensligar/compare_traces.svg?style=for-the-badge
[forks-url]: https://github.com/ariensligar/compare_traces/network/members
[stars-shield]: https://img.shields.io/github/stars/ariensligar/compare_traces.svg?style=for-the-badge
[stars-url]: https://github.com/ariensligar/compare_traces/stargazers
[issues-shield]: https://img.shields.io/github/issues/ariensligar/compare_traces.svg?style=for-the-badge
[issues-url]: https://github.com/ariensligar/compare_traces/issues
[license-shield]: https://img.shields.io/github/license/ariensligar/compare_traces.svg?style=for-the-badge
[license-url]: https://github.com/ariensligar/compare_traces/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
