import pandas as pd
from plotnine import *

df = pd.read_csv('../20_intermediate_files/full_merge.csv')
df.head()

# florida
fl_death_comp = ['FL', 'NV', 'PA', 'IN']
fl_mme_comp = ['FL', 'GA', 'CA', 'NM']
fl_death = df[df['State'].isin(fl_death_comp)]
fl_mme = df[df['State'].isin(fl_mme_comp)]
fl = df[df['State'] == 'FL']

# texas
tx_death_comp = ['TX', 'PA', 'OH', 'IL', 'CA']
tx_death = df[df['State'].isin(tx_death_comp)]
tx = df[df['State'] == 'TX']

# washington
wa_death_comp = ['WA', 'NC', 'MA', 'CO']
wa_death = df[df['State'].isin(wa_death_comp)]
wa = df[df['State'] == 'WA']

# FLORIDA 

# diff in diff (death)
(ggplot(fl_death, aes(x ='Year', y='deaths_percap',color = 'State')) + geom_line(alpha=1) + xlim(2003, 2015) + geom_vline(xintercept = 2010))

# prepost (death)
(ggplot(fl, aes(x ='Year', y='deaths_percap',color = 'State')) + geom_line(alpha=1) + xlim(2003, 2015) + geom_vline(xintercept = 2010))


# prepost (shipment)
(ggplot(fl, aes(x ='Year', y='mme_percap',color = 'State')) + geom_line(alpha=1) + xlim(2003, 2015) + geom_vline(xintercept = 2010))

# diff in diff (shipment)
(ggplot(fl_mme, aes(x ='Year', y='mme_percap',color = 'State')) + geom_line(alpha=1) + xlim(2003, 2015) + geom_vline(xintercept = 2010))


# TEXAS
# diff in diff
(ggplot(tx_death, aes(x ='Year', y='deaths_percap',color = 'State')) + geom_line(alpha=1) + xlim(2003, 2015) + geom_vline(xintercept = 2007))
# prepost
(ggplot(tx, aes(x ='Year', y='deaths_percap',color = 'State')) + geom_line(alpha=1) + xlim(2003, 2015) + geom_vline(xintercept = 2007))

# WASHINGTON
# diff in diff
(ggplot(wa_death, aes(x ='Year', y='deaths_percap',color = 'State')) + geom_line(alpha=1) + xlim(2003, 2015) + geom_vline(xintercept = 2012))
# prepost
(ggplot(wa, aes(x ='Year', y='deaths_percap',color = 'State')) + geom_line(alpha=1) + xlim(2003, 2015) + geom_vline(xintercept = 2012))
