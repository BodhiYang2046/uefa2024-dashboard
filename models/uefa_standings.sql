{{ config(materialized='table') }}

SELECT
    group,
    team,
    played,
    won,
    drawn,
    lost,
    points,
    scraped_at,
    ROW_NUMBER() OVER (PARTITION BY group ORDER BY points DESC, won DESC) as rank
FROM {{ source('uefa_data', 'standings') }}
WHERE DATE(scraped_at) = CURRENT_DATE()