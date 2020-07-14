# CNN2D

## Inputs (3)

Feature|Description
:--:|:--:
j1_etarot|rotated eta of each constituent
j1_phirot|rotated phi of each constituent
j1_ptrel|ratio of the pT of each consistent to the pT of the jet
(j1_index)|This will be dropped in training
MaxParticles: 100

## Labels (5)

Label|Description
:--:|:--:
j_g|Gluon jet
j_q|Light-quark jet
j_w|W-boson
j_z|Z-boson
j_t|Top-quark
(j1_index)|This will be dropped in training

## Preprocessing

    2D feature map (etarot, phirot) weighted by ptrel
    binning: 40×40, range: [0.8,0.8] in (etarot, phirot)
    Pixelated each jet as input to 2D CNN.
    Jet image can also be used as input to the ResNet-50

## Model structure

### Input Shape: (40, 40, 1)

### Conv2d Layers (3)

    Kernel Size:            (11,11) + (3,3) + (3,3)
    Strides:                (1,1) + (2,2) + (2,2)
    Number of Filters:      8 + 4 + 2
    Activation function:    Relu
    Kernel initializer:     he_normal
    Padding:                Same

### Flatten Layers (1)

### Dense Layers (1)

    Perceptrons:            32
    Activation function:    Relu

### Output layer (1)

    Output:                 5-class Classification
    Activation function:    Softmax
    Kernel initializer:     lecun_uniform

#### Learning rate: 1e-4

#### Optimizer: Adam

#### Loss function: categorical_crossentropy

#### Metrics: Accuracy

### Example ROC Curve

![Conv1D ROC Curve](https://github.com/451488975/Jet_Classification/raw/master/CNN2D/Conv2d_ROC.png "Conv1D ROC Curve")
