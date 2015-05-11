import plotly.plotly as py
from project import Project
from plotly.graph_objs import *

class Potato:

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

        self.unique_url = py.plot(data, filename = 'basic-line', auto_open=False)
        self.embed_url = self.unique_url + '.embed?width=750&height=550'
        self.html_url  = self.unique_url + '.html' 
        #return self.unique_url

    def get_result(self, tid):
        self.tid = tid
        potato = Project(user_name=tid, SUPPORT=0.3)

        #potato.shoot_lazy()
        potato.shoot_eager()

        result = potato.ranked_recommendations
        sorted_list = sorted(result.items(), key= lambda (k,v) : v, reverse=True)
        
        """
            turn the dic into array of items, get its first set 
            and then its second value to get the high value in 
            the result map
        """
        highest_value =  sorted_list[0][1]
        self.top = []
        for key, value in result.items():
            if highest_value == value:
                self.top.append(key)

        data = Data([
            Bar(
                x = result.keys(),
                y = result.values()
                )
            ])
        self.unique_url = py.plot(data, filename='basic-bar', auto_open=False)
        self.html_url = self.unique_url + 'html'
        self.embed_url = self.unique_url + '.embed?width=750&height=550'




