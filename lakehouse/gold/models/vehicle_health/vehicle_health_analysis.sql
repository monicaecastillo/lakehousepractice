{% set nessie_branch = var('nessie_branch', 'main') %}

SELECT
    vh.VehicleID,
    vh.ManufacturingYear,
    vh.Model,
    COUNT(JSON_LENGTH(vh.Alerts)) as total_alerts,
    JSON_EXTRACT_SCALAR(MAX(vh.Alerts, '$.Date')) as latest_alert_date
FROM {{ source('silver', 'vehicle_health_logs') }} AT branch {{ nessie_branch }} vh
GROUP BY vh.VehicleID, vh.ManufacturingYear, vh.Model