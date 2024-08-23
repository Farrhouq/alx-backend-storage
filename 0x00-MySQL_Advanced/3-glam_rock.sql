-- Lists all bands with glam rock as their style
SELECT band_name, COALESCE(split - formed, 2022 - formed, 0) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
