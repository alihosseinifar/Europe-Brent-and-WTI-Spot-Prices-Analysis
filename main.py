
import pandas as pd

# Read CSV files and store them in DataFrames
df1_day = pd.read_csv('brent-day.csv')
df1_week = pd.read_csv('brent-week.csv')
df1_month = pd.read_csv('brent-month.csv')
df1_year = pd.read_csv('brent-year.csv')

# Convert the 'Date' column to datetime format for all DataFrames
df1_day['Date'] = pd.to_datetime(df1_day['Date'])
df1_week['Date'] = pd.to_datetime(df1_week['Date'])
df1_month['Date'] = pd.to_datetime(df1_month['Date'])
df1_year['Date'] = pd.to_datetime(df1_year['Date'])

# Group the data by different frequencies (weekly, monthly, yearly) and sum the values
df1_weekly = df1_day.groupby(pd.Grouper(key='Date', freq='W')).sum()
df1_monthly = df1_day.groupby(pd.Grouper(key='Date', freq='M')).sum()
df1_yearly = df1_day.groupby(pd.Grouper(key='Date', freq='Y')).sum()

# Visualizations
import matplotlib.pyplot as plt
# Daily Data Brent
plt.figure(figsize=(10, 6))
plt.plot(df1_day['Date'], df1_day['Brent Spot Price'])
plt.xlabel('Date')
plt.ylabel('Brent Spot Price')
plt.title('Daily Data - Brent')
plt.show()

# Weekly Data Brent
plt.figure(figsize=(10, 6))
plt.plot(df1_weekly.index, df1_weekly['Brent Spot Price'])
plt.xlabel('Date')
plt.ylabel('Brent Spot Price')
plt.title('Weekly Data - Brent')
plt.show()

# Monthly Data Brent
plt.figure(figsize=(10, 6))
plt.plot(df1_monthly.index, df1_monthly['Brent Spot Price'])
plt.xlabel('Date')
plt.ylabel('Brent Spot Price')
plt.title('Monthly Data - Brent')
plt.show()

# Yearly Data Brent
plt.figure(figsize=(10, 6))
plt.plot(df1_yearly.index, df1_yearly['Brent Spot Price'])
plt.xlabel('Date')
plt.ylabel('Brent Spot Price')
plt.title('Yearly Data - Brent')
plt.show()


# Read CSV files and store them in DataFrames
df2_day = pd.read_csv('wti-day.csv')
df2_week = pd.read_csv('wti-week.csv')
df2_month = pd.read_csv('wti-month.csv')
df2_year = pd.read_csv('wti-year.csv')

# Convert the 'Date' column to datetime format for all DataFrames
df2_day['Date'] = pd.to_datetime(df2_day['Date'])
df2_week['Date'] = pd.to_datetime(df2_week['Date'])
df2_month['Date'] = pd.to_datetime(df2_month['Date'])
df2_year['Date'] = pd.to_datetime(df2_year['Date'])

# Group the data by different frequencies (weekly, monthly, yearly) and sum the values
df2_weekly = df2_day.groupby(pd.Grouper(key='Date', freq='W')).sum()
df2_monthly = df2_day.groupby(pd.Grouper(key='Date', freq='M')).sum()
df2_yearly = df2_day.groupby(pd.Grouper(key='Date', freq='Y')).sum()

# Daily Data WTI
plt.figure(figsize=(10, 6))
plt.plot(df2_day['Date'], df2_day['WTI Spot Price'])
plt.xlabel('Date')
plt.ylabel('WTI Spot Price')
plt.title('Daily Data - WTI')
plt.show()

# Weekly Data WTI
plt.figure(figsize=(10, 6))
plt.plot(df2_weekly.index, df2_weekly['WTI Spot Price'])
plt.xlabel('Date')
plt.ylabel('WTI Spot Price')
plt.title('Weekly Data - WTI')
plt.show()

# Monthly Data WTI
plt.figure(figsize=(10, 6))
plt.plot(df2_monthly.index, df2_monthly['WTI Spot Price'])
plt.xlabel('Date')
plt.ylabel('WTI Spot Price')
plt.title('Monthly Data - WTI')
plt.show()

# Yearly Data WTI
plt.figure(figsize=(10, 6))
plt.plot(df2_yearly.index, df2_yearly['WTI Spot Price'])
plt.xlabel('Date')
plt.ylabel('WTI Spot Price')
plt.title('Yearly Data - WTI')
plt.show()


#plot for both Brent and WTI Spot Prices together for better comparison
import matplotlib.pyplot as plt

# Create a figure with two subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Plot Daily Data - Brent
axs[0, 0].plot(df1_day['Date'], df1_day['Brent Spot Price'], label='Brent', color='blue')
axs[0, 0].plot(df2_day['Date'], df2_day['WTI Spot Price'], label='WTI', color='green')
axs[0, 0].set_xlabel('Date')
axs[0, 0].set_ylabel('Spot Price')
axs[0, 0].set_title('Daily Data')
axs[0, 0].legend()

# Plot Weekly Data - Brent
axs[0, 1].plot(df1_weekly.index, df1_weekly['Brent Spot Price'], label='Brent', color='blue')
axs[0, 1].plot(df2_weekly.index, df2_weekly['WTI Spot Price'], label='WTI', color='green')
axs[0, 1].set_xlabel('Date')
axs[0, 1].set_ylabel('Spot Price')
axs[0, 1].set_title('Weekly Data')
axs[0, 1].legend()

# Plot Monthly Data - Brent
axs[1, 0].plot(df1_monthly.index, df1_monthly['Brent Spot Price'], label='Brent', color='blue')
axs[1, 0].plot(df2_monthly.index, df2_monthly['WTI Spot Price'], label='WTI', color='green')
axs[1, 0].set_xlabel('Date')
axs[1, 0].set_ylabel('Spot Price')
axs[1, 0].set_title('Monthly Data')
axs[1, 0].legend()

# Plot Yearly Data - Brent
axs[1, 1].plot(df1_yearly.index, df1_yearly['Brent Spot Price'], label='Brent', color='blue')
axs[1, 1].plot(df2_yearly.index, df2_yearly['WTI Spot Price'], label='WTI', color='green')
axs[1, 1].set_xlabel('Date')
axs[1, 1].set_ylabel('Spot Price')
axs[1, 1].set_title('Yearly Data')
axs[1, 1].legend()

# Adjust layout
plt.tight_layout()

# Show the plots
plt.show()
