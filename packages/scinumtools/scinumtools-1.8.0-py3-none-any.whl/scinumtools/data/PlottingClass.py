from matplotlib.colors import Normalize, LogNorm
from dataclasses import dataclass
import numpy as np
from typing import Union

from ..structs import ArrayCollector

@dataclass
class Ranges:
    """ Dataclass that contains data ranges
    """
    minpos: float
    min: float
    max: float

class NormalizeData:
    """ Normalize numerical data across multiple plots
    """

    xaxis: bool
    yaxis: bool
    _collector: ArrayCollector
    
    def __enter__(self):
        return self
    
    def __exit__(self, type, value, tb):
        pass

    def __init__(self, xaxis=None, yaxis=None):
        self.xaxis = xaxis
        self.yaxis = yaxis
        columns = ['zminpos','zmin','zmax']
        if xaxis: columns += ['xminpos','xmin','xmax']
        if yaxis: columns += ['yminpos','ymin','ymax']
        self._collector = ArrayCollector(columns)

    def append(self, vdata, xdata=None, ydata=None):
        """ Append data to the range collector
        
        Statistics of x and y axes is optional

        :param vdata: Numerical data
        :param xdata: X-axis points
        :param ydata: Y-axis points
        """
        zminpos = np.nanmin(vdata[vdata>0]) if np.sum(vdata>0) else np.nan
        ranges = [zminpos,np.min(vdata),np.max(vdata)]
        if self.xaxis:
            if xdata is None:
                raise Exception("Missing x-axes values")
            xminpos = np.nanmin(xdata[xdata>0]) if np.sum(xdata>0) else np.nan
            ranges += [xminpos,np.min(xdata),np.max(xdata)]
        if self.yaxis:
            if ydata is None:
                raise Exception("Missing y-axes values")
            yminpos = np.nanmin(ydata[ydata>0]) if np.sum(ydata>0) else np.nan
            ranges += [yminpos,np.min(ydata),np.max(ydata)]
        self._collector.append(ranges)

    def data(self):
        """ Return collected ranges as a dictionary
        """
        return self._collector.to_dict()

    def xranges(self):
        """ Return x-axis ranges
        """
        return Ranges(
            minpos = np.nanmin(self._collector.xminpos),
            min = np.nanmin(self._collector.xmin),
            max = np.nanmax(self._collector.xmax)
        )
    
    def yranges(self):
        """ Return y-axis ranges
        """
        return Ranges(
            minpos = np.nanmin(self._collector.yminpos),
            min = np.nanmin(self._collector.ymin),
            max = np.nanmax(self._collector.ymax)
        )
        
    def zranges(self):
        """ Return data ranges
        """
        return Ranges(
            minpos = np.nanmin(self._collector.zminpos),
            min = np.nanmin(self._collector.zmin),
            max = np.nanmax(self._collector.zmax)
        )
    
    def linnorm(self):
        """ Return linear norm from ranges
        """
        return Normalize(
            vmin=np.nanmin(self._collector.zmin), 
            vmax=np.nanmax(self._collector.zmax)
        )

    def lognorm(self):
        """ Return logarithmic norm from ranges
        """
        return LogNorm(
            vmin=np.log10(np.nanmin(self._collector.zminpos)), 
            vmax=np.log10(np.nanmax(self._collector.zmax))
        )

class DataPlotGrid:
    data: Union[list,dict]
    ndata: int
    ncols: int
    nrows: int
    figsize: tuple

    def __init__(self, data: Union[list,dict], ncols:int=2, axsize:tuple=(4,2)):
        self.data = data
        self.ndata = len(data)
        self.ncols = ncols
        self.nrows = int(np.ceil(self.ndata/self.ncols))
        self.figsize = (self.ncols*axsize[0], self.nrows*axsize[1])

    def items(self, missing:bool=None, transpose:bool=False):
        if missing:
            for i in range(self.ndata, self.ncols*self.nrows):
                if transpose:
                    yield (i,int(i%self.nrows),int(i/self.nrows))
                else:
                    yield (i,int(i/self.ncols),int(i%self.ncols))
        else:
            if isinstance(self.data, list):
                for i,d in enumerate(self.data):
                    if transpose:
                        yield (i,int(i%self.nrows),int(i/self.nrows),d)
                    else:
                        yield (i,int(i/self.ncols),int(i%self.ncols),d)
            elif isinstance(self.data, dict):
                for i,(k,v) in enumerate(self.data.items()):
                    if transpose:
                        yield (i,int(i%self.nrows),int(i/self.nrows),k,v)
                    else:
                        yield (i,int(i/self.ncols),int(i%self.ncols),k,v)
            else:
                raise Exception('Wrong data type:', self.data)
