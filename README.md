# Segmentation for Self-Driving Cars Project

Welcome to the **Segmentation for Self-Driving Cars** project! This repository contains code and resources for training a deep learning U-Net model for image segmentation and creating a graphical user interface (GUI) using Tkinter to demonstrate the model's performance. Image segmentation plays a crucial role in enabling self-driving cars to perceive and understand their surroundings.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Model Training](#model-training)
- [GUI Demonstration](#gui-demonstration)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The goal of this project is to develop an image segmentation model capable of identifying and labeling different objects within images relevant to self-driving cars. Image segmentation is vital for tasks such as identifying pedestrians, vehicles, road lanes, and other obstacles.

## Installation

1. Clone this repository to your local machine using:

   ```
   git clone https://github.com/liorperlman/Segmentation-for-Self-Driving-Cars.git
   ```

2. Navigate to the project directory:

   ```
   cd segmentation-self-driving
   ```

3. Set up a virtual environment (recommended) and install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Usage

This project consists of two main components: **model training** and **GUI demonstration**. Below, we outline how to utilize each component.

### Model Training

The `model_training` file contains scripts and data for training the U-Net model. To train the model using Kaggle's GPU:

1. **Kaggle Setup**: Upload your dataset to Kaggle and create a new notebook.
2. **Notebook Configuration**: Configure the notebook to use the GPU provided by Kaggle.
3. **Training Code**: Copy the training code from `train_model.ipynb` to your notebook.
4. **Run Training**: Run the notebook cells to start training and inference the U-Net model.

### GUI Demonstration

The `gui` directory contains the code for building a GUI to showcase the model's segmentation performance. To run the GUI:

1. Run the GUI script:

   ```
   python gui_app.py
   ```

3. The GUI application will open, allowing you to interactively input images and observe the model's segmentation results.

## Contributing

We welcome contributions to enhance the project! If you find any issues or have suggestions for improvements, feel free to create issues or pull requests in this repository.

## License

This project is licensed under the [MIT License](LICENSE).

---

We hope this README provides you with a clear overview of the **Segmentation for Self-Driving Cars** project. If you have any questions or need further assistance, please don't hesitate to reach out.

Happy coding!

