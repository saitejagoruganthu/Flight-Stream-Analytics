# Create Dataset 

Click `Create dataset and create chart`

![Pasted image 20250810194615.png](./images/Pasted%20image%2020250810194615.png)

Attach a chart. For now, let's start with a `Bar chart` and click on `Create`.

After that, edit the dataset to add a Calculated Column for timestamp.

SQL Expression

```
from_unixtime(time_position)
```

Label

```
event_ts
```

Data type

```
DATETIME
```

![Pasted image 20250810195425.png](./images/Pasted%20image%2020250810195425.png)

Finally, in the Metrics tab, add a new metric `COUNT(DISTINCT)`

![Pasted image 20250810201118.png](./images/Pasted%20image%2020250810201118.png)

Click `Save`.

# Bar Chart to display Unique Flights by Country

Drag and drop `origin_country` into X-axis box.

Click on the metrics box to add Custom SQL

```
COUNT(DISTINCT icao24)
```

![Pasted image 20250810201327.png](./images/Pasted%20image%2020250810201327.png)

Click `Save`. Fill other properties as shown.

Click `Create Chart`

![Pasted image 20250811021757.png](./images/Pasted%20image%2020250811021757.png)

Click `Save` to save the chart and create a new dashboard and save again.


# KPI to display the Average Velocity of All Flights

Select the `Big Number` chart and click `Create New Chart`

![Pasted image 20250811022311.png](./images/Pasted%20image%2020250811022311.png)

To get average, we need to another metric to the dataset.

![Pasted image 20250811022509.png](./images/Pasted%20image%2020250811022509.png)

Add the metric and Subheader.

![Pasted image 20250811022551.png](./images/Pasted%20image%2020250811022551.png)

Change the Number format in Customize Tab

![Pasted image 20250811023752.png](./images/Pasted%20image%2020250811023752.png)

Add to the dashboard by clicking on `Save`.

![Pasted image 20250811023824.png](./images/Pasted%20image%2020250811023824.png)


# Heat Map - Flight Density by latitude / longitude

Create a new chart named `deck.gl Heatmap`.

![Pasted image 20250811024246.png](./images/Pasted%20image%2020250811024246.png)

Attach `longitude` and `latitude` to corresponding columns.

![Pasted image 20250811024709.png](./images/Pasted%20image%2020250811024709.png)

Go to mapbox website and signup. Get the access token from mapbox.

Export it using below command.

```
Export MAPBOX_API_KEY = "your-api-key"
```

Restart the superset.

```
superset run -p 8088 --with-threads --reload --debugger
```

![Screenshot 2025-08-11 at 3.56.55 AM.png](./images/Screenshot 2025-08-11 at 3.56.55 AM.png)

Add to the dashboard by clicking on save. The dashboard currently looks like below.

![Pasted image 20250811035615.png](./images/Pasted%20image%2020250811035615.png)


# Line Chart - Average Velocity Over time

Create a chart. Fill the properties as shown and click on `Create Chart`.

![Pasted image 20250811170014.png](./images/Pasted%20image%2020250811170014.png)

Add to the dashboard by clicking on `Save`. The final dashboard looks like below.

![Pasted image 20250811171120.png](./images/Pasted%20image%2020250811171120.png)

The Presto UI dashboard runs all 4 queries as shown below

![Pasted image 20250811171035.png](./images/Pasted%20image%2020250811171035.png)