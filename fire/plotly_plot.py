from plotly.offline import plot
import plotly.graph_objs as go

def plotly_plot(values, labels):
    fig = go.Figure(data=go.Pie(values=values, labels=labels))

    # Update layout for graph object Figure
    # https://plotly.com/python/reference/layout/
    fig.update_layout(title_text='Percentage Per Ticker',
                      xaxis_title='X_Axis',
                      yaxis_title='Y_Axis',
                      showlegend=False,
                      )
    fig.update_traces(textposition='inside', textinfo='percent+label')


    # Turn graph object into local plotly graph
    plotly_plot_obj = plot({'data': fig}, output_type='div', config=dict(displaylogo=False))

    return plotly_plot_obj