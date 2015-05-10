import plotly.plotly as py
from plotly.graph_objs import *

class Potato:
    def __init__(self,tid):
        self.tid = tid

    def get_test_plot(self):
        twitterid = self.tid
        
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
        self.embed_url  = self.unique_url + '.embed?width=750&height=550'
        self.html_url   = self.unique_url + '.html' 
        #return self.unique_url
