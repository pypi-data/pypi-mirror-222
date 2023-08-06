# Copyright 2020, General Electric Company. All rights reserved. See https://github.com/xcist/code/blob/master/LICENSE

import numpy.matlib as nm
from gecatsim.pyfiles.CommonTools import *
from gecatsim.pyfiles.Scatter_ConvolutionModel import get_scatter_kernel
from tqdm import tqdm

# This is a simplified kernel based scatter correction algorithm.
def Scatter_Correction(cfg, airscan, offsetScan, phantomScan):
    print("Applying Scatter Correction ... ", end='')

    ###--------- Get scatter kernel
    if cfg.physics.scatterKernelCallback:
        cfg.scatter_kernel = feval(cfg.physics.scatterKernelCallback, cfg)
    else:
        cfg.scatter_kernel = get_scatter_kernel()
            
    ###--------- log
    #if cfg.protocol.airViewCount==1:
    #    airscan = nm.repmat(airscan, cfg.protocol.viewCount, 1)
    #if cfg.protocol.offsetViewCount==1:
    #    offsetScan = nm.repmat(offsetScan, cfg.protocol.viewCount, 1)
    prep = (phantomScan-offsetScan)/(airscan-offsetScan)
    smallValue = 1.E-10
    prep[prep<smallValue] = smallValue
    prep = -np.log(prep)

    for viewId in tqdm(range(cfg.protocol.viewCount)):
        if not hasattr(cfg.physics, "scatterScaleFactor"):
            cfg.physics.scatterScaleFactor = 1
        sc_preConv = phantomScan[viewId,:]*prep[viewId,:]*0.025*cfg.physics.scatterScaleFactor
        sc_preConv = sc_preConv.reshape(cfg.scanner.detectorRowCount, cfg.scanner.detectorColCount)
        sc_conv = conv2(sc_preConv, cfg.scatter_kernel, 'same')
        sc_conv = sc_conv.ravel()
        phantomScan[viewId,:] -= sc_conv
        
        # import matplotlib.pyplot as plt
        # sc_conv = sc_conv.reshape(cfg.scanner.detectorRowCount, cfg.scanner.detectorColCount)
        # plt.plot(sc_conv[32, :])
        # plt.show()
    
    print("done.\n")
    
    return airscan, offsetScan, phantomScan

    
