import pandas as pd
import plotly.graph_objects as go
import streamlit as st


df = pd.read_csv('Army_mens_basketball.csv')

dfpro = pd.read_csv('Pro_Players_College.csv')


columns_to_drop = ['Pos', 'MP','Awards',]

df.drop(columns=columns_to_drop, inplace=True)
dfpro.drop(columns=columns_to_drop, inplace=True)

columns_to_drop = []

options = df.columns.to_list()
selection = st.pills("What Statisitcs would you like to see", options, selection_mode="multi")
st.markdown(f"Your selected options: {selection}.")


for i in options[:]:
    if i not in selection:
        remove = options.pop(options.index(i))
        columns_to_drop.append(i)

#How you get the army player
player_Army = st.text_input("what Army Player do you want to see", placeholder='Ryan Curry').title()
ARMY = df.loc[df['Player'] == player_Army]

#how to get the pro player
Pro_player = st.text_input("what Pro Player do you want to see", placeholder='Jimmy Butler').title()
PRO = dfpro.loc[(dfpro['Player'] == Pro_player) & (dfpro['Class'] == ARMY['Class'].iloc[0])]

#Creating the list so you can plot the values
#filter out the columns that are not selected
r_Army = ARMY.drop(columns= columns_to_drop, inplace=False)
r_Army = r_Army.iloc[0].to_list()
r_Pro_player = PRO.drop(columns=columns_to_drop, inplace=False)
r_Pro_player = r_Pro_player.iloc[0].to_list()

r_range = max(r_Army + r_Pro_player)
    



#Plotting the two radar charts
fig = go.Figure()

fig.add_trace(go.Scatterpolar(
      r=r_Army,
      theta=selection,
      fill='toself',
      name=player_Army,
      fillcolor='rgba(0, 0, 255, 0.3)'
))
fig.add_trace(go.Scatterpolar(
      r=r_Pro_player,
      theta=selection,
      fill='toself',
      name=Pro_player,
      fillcolor='rgba(255, 0, 0, 0.3)'
))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0,r_range]
    )),
  showlegend=False
)


st.plotly_chart(fig)
