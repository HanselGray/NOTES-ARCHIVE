# COMPUTER VISION

# I. BASIC GRAY LEVEL TRANSFORMATION

## 1. Image Negatives:

- The negative of an image with gray levels in the range [0, L-1] is obtained by s = L - 1 - r

![Image-negative](Image_negative.png)

## 2. Log-transformations:

![Log-transform](Log-transformation-1.png)

1. Log-transform:
    - **Characteristic**:
        1. This transformation maps a narrow range of low gray-level values in the input image into a wider range of output levels. 
        2. The opposite is true of higher values of input levels. 
    - **Usage**: Expand the values of dark pixels in an image while compressing the higher-level values.

2. Inverse log-transform:

- **Characteristic**: Opposite to log-transform.
- **Usage**: Compress dark pixels, expand light pixels.

## 3. Power-Law (Gamma) Transformations:

![Gamma-transformation](Gamma-transformation.png)

![Gamma-correction](Gamma-correction.png)

## 4. Piecewise-linear transformation:

![Piecewise-linear](Piecewise-linear.png)

![Piecewise-linear](Piecewise-linear2.png)

## 5. Histogram equalization:

![Histogram-eq](Histogram-equalization1.png)

![Histogram-eq](Histogram-equalization2.png)


- **HISTOGRAM EQ FOR COLOR IMAGES**:

![Histogram-eq](Histogram-equalization-color.png)

# II. IMAGE FILTERING

## 1. Convolution and Spatial-filtering:

### 1.1. Convolution and Correlation:

![Spatial-convolution](Spatial-convolution.png)

![Correlation-vs-convolution](Correlation-vs-convolution.png)

## 2. Smooth filtering:

### 2.1 Mean filtering:

![Mean-filtering](Mean-filtering.png)

![Weighted-average-filtering](Weigted-average-filtering.png)

### 2.2. Gaussian filtering:

![Smooth-filtering](Smooth-filtering-example.png)

# III. Arithmetical/Logical Operations

## 1. AND operation: 

![abc](AND-op.png)

## 2. OR op:

![ab](OR-op.png)

## 3. Image addition:

![Image-addition.png](Image-addition.png)

## 4. Average image:

![avg-img](Average-image.png)

![avg-img-2](Average-image2.png)

## 5. Image subtraction:

![img-sub](Image-subtraction.png)

![img-sub-2](Image-subtraction2.png)

## 6. Image multiplication:

- Pretty much the same as image addition.

# IV. BINARY IMAGES, THRESHOLDING AND MORPHOLOGICAL OPERATORS

## 1. Binary images:

![bin-img](Bin-img.png)

## 2. Thresholding:

![threshold](Thresholding.png)

![threshold2](Thresholding2.png)

![threshold3](Thresholding3.png)

![threshold4](Thresholding4.png)

## 3. Morphological operators:

![Maskk](Structuring-elements.png)

### 3.1 Dilation:

![Dilation](Dilation.png)

![Dilation](Dilation2.png)

![Dilation](Dilation3.png)

### 3.2 Erosion:

![Erosion](Erosion.png)

![Erosion](Erosion2.png)

![Erosion](Erosion3.png)

### 3.3 Opening:

- Erode, then dilate
- Remove small objects, keep original shape

### 3.4 Closing: 

- Dilate, then erode 
- Fill holes, but keep original shape

# V. CONNECTED COMPONENT LABELING:

- For region labeling: 
    - We use 4-connexity
    - Each loop, we compare 2 neighbors.

- For edge labeling:
    - We use 8-connexity
    - Each loop, we compare 4 neighbors.

![Connected-labeling](Connected-component.png)

# VI. FREQUENCY IN IMAGES:

![Freq-in-img](Frequency-in-img.png)