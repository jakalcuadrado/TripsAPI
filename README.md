# TripsAPI

Results of the coding challenge

- There must be an automated process to ingest and store the data. **Done**
- Trips with similar origin, destination, and time of day should be grouped together.**No Done**
- Develop a way to obtain the weekly average number of trips for an area, defined by a bounding box (given by coordinates) or by a region. **Done**
- Develop a way to inform the user about the status of the data ingestion without using a polling solution.**No Done**
- The solution should be scalable to 100 million entries. It is encouraged to simplify the data by a data model. Please add proof that the solution is scalable.**No Done**
- Use a SQL database.**Done**

- Containerize your solution.**Done**
- Sketch up how you would set up the application using any cloud provider (AWS, GoogleCloud, etc).**No Done**
- Include a .sql file with queries to answer these questions:
    > From the two most commonly appearing regions, which is the latest datasource?  [Link](db/latestDataSource.sql)

    > What regions has the "cheap_mobile" datasource appeared in? [Link](db/cheap_mobile.sql)