SELECT ROUND(SUM(t.tiv_2016)::NUMERIC, 2) AS tiv_2016
FROM (SELECT tiv_2016,
             COUNT(*) OVER (PARTITION BY tiv_2015) AS tiv2015_cnt,
             COUNT(*) OVER (PARTITION BY lat, lon) AS latlon_cnt
      FROM Insurance) t
WHERE t.tiv2015_cnt > 1
  AND t.latlon_cnt = 1;