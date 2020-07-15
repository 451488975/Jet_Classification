# Convolutional Neural Network
https://docs.google.com/document/d/1bp4oxD565IObtLr8xh-4UKNAC1taZ59tJH6VHr2x8SE/edit
## CNN2D

### Inputs (3)

Feature|Description
:--:|:--:
j1_etarot|rotated eta of each constituent
j1_phirot|rotated phi of each constituent
j1_ptrel|ratio of the pT of each consistent to the pT of the jet
(j1_index)|This will be dropped in training
MaxParticles: 100

### Labels (5)

Label|Description
:--:|:--:
j_g|Gluon jet
j_q|Light-quark jet
j_w|W-boson
j_z|Z-boson
j_t|Top-quark
(j1_index)|This will be dropped in training

### Preprocessing

    2D feature map (etarot, phirot) weighted by ptrel
    binning: 40×40, range: [0.8,0.8] in (etarot, phirot)
    Pixelated each jet as input to 2D CNN.
    Jet image can also be used as input to the ResNet-50

### Model structure

    Model: "model"
    _________________________________________________________________
    Layer (type)                 Output Shape              Param #   
    =================================================================
    input_1 (InputLayer)         [(None, 40, 40, 1)]       0         
    _________________________________________________________________
    conv1_relu (Conv2D)          (None, 40, 40, 8)         976       
    _________________________________________________________________
    conv2_relu (Conv2D)          (None, 20, 20, 4)         292       
    _________________________________________________________________
    conv3_relu (Conv2D)          (None, 10, 10, 2)         74        
    _________________________________________________________________
    flatten (Flatten)            (None, 200)               0         
    _________________________________________________________________
    dense (Dense)                (None, 32)                6432      
    _________________________________________________________________
    output_softmax (Dense)       (None, 5)                 165       
    =================================================================
    Total params: 7,939
    Trainable params: 7,939
    Non-trainable params: 0
    _________________________________________________________________

#### Input Shape: (40, 40, 1)

#### Conv2d Layers (3)

    Kernel Size:            (11,11) + (3,3) + (3,3)
    Strides:                (1,1) + (2,2) + (2,2)
    Number of Filters:      8 + 4 + 2
    Activation function:    Relu
    Kernel initializer:     he_normal
    Padding:                Same

#### Flatten Layers (1)

#### Dense Layers (1)

    Perceptrons:            32
    Activation function:    Relu

#### Output layer (1)

    Output:                 5-class Classification
    Activation function:    Softmax
    Kernel initializer:     lecun_uniform

##### Learning rate: 1e-4

##### Optimizer: Adam

##### Loss function: categorical_crossentropy

##### Metrics: Accuracy

### Example ROC Curve

![Conv2D ROC Curve](https://github.com/451488975/Jet_Classification/raw/master/CNN2D/Conv2d_ROC.png "Conv2D ROC Curve")
