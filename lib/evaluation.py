from keras.models import load_model, Model
from keras import backend as K
import h5py
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc
import pandas as pd
import yaml

def makeRoc(features_val, labels_val, labels, model, outputSuffix=''):
    if 'j_index' in labels: labels.remove('j_index')   
    predict_test = model.predict(features_val)
    df = pd.DataFrame()
    fpr = {}
    tpr = {}
    auc1 = {}
    plt.figure()       
    for i, label in enumerate(labels):
        df[label] = labels_val[:,i]
        df[label + '_pred'] = predict_test[:,i]
        fpr[label], tpr[label], threshold = roc_curve(df[label],df[label+'_pred'])
        auc1[label] = auc(fpr[label], tpr[label])
        plt.plot(tpr[label],fpr[label],label='%s tagger, AUC = %.1f%%'%(label.replace('j_',''),auc1[label]*100.))
    plt.semilogy()
    plt.xlabel("Signal Efficiency")
    plt.ylabel("Background Efficiency")
    plt.ylim(0.001,1)
    plt.grid(True)
    plt.legend(loc='upper left')
    plt.figtext(0.25, 0.90,'%s_ROC_Curve'%(outputSuffix),fontweight='bold', wrap=True, horizontalalignment='right', fontsize=14)
    plt.savefig('%s_ROC.pdf'%(outputSuffix))
    return predict_test

def learningCurveLoss(history):
    plt.figure()
    plt.plot(history.history['loss'], linewidth=1)
    plt.plot(history.history['val_loss'], linewidth=1)
    plt.title('Model Loss over Epochs')
    plt.legend(['training sample loss','validation sample loss'])
    plt.xlabel('epoch')
    plt.ylabel('loss')
    plt.show()

def learningCurveAcc(history):
    plt.figure()
    plt.plot(history.history['acc'], linewidth=1)
    plt.plot(history.history['val_acc'], linewidth=1)
    plt.title('Model Loss over Epochs')
    plt.legend(['training sample accuracy','validation sample accuracy'])
    plt.legend()
    plt.xlabel('epoch')
    plt.ylabel('accuracy')
    plt.show()

        
