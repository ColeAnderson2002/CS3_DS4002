# NOTE: ONLY USE AND REFERENCE THIS CODE IF YOU ARE STUCK! It serves as a guide, not as something to base your entire project off of.

# Preprocessing and simple EDA starter code
import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Standard parameters
img_size = (128, 128)
batch_size = 32

# Set paths
train_dir = './snake_data/snake_data/train'
test_dir = './snake_data/snake_data/test'

# Load datasets
train_ds = tf.keras.utils.image_dataset_from_directory(
    train_dir,
    image_size=img_size,
    batch_size=batch_size,
    label_mode='int',
    shuffle=True
)

test_ds = tf.keras.utils.image_dataset_from_directory(
    test_dir,
    image_size=img_size,
    batch_size=batch_size,
    label_mode='int',
    shuffle=False
)

# Show class names
class_names = train_ds.class_names
print("Class Names:", class_names)

# Quick class distribution plot
label_counts = [0] * len(class_names)

for images, labels in train_ds.unbatch():
    label_counts[labels.numpy()] += 1

plt.bar(class_names, label_counts)
plt.xlabel('Class')
plt.ylabel('Count')
plt.title('Training Set Class Distribution')
plt.show()
