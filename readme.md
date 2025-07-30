# Waste Classification

Description goes here

## Overview

The system can classify waste into 10 distinct categories, making it easier to sort waste.

## The Algorithm

### Model Architecture

[The model](https://drive.google.com/file/d/1rxGChiVVU55-F3HUiedWlTLn6W6AyduL/view?usp=sharing) uses a ResNet-18 architecture that has been retrained on [this waste classification dataset](https://www.kaggle.com/datasets/mostafaabla/garbage-classification?select=garbage_classification). For training, 500 images were used for each category, 90 were used for validation, and 50 were used for testing.

### Waste Categories

The model classifies waste into the following 10 categories:

1. Battery
2. Biological
3. Cardboard
4. Clothes
5. Green-Glass
6. Metal
7. Paper
8. Plastic
9. Trash
10. White-Glass

## Setup

### 1. Install Jetson Inference

```
git clone --recursive https://github.com/dusty-nv/jetson-inference
cd jetson-inference
mkdir build
cd build
cmake ../
make
sudo make install
```

### 2. Prepare Dataset

Organize images like this:
```
jetson-inference/python/training/classification/data/trash_data/
├── train/
│   ├── Battery/
│   ├── Biological/
│   ├── Cardboard/
│   ├── Clothes/
│   ├──  Green-Glass/
│   ├── Metal/
│   ├── Paper/
│   ├── Plastic/
│   ├── Trash/
│   ├── White-Glass/
├── val/
└── test/

```

### 3. Training

1. Enable more memory: `echo 1 | sudo tee /proc/sys/vm/overcommit_memory`
2. Train the model (I used batch size of 4)
  ```
  cd jetson-inference
  ./docker/run.sh
  cd python/training/classification
  python3 train.py --model-dir=models/trash_classification data/trash_data
  ```
3. Export Model
  ```
  # Still in docker container:
  python3 onnx_export.py --model-dir=models/trash_classification
  ```

## Using the Model

### Set Variables
```
cd jetson-inference/python/training/classification
NET=models/trash_classification
DATASET=data/trash_data
```

### Test on Image
```
imagenet.py --model=$NET/resnet18.onnx --input_blob=input_0 --output_blob=output_0 --labels=$DATASET/labels.txt $DATASET/test/battery/<image.jpg> result.jpg
```
Replace <image.jpg> with your actual image.
### Live Camera
```
imagenet.py --model=$NET/resnet18.onnx --input_blob=input_0 --output_blob=output_0 --labels=$DATASET/labels.txt /dev/video0 output.mp4
```

### Process Video
```
imagenet.py --model=$NET/resnet18.onnx --input_blob=input_0 --output_blob=output_0 --labels=$DATASET/labels.txt input.mp4 output.mp4
```

## Resources
* [The Finished Model](https://drive.google.com/file/d/1rxGChiVVU55-F3HUiedWlTLn6W6AyduL/view?usp=sharing)
* [Dataset](https://www.kaggle.com/datasets/mostafaabla/garbage-classification?select=garbage_classification)
* [ImageNet Documentation](https://github.com/dusty-nv/jetson-inference/blob/master/docs/imagenet-console-2.md)
* [Jetson Inference GitHub](https://github.com/dusty-nv/jetson-inference)
* [Video Demonstration]()
