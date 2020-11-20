import scipy.stats as ss
import matplotlib.pyplot as plt
import numpy as np

def random_uniform(bottom, ceiling, count):
    x = ss.uniform.rvs(size=count)
    return (ceiling - bottom) * x + bottom

def random_normal(mean, std, count):
    x = ss.norm.rvs(size=count)
    return std * x + mean

def random_expo(mean, count):
    x = ss.expon.rvs(size=count)
    return mean * x

def plotting(function,plot1,plot2,bins):
    dist1 = function(*plot1)
    dist2 = function(*plot2)

    plt.style.use('seaborn')
    plt.figure(figsize=(10,10))
    # bins = np.arange(min(dist2), max(dist2))
    
    ax1 = plt.subplot(2,2,1)
    plt.hist(dist1, bins=bins)

    plt.subplot(2,2,2, sharey=ax1)
    plt.hist(dist2, bins=bins)

    plt.show()

# plotting(random_uniform,[10,15,100],[10,60,1000],10)
# plotting(random_normal,[10,1,1000],[10,50,1000],50)
# plotting(random_expo,[10,100],[10,1000],100)