# Seatbelt Detection System

This repository contains a Python-based implementation of a **Seatbelt Detection System** using OpenCV. The system uses edge detection and Hough Line Transform to identify seatbelt patterns within an image and checks for the presence or absence of a seatbelt in the driver's seat area.

---

## Table of Contents
- [Project Overview](#project-overview)
- [How It Works](#how-it-works)
- [Requirements](#requirements)


---

## Project Overview

This project leverages **OpenCV** to detect seatbelts by analyzing line patterns within an image of the driver's seat area. It identifies key characteristics of lines that typically correspond to a fastened seatbelt, such as slope and proximity of detected lines. The system outputs an annotated image indicating whether a seatbelt has been detected.

---

## How It Works

1. **Image Preprocessing**:
   - The input image is converted to grayscale.
   - A blur filter is applied to smooth the image.
   - Edge detection is performed using the **Canny Edge Detector**.

2. **Line Detection**:
   - The **Hough Line Transform** is applied to detect straight lines in the image.
   - Each detected line is analyzed based on its slope and position relative to previously detected lines.

3. **Seatbelt Detection Logic**:
   - Lines that fall within specific slope and distance criteria are assumed to correspond to a seatbelt pattern.
   - If two lines matching these criteria are found close to each other, the system recognizes it as a seatbelt.

---

## Requirements

- **Python 3.6+**
- **OpenCV 4.x**
- **NumPy**
- **Matplotlib** (optional, for extended visualization)

Install the dependencies using:
```bash
pip install opencv-python numpy matplotlib
