import plotly.plotly as py
from plotly.graph_objs import *

class Potato:
    def __init__(self,tid):
        self.tid = []

    def get_test_plot(self):
        twitterid = tid
        
        trace0 = Scatter(
            x=[1, 2, 3, 4],
            y=[10, 15, 13, 17]
        )
        trace1 = Scatter(
            x=[1, 2, 3, 4],
            y=[16, 5, 11, 9]
        )
        data = Data([trace0, trace1])

        self.unique_url = py.plot(data, filename = 'basic-line')
        return unique_url
