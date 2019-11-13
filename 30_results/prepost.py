import pandas as pd
import numpy as np
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

###

# ANALYSIS PLOTS

death_yrs = (2003,2015)
death_scale = np.arange(2003, 2016, 1)

ship_yrs = (2006, 2013)
ship_scale = np.arange(2006, 2013, 1)

# FLORIDA 

fl_policy = 2010

# FLORIDA DEATHS

# diff in diff (death)
(ggplot(fl_death, aes(x ='Year', y='deaths_percap',color = 'State')) + geom_line(alpha=1) + geom_vline(xintercept = fl_policy) + labs(title = 'Florida: Diff-in-Diff Plot of Opioid Deaths') + ylab('Overdose Deaths per Capita') + scale_x_continuous(breaks = death_scale, limits= death_yrs) )

# prepost (death)
(ggplot(fl, aes(x ='Year', y='deaths_percap', color = 'State')) + geom_line(alpha=1) + labs(title = 'Florida: Pre-Post Plot of Opioid Deaths') + ylab('Overdose Deaths per Capita') + scale_x_continuous(breaks = death_scale, limits = death_yrs) + geom_vline(xintercept = fl_policy))

# FLORIDA SHIPMENTS

# prepost (shipment)
(ggplot(fl, aes(x ='Year', y='mme_percap', color = 'State')) + geom_line(alpha=1) + geom_vline(xintercept = fl_policy) + labs(title = 'Florida: Pre-Post Plot of Opioid Shipments') + ylab('Morphine Equivalents per Capita') + scale_x_continuous(breaks = ship_scale, limits = ship_yrs))

# diff in diff (shipment)
(ggplot(fl_mme, aes(x ='Year', y='mme_percap',color = 'State')) + geom_line(alpha=1) + geom_vline(xintercept = fl_policy) + labs(title = 'Florida: Diff-in-Diff Plot of Opioid Shipments') + ylab('Morphine Equivalents per Capita') + scale_x_continuous(breaks = ship_scale, limits = ship_yrs))


# TEXAS

tx_policy = 2007

# diff in diff
(ggplot(tx_death, aes(x ='Year', y='deaths_percap', color = 'State')) + geom_line(alpha=1) + scale_x_continuous(breaks = death_scale, limits = death_yrs) + geom_vline(xintercept = tx_policy) + labs(title = 'Texas: Diff-in-Diff Plot of Opioid Deaths') + ylab('Overdose Deaths per Capita'))

# prepost
(ggplot(tx, aes(x ='Year', y='deaths_percap',color = 'State')) + geom_line(alpha=1) + scale_x_continuous(breaks = death_scale, limits = death_yrs) + geom_vline(xintercept = tx_policy) + labs(title = 'Texas: Pre-Post Plot of Opioid Deaths') + ylab('Overdose Deaths per Capita'))

# WASHINGTON

wa_policy = 2012

# diff in diff
(ggplot(wa_death, aes(x ='Year', y='deaths_percap',color = 'State')) + geom_line(alpha=1) + scale_x_continuous(breaks = death_scale, limits = death_yrs) + geom_vline(xintercept = wa_policy) + labs(title = 'Washington: Diff-in-Diff Plot of Opioid Deaths') + ylab('Overdose Deaths per Capita'))

# prepost
(ggplot(wa, aes(x ='Year', y='deaths_percap',color = 'State')) + geom_line(alpha=1) + scale_x_continuous(breaks = death_scale, limits = death_yrs) + geom_vline(xintercept = wa_policy) + labs(title = 'Washington: Pre-Post Plot of Opioid Deaths') + ylab('Overdose Deaths per Capita'))
