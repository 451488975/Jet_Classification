import numpy as np
import h5py
import pandas as pd
import os
from tqdm import tqdm

def downsize(df,size,seed,labels):
    jet_dict = {}
    np.random.seed(seed)
    for label in labels:
        jet_dict[label] = np.random.choice(a=np.unique(df[df[label]==1].j_index), size=size,replace=False )
    mini_df = pd.DataFrame()
    for label in labels:
        mini_df = pd.concat([mini_df,df[df.j_index.isin(jet_dict[label])]],axis=0)
    return mini_df

def downsize_unbalanced(df,max_size,seed,labels,ratio):
    '''max_size is the baseline. It is 1 in ratio.'''
    jet_dict = {}
    np.random.seed(seed)
    for i,label in enumerate(labels):
        jet_dict[label] = np.random.choice(a=np.unique(df[df[label]==1].j_index), size= int(max_size*ratio[i]),replace=False )
    mini_df = pd.DataFrame()
    for label in labels:
        mini_df = pd.concat([mini_df,df[df.j_index.isin(jet_dict[label])]],axis=0)
    return mini_df


def loadNdownsize (filePath,features,labels,size,seed,ratio=None):
    '''
    features: 'j_index' is necessary!
    '''
    with h5py.File(filePath+"processed-pythia82-lhc13-all-pt1-50k-r1_h022_e0175_t220_nonu_withPars_truth_0.z", 'r') as f:
        treeArray = f['t_allpar_new'][()]
    df = pd.DataFrame(treeArray, columns=features+labels) 
    if ratio==None:
        mini_df = downsize(df,size,seed,labels)
    else:
        mini_df = downsize_unbalanced(df,size,seed,labels,ratio=ratio)
    # Sort constituents by pt in each jet
    mini_df.sort_values(by=['j1_ptrel'],ascending=False,inplace=True)
    # Add new feature "constituents_index", "j1_ptLog", "j1_eLog"
    cIndex = np.array([],dtype='int8')
    for i in tqdm(np.unique(mini_df['j_index'])):
        new_cIndex = np.arange(mini_df[mini_df['j_index']==i].shape[0])
        cIndex = np.append(cIndex, new_cIndex)

    mini_df['j1_ptLog'] = np.log(mini_df['j1_pt'])
    mini_df['j1_eLog'] = np.log(mini_df["j1_e"])
    mini_df['constituents_index'] = cIndex
    mini_df = mini_df.sort_values(by='j_index')

    mini_df.drop(['j1_pt','j1_e'],axis=1,inplace=True)
    _features = mini_df.columns.values.tolist()
    
    _features.remove('j_q')
    _features.remove('j_t')
    _features.remove('j_g')
    _features.remove('j_w')
    _features.remove('j_z')
    return mini_df, _features

def saveAsH5(filePath,df, size,features,labels,ratio=None):
# Since list is not valid in Dataframe, create a nparray to store the label list
    if ratio==None:
        label_list = np.vstack([df[label] for label in labels]).T
    else:
        target = labels[ratio.index(1)]
        label_list = np.vstack([df[target], np.abs(df[target]-1)]).T
    
    if ratio==None:
        savePath = filePath+"data_%sjets_%dlabels"%(size*5,len(labels))+'.h5'
    else:
        savePath = filePath+"data_%sjets_%dlabels_unbalanced"%(size*np.sum(ratio),len(labels))+'.h5'
        
    with h5py.File(savePath, 'w') as f:
        for col in features:
            f.create_dataset(col, data=df[col])
        f.create_dataset('label', data = label_list)

def LoadTransSave (filePath, features, labels, size, seed,ratio=None):
    mini_df, _features = loadNdownsize(filePath,features, labels,size=size,seed=seed,ratio=ratio)
    saveAsH5(filePath, df = mini_df, size=size, features=_features, labels=labels,ratio=ratio)

# # To test:
# filePath = './data/'
# features = ['index','j1_pt','j1_eta','j1_phi','j_mass','j_multiplicity','j1_etarot','j1_phirot','j_pt','j1_etarel','j1_phirel','j_index']
# labels = ['j_g','j_q','j_w','j_z','j_t']
# size=20
# seed=42
# ratio=[1,.2,.5,.1,.3]
# LoadTransSave(filePath,features, labels,size=size,seed=seed)
