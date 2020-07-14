# CNN1D

## Inputs (7)

Feature|Description
:--:|:--:
j1_ptrel|ratio of the pT of each consistent to the pT of the jet
j1_etarot|rotated eta of each constituent
j1_phirot|rotated phi of each constituent
j1_erel|ratio of the energy of each consistent to the pT of the jet
j1_deltaR|sqrt ((Δeta)2 + (Δ phi)2 )
j1_costhetarel|cos (angle (constituent, jet))
j1_pdgid|PDG ID number of the constituent
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

## Model structure

    Model: "model"
    _________________________________________________________________
    Layer (type)                Output Shape                Param #   
    =================================================================
    input (InputLayer)          [(None, 100, 7)]            0         
    _________________________________________________________________
    conv1_relu_1 (Conv1D)       (None, 100, 8)              232       
    _________________________________________________________________
    conv1_relu_2 (Conv1D)       (None, 50, 4)               132       
    _________________________________________________________________
    conv1_relu_3 (Conv1D)       (None, 17, 2)               34        
    _________________________________________________________________
    flatten (Flatten)           (None, 34)                  0         
    _________________________________________________________________
    fc1_relu (Dense)            (None, 32)                  1120      
    _________________________________________________________________
    rnn_densef (Dense)          (None, 5)                   165       
    =================================================================
    Total params: 1,683
    Trainable params: 1,683
    Non-trainable params: 0
    _________________________________________________________________

<https://github.com/451488975/Jet_Classification/blob/master/CNN1D/KERAS_conv1d.json>

### Input Shape: (100, 7) *100 particles, 7 features*

### Conv1D Layers (3)

    Filters:                8 + 4 + 2
    Kernel_size:            4 + 4 + 4
    Strides:                1 + 2 + 3
    Regularizer:            Lasso regularization (l = 1e-4)
    Activation function:    Relu
    Kernel initializer:     he_normal

### Dense Layers (1)

    Perceptrons:            32
    Activation function:    lecun_uniform
    Regularizer:            Lasso regularization (l = 1e-4)
    Kernel initializer:     lecun_uniform

### Output layer (1)

    Output:                 5-class Classification
    Activation function:    Softmax
    Kernel initializer:     lecun_uniform

#### Learning rate:         1e-4

#### Optimizer:             Adam

#### Loss function:         categorical_crossentropy

#### Metrics:               Accuracy

## Example ROC Curve

![Conv1D ROC Curve](https://github.com/451488975/Jet_Classification/raw/master/CNN1D/Conv1d_ROC.png "Conv1D ROC Curve")
