<div align="center">

<br/>

```
██████╗ ███████╗███████╗██████╗     ██╗     ███████╗ █████╗ ██████╗ ███╗   ██╗██╗███╗   ██╗ ██████╗
██╔══██╗██╔════╝██╔════╝██╔══██╗    ██║     ██╔════╝██╔══██╗██╔══██╗████╗  ██║██║████╗  ██║██╔════╝
██║  ██║█████╗  █████╗  ██████╔╝    ██║     █████╗  ███████║██████╔╝██╔██╗ ██║██║██╔██╗ ██║██║  ███╗
██║  ██║██╔══╝  ██╔══╝  ██╔═══╝     ██║     ██╔══╝  ██╔══██║██╔══██╗██║╚██╗██║██║██║╚██╗██║██║   ██║
██████╔╝███████╗███████╗██║         ███████╗███████╗██║  ██║██║  ██║██║ ╚████║██║██║ ╚████║╚██████╔╝
╚═════╝ ╚══════╝╚══════╝╚═╝         ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═══╝ ╚═════╝
```

### 🧠 A Hands-On Journey Into Computer Vision & Image Processing

<br/>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active%20Learning-brightgreen?style=for-the-badge)

<br/>

> *"Every pixel tells a story. This repository is where I learn to read them."*

<br/>

</div>

---

## 📖 What Is This Repository?

This is my personal **learning laboratory** for Deep Learning and Computer Vision concepts. Starting from first principles — how images are stored, read, and manipulated — this repository documents my step-by-step journey into one of the most exciting fields in AI.

Whether you're a beginner curious about how computers "see," or a developer looking for clean, well-commented code snippets, you'll find something useful here.

> **No prior deep learning experience required to follow along!** Each file is self-contained and thoroughly commented.

---

## 🗺️ Repository Structure

```
Deep_Learning_concepts/
│
├── 📄 read_image_using_opencv.py              ← Reading images with OpenCV (grayscale & color)
├── 📄 Reading the Grayscale image using matplotlib.py   ← Grayscale pixel analysis with Matplotlib
├── 📄 Reading_the_color_image_using matplotlib.py       ← RGB channel exploration with Matplotlib
│
└── 📁 Opencv/                                ← Dedicated OpenCV operations module
    ├── 📄 adding_both_images.py              ← Image blending & weighted overlay
    ├── 📄 apply_circle_on_image.py           ← Drawing circles on images
    ├── 📄 apply_rectangle_on_image.py        ← Rectangles, lines & text annotations
    ├── 📄 resize_image.py                    ← Image resizing techniques
    ├── 📄 print_current_datetime_on_image.py ← Live timestamp overlay on frames
    │
    └── 📁 mouse events/
        └── 📄 getting_x_y_coordinates_on_the_image.py  ← Interactive mouse coordinate tracking
```

---

## 🔬 Concepts Covered

### 🖼️ 1. Image Reading & Pixel Analysis

Understanding how computers store and interpret images at the fundamental level — as grids of numbers.

| Concept | Tool Used | What You'll Learn |
|---|---|---|
| Reading grayscale images | Matplotlib | Pixel arrays, shape `(H, W)`, min/max values (0–255) |
| Reading color images | Matplotlib | 3D arrays `(H, W, 3)`, RGB channels independently |
| Reading with OpenCV | OpenCV (cv2) | BGR vs. RGB format differences, `waitKey()`, display windows |

**Key insight covered:** OpenCV reads images in **BGR** format while Matplotlib uses **RGB** — a critical distinction that trips up many beginners. This repo handles that conversion explicitly.

---

### 🎨 2. OpenCV Image Manipulation

A suite of hands-on scripts that teach image drawing, annotation, and transformation.

#### ✏️ Drawing & Annotation
- **Circles** — Draw shapes at precise coordinates with custom color and thickness
- **Rectangles** — Define bounding boxes (commonly used in object detection)
- **Lines** — Draw straight lines across images
- **Text overlays** — Annotate images with custom fonts, sizes, and colors

#### 🔀 Image Arithmetic
- **`cv2.add()`** — Combine two images pixel-by-pixel (saturation arithmetic)
- **`cv2.addWeighted()`** — Blend images with weighted priority (e.g., 70%/30% blend)

This is the foundation of techniques like **image augmentation** and **alpha compositing** used in deep learning pipelines.

