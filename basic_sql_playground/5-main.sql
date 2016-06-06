SELECT DISTINCT last_name FROM Person LEFT JOIN TVShowPerson
on Person.id = TVShowPerson.person_id
LEFT JOIN TVShow
on TVShowPerson.tvshow_id = TVShow.id
WHERE name = 'Game of Thrones'
ORDER BY last_name ASC;

SELECT count(age) FROM PERSON where age > 30;

SELECT Person.id, first_name, last_name, age, color, name
FROM PERSON LEFT JOIN EyesColor on Person.id = EyesColor.person_id
LEFT JOIN TVShowPerson on Person.id = TVShowPerson.person_id
LEFT JOIN TVShow on TVShowPerson.tvshow_id = TVShow.id;

SELECT sum(age) FROM Person;
