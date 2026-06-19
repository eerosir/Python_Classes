-- - Find all actors with first name "PENELOPE".
USE sakila;
SELECT * FROM actor 
WHERE first_name = 'PENELOPE';

-- - Find all films with rating = 'PG'.
SELECT * FROM film 
WHERE rating = 'PG';

-- - Find all films longer than 120 minutes.
SELECT * FROM film 
WHERE length > 120;

-- - Find all customers with active = 1.
SELECT * FROM customer 
WHERE active = 1;

-- - Find all customers from the store with store_id = 1.
SELECT * FROM customer 
WHERE store_id = 1;

-- - Show all films ordered by length from shortest to longest.
SELECT * FROM film 
ORDER BY length ASC;

-- - Show all films ordered by rental_rate from highest to lowest.
SELECT * FROM film 
ORDER BY rental_rate DESC;

-- - Show 5 longest films.
SELECT * FROM film 
ORDER BY length DESC LIMIT 5;

-- - Show 10 cheapest films by rental price.
SELECT * FROM film 
ORDER BY rental_rate ASC LIMIT 10;

-- - Show all different ratings from the film table.
SELECT DISTINCT rating FROM film;

-- - Show all different release years from the film table.
SELECT DISTINCT release_year FROM film;

-- - Show all different customer last names.
SELECT DISTINCT last_name FROM customer;

-- - Count how many actors exist.
SELECT COUNT(actor_ID) FROM film_actor;

-- - Count how many films exist.
SELECT COUNT(film_ID) FROM film;

-- - Find the average film length.
SELECT AVG(length) FROM film;

-- - Find the maximum rental rate.
SELECT MAX(rental_rate) FROM film;

-- - Find the minimum replacement cost.
SELECT MIN(replacement_cost) FROM film;

-- - Find all films that contain the word "LOVE" in the title.
SELECT * FROM film 
WHERE title LIKE '%LOVE%';

-- - Find all actors whose last name starts with "S".
SELECT first_name, last_name FROM actor 
WHERE last_name LIKE 'S%';

-- - Find all customers whose email contains "gmail".
SELECT * FROM customer 
WHERE email like '%gmail%';

-- - Find all films that end with "MAN".
SELECT * FROM film 
WHERE title LIKE '%MAN';