#### 📐 Resizing
Two resizing strategies are demonstrated:
- Fixed dimensions: `cv2.resize(img, (width, height))`
- Scale factors: `cv2.resize(img, None, fx=1, fy=0.3)` — resize proportionally

---

### ⏱️ 3. Live Frame Annotation

```python
# Real-time timestamp overlay on a live canvas
text = str(datetime.now())
cv2.putText(black_image, text, (50, i), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)
```

This script demonstrates a core pattern used in **CCTV systems**, **dashcam software**, and **video processing pipelines** — overlaying dynamic text on image frames in real time. The output image is also saved to disk with `cv2.imwrite()`.

---

### 🖱️ 4. Interactive Mouse Event Handling

One of the more advanced concepts here — registering mouse callbacks to capture user interaction with an image window.

```
📌 Click anywhere on the image
   → The (x, y) coordinates are printed directly onto the image at the click location
   → The annotated image is auto-saved as sharuk.jpg
```

**Why this matters:** Mouse event callbacks are the building block for tools like:
- Manual image annotation / labeling tools
- Custom ROI (Region of Interest) selectors
- Interactive segmentation interfaces

---

## 🛠️ Tech Stack

| Library | Purpose |
|---|---|
| **OpenCV (`cv2`)** | Core image I/O, drawing, transformations, mouse events |
| **NumPy** | Pixel array manipulation, creating blank canvases |
| **Matplotlib** | Image visualization and RGB channel inspection |
| **Pandas** | Imported for potential future data handling |
| **datetime / time** | Real-time timestamp generation |

---

## ⚡ Getting Started

### Prerequisites

Make sure you have Python 3.7+ installed. Then install the required libraries:

```bash
pip install opencv-python numpy matplotlib pandas
```

### Running the Scripts

Clone the repository:

```bash
git clone https://github.com/krishna-gunda/Deep_Learning_concepts.git
cd Deep_Learning_concepts
```

Run any script directly:

```bash
# Example: Read and display a grayscale image
python "Reading the Grayscale image using matplotlib.py"

# Example: Draw shapes on an image
python Opencv/apply_rectangle_on_image.py

# Example: Interactive mouse coordinate tracker
python "Opencv/mouse events/getting_x_y_coordinates_on_the_image.py"
```

> **📝 Note:** Some scripts reference image files in a `Pictures/` directory (e.g., `cameraman.tif`, `lena_color_512.tif`). These are classic benchmark images widely used in image processing. You can download them from standard image processing datasets or substitute your own `.tif`/`.jpg` images.

---

## 🎯 Learning Roadmap

This repository represents the **foundation layer** of a broader deep learning journey:

```
✅ Phase 1 — Image Fundamentals (CURRENT)
   └── Reading pixels · RGB vs. BGR · NumPy arrays · OpenCV basics

🔲 Phase 2 — Neural Network Foundations
   └── Artificial Neural Networks (ANN) · Activation functions · Backpropagation

🔲 Phase 3 — Convolutional Neural Networks
   └── Convolution layers · Pooling · Feature maps · CNN architectures

🔲 Phase 4 — Applied Projects
   └── Image classification · Object detection · Model deployment
```

---

## 💡 Who Is This For?

| Audience | Why This Helps |
|---|---|
| **Beginners in AI/ML** | Gentle introduction to how computers process visual data |
| **Python developers** | Clean, readable examples of OpenCV and NumPy in action |
| **CS students** | Practical implementations of image processing theory |
| **Self-learners** | A structured progression from pixel basics to real applications |

---

## 👨‍💻 About the Author

**Krishna Gunda** — A passionate learner building expertise in Deep Learning and Computer Vision from the ground up. This repository is a living document of that journey.

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-krishna--gunda-181717?style=for-the-badge&logo=github)](https://github.com/krishna-gunda)

</div>

---

## 🌱 Contributing & Feedback

This is a learning repository, so suggestions, corrections, and improvements are always welcome!

- 🐛 Found a bug or a better approach? Open an issue.
- 💬 Have a question about any concept? Start a discussion.
- ⭐ If this helped you, a star goes a long way!

---

<div align="center">

**Made with curiosity, coffee, and a lot of pixel math ☕**

*The journey of a thousand models begins with a single pixel.*

</div>
