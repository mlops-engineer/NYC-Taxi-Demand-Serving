base_query = """
    WITH base_data AS 
    (
      SELECT nyc_taxi.*, gis.* EXCEPT (zip_code_geom)
      FROM (
        SELECT *
        FROM `bigquery-public-data.new_york_taxi_trips.tlc_yellow_trips_2015`
        WHERE 
            EXTRACT(MONTH from pickup_datetime) = 1
            and pickup_latitude  <= 90 and pickup_latitude >= -90
        ) AS nyc_taxi
      JOIN (
        SELECT zip_code, state_code, state_name, city, county, zip_code_geom
        FROM `bigquery-public-data.geo_us_boundaries.zip_codes`
        WHERE state_code='NY'
        ) AS gis 
      ON ST_CONTAINS(zip_code_geom, st_geogpoint(pickup_longitude, pickup_latitude))
    ), distinct_datetime AS (
      SELECT distinct DATETIME_TRUNC(pickup_datetime, hour) as pickup_hour
      FROM base_data
    ), distinct_zip_code AS (
      SELECT distinct zip_code
      FROM base_data
    ), zip_code_datetime_join AS (
      SELECT
        *,
        EXTRACT(MONTH FROM pickup_hour) AS month,
        EXTRACT(DAY FROM pickup_hour) AS day,
        CAST(format_datetime('%u', pickup_hour) AS INT64) -1 AS weekday,
        EXTRACT(HOUR FROM pickup_hour) AS hour,
        CASE WHEN CAST(FORMAT_DATETIME('%u', pickup_hour) AS INT64) IN (6, 7) THEN 1 ELSE 0 END AS is_weekend
      FROM distinct_zip_code  
      CROSS JOIN distinct_datetime
    ), agg_data AS (
      SELECT 
          zip_code,
          DATETIME_TRUNC(pickup_datetime, hour) as pickup_hour,
          COUNT(*) AS cnt
      FROM base_data 
      GROUP BY zip_code, pickup_hour
    ), join_output AS (
      select 
        zip_code_datetime.*, 
        IFNULL(agg_data.cnt, 0) AS cnt
      from zip_code_datetime_join as zip_code_datetime
      LEFT JOIN agg_data
      ON zip_code_datetime.zip_code = agg_data.zip_code and zip_code_datetime.pickup_hour = agg_data.pickup_hour
    )
    SELECT
      *,
      LAG(cnt, 1) OVER(PARTITION BY zip_code ORDER BY pickup_hour) AS lag_1h_cnt,
      LAG(cnt, 24) OVER(PARTITION BY zip_code ORDER BY pickup_hour) AS lag_1d_cnt,
      LAG(cnt, 168) OVER(PARTITION BY zip_code ORDER BY pickup_hour) AS lag_7d_cnt,
      LAG(cnt, 336) OVER(PARTITION BY zip_code ORDER BY pickup_hour) AS lag_14d_cnt,
      ROUND(AVG(cnt) OVER(PARTITION BY zip_code ORDER BY pickup_hour ROWS BETWEEN 168 PRECEDING AND 1 PRECEDING), 2) AS avg_14d_cnt,
      ROUND(AVG(cnt) OVER(PARTITION BY zip_code ORDER BY pickup_hour ROWS BETWEEN 336 PRECEDING AND 1 PRECEDING), 2) AS avg_21d_cnt,
      CAST(STDDEV(cnt) OVER(PARTITION BY zip_code ORDER BY pickup_hour ROWS BETWEEN 168 PRECEDING AND 1 PRECEDING) AS INT64) AS std_14d_cnt,
      CAST(STDDEV(cnt) OVER(PARTITION BY zip_code ORDER BY pickup_hour ROWS BETWEEN 336 PRECEDING AND 1 PRECEDING) AS INT64) AS std_21d_cnt
    FROM join_output
    ORDER BY zip_code, pickup_hour
"""