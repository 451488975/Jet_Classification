# Dense Neural Network (DNN)

## Inputs (16)

Feature|Description
:--:|:--:
j_zlogz|Jet splitting fraction
j_c1_b0_mmdt, j_c1_b1_mmdt, j_c1_b2_mmdt, j_c2_b1_mmdt, j_c2_b2_mmdt, j_d2_b1_mmdt, j_d2_b2_mmdt, j_d2_a1_b1_mmdt, j_d2_a1_b2_mmdt, j_m2_b1_mmdt, j_m2_b2_mmdt, j_n2_b1_mmdt, j_n2_b2_mmdt|Energy Correlation Function after Modified Mass Drop Tagger
j_mass_mmdt|jet mass computed based on modified mass drop tagger
j_multiplicity|number of constituents

## Labels (5)

Label|Description
:--:|:--:
j_g|Gluon jet
j_q|Light-quark jet
j_w|W-boson
j_z|Z-boson
j_t|Top-quark

## Model structure

    Model: "model_1"
    _________________________________________________________________
    Layer (type)                 Output Shape              Param #   
    =================================================================
    input_2 (InputLayer)         [(None, 16)]              0         
    _________________________________________________________________
    fc1_relu (Dense)             (None, 64)                1088      
    _________________________________________________________________
    fc2_relu (Dense)             (None, 32)                2080      
    _________________________________________________________________
    fc3_relu (Dense)             (None, 32)                1056      
    _________________________________________________________________
    output_softmax (Dense)       (None, 5)                 165       
    =================================================================
    Total params: 4,389
    Trainable params: 4,389
    Non-trainable params: 0
    _________________________________________________________________

### Input Shape (16)

### Dense Layers (1)

    Neurons:                64 + 32 + 32
    Activation function:    Relu
    Regularizer:            Lasso regularization (l = 1e-4)
    Kernel initializer:     lecun_uniform

### Output layer (1)

    Output:                 5-class Classification
    Activation function:    Softmax
    Kernel initializer:     lecun_uniform

#### Learning rate: 1e-4

#### Optimizer: Adam

#### Loss function: binary_crossentropy

#### Metrics: Accuracy

### Example ROC Curve

![DNN ROC Curve](https://github.com/451488975/Jet_Classification/raw/master/DNN/DNN_ROC.png "DNN ROC Curve")
