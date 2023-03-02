SELECT t1.region, MAX(t1.datetime) AS latest_datetime, t1.datasource
FROM trips t1
JOIN (
  SELECT region
  FROM trips 
  GROUP BY region
  ORDER BY COUNT(*) DESC
  LIMIT 2
) t2 ON t1.region = t2.region
GROUP BY t1.region, t1.datasource
ORDER BY COUNT(*) DESC, latest_datetime DESC
LIMIT 1;