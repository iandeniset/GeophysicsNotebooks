def create_data(data):
    import numpy as np

    '''Makes a simple SEGY ascii file exported from OpendTect and maps it into a 3D array for manipulation.  
       Must export the file with in/xl information!
       '''
    
    #Inlines are stored in the first time sample location (i.e index 0)
    #Crosslines are stored in the second time sample location (i.e index 1)
    inmax,inmin = np.max(data[:,0]) , np.min(data[:,0])#find the max/min inline
    xlmax,xlmin = np.max(data[:,1]) , np.min(data[:,1])#find crossline max/min
    samp = len(data[1,:])#find the amount of time samples in data
    time = samp - 2.0 #remove the in/xl values from the time values
    
    il,xl = (inmax-inmin) , (xlmax-xlmin) #find in/xl range
    
    print('The inline min and max are: ', inmin,inmax)
    print('The crossline min and max are: ', xlmin,xlmax)
    print('The number of inlines is: ', il)
    print('The number of crosslines is: ', xl)
    print('The number of time samples are: ', time)
    
    
    mapped_data = np.zeros([il,xl,time])
    print('The shape of the mapped data empty matrix is :', mapped_data.shape)
    np.place(mapped_data, mapped_data==0.0, np.nan)
    
    for i in range(len(data)):
        inl = data[i,0] - inmax
        xln = data[i,1] - xlmax
        mapped_data[inl,xln] = data[i,2:]
        
    return mapped_data