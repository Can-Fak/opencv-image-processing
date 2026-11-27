
# STNM - Image Processing

## Overview

This repository contains image processing studies developed as part of STNM activities, focusing on color detection using Python and OpenCV, as well as research on Canny edge detection.

## Technologies

- Python
- OpenCV
- HSV Color Space
- Image Masking
- Bitwise Operations

## Red Color Detection

The application detects red regions in an image using HSV color thresholds and masking techniques.

### Pen Detection

| Original Image | Binary Mask | Detection Result |
| :---: | :---: | :---: |
| ![](kirmizi_kalem.jpg) | ![](kalem_maske.png) | ![](kalem_sonuc.png) |

### Apple Detection

The following images show the results of an earlier color detection experiment.

| Original Image | Binary Mask | Detection Result |
| :---: | :---: | :---: |
| ![](kirmizi_elma.jpeg) | ![](kirmizi_maske.png) | ![](kirmizi_sonuc.png) |

## Canny Edge Detection

A theoretical research study covering the Canny edge detection algorithm, its processing stages, applications, advantages and limitations.

## Installation

Install the required library:

```bash
python -m pip install -r requirements.txt
```

## Usage

Run the application from the project directory:

```bash
python app.py
```

The current application processes the pen image and displays the original image, binary mask and detection result.

## Documentation

Research and application reports are available in the [reports](reports/) directory.
