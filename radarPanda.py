import pandas as pd
import pygal

df = pd.read_csv('Army_mens_basketball.csv')

dfpro = pd.read_csv('Pro_Players_College.csv')

radar_chart = pygal.Radar()

columns_to_drop = ['Pos', 'MP','Awards']

df.drop(columns=columns_to_drop, inplace=True)
dfpro.drop(columns=columns_to_drop, inplace=True)

player_Army = input('what player do you want to see: ').title()

classes = list(df[df['Player'] == player_Army].iloc[0])[0]

players = dfpro['Player']

for i in set(players):
        print(i)

Pro_player=input(f'What pro player do you want to compare him to: ')

i = df[df['Player'] == player_Army]
z = dfpro[(dfpro['Player'] == Pro_player) & (dfpro['Class'] == classes)]

important = list(df.columns[5:10])
zimportant = list(dfpro.columns[5:10])

x_values = list(i[important].iloc[0])
prox_values = list(z[zimportant].iloc[0])

radar_chart.x_labels = important
radar_chart.add(player_Army, x_values)
radar_chart.add(Pro_player, prox_values)
radar_chart.render_to_file('BBPanda.svg')