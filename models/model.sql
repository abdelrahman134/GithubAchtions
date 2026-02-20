WITH source_data AS (
    SELECT 1 AS user_id, 'active' AS status
    UNION ALL
    SELECT 2 AS user_id, 'inactive' AS status
)

SELECT * FROM source_data
WHERE status = 'active'