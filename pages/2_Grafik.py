fig=px.sunburst(df, path=['jenis_kelamin', 'status_gizi'], values=df.value_counts().values,color_discrete_sequence=['#f66095', '#2bcdc1'])
fig.show()
