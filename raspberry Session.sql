SELECT horses.name
FROM horses
JOIN race_horses
    ON race_horses.horse_id = horses.id
JOIN races
    ON race_horses.race_id = races.id
WHERE races.id = 1