create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";

create table dogs as
  select "abraham" as name, "long" as fur, 26 as height union
  select "barack"         , "short"      , 52           union
  select "clinton"        , "long"       , 47           union
  select "delano"         , "long"       , 46           union
  select "eisenhower"     , "short"      , 35           union
  select "fillmore"       , "curly"      , 32           union
  select "grover"         , "short"      , 28           union
  select "herbert"        , "curly"      , 31;

create table sizes as
  select "toy" as size, 24 as min, 28 as max union
  select "mini",        28,        35        union
  select "medium",      35,        45        union
  select "standard",    45,        60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
create table size_of_dogs as
  select dog.name as name, b.size as size
  from dogs as dog, sizes as b
  where dog.height <= b.max and dog.height > b.min;

-- All dogs with parents ordered by decreasing height of their parent
create table by_height as
  select dog.name
  from dogs as dog, parents as storage, dogs as data
  where dog.name = storage.child and data.name = storage.parent
  order by - data.height;

-- Sentences about siblings that are the same size
create table sentences as
  with compare(name, sibling) as
    (
    select a.child, b.child
    from parents as a, parents as b
    where a.parent = b.parent and a.child < b.child
    order by a.child
    )
  select dog.name || " and " || dog.sibling || " are " || marker.size || " siblings"
  from compare as dog, size_of_dogs as marker, size_of_dogs as second
  where marker.name = dog.name and dog.sibling = second.name and second.size = marker.size
  order by dog.name;

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
create table stacks as
  --with stackings(dawg, num, prev_height) as
    --(
    ---select dog.name, 1, max(dog.height) from dogs as dog union
    ----union
  --- )
  select a.name || ", " || b.name || ", " || c.name || ", " || d.name, a.height + b.height + c.height + d.height as heights
  from dogs as a, dogs as b, dogs as c, dogs as d
  where a.height + b.height + c.height + d.height > 170 and a.height < b.height and b.height < c.height and c.height < d.height
  order by heights;

-- non_parents is an optional, but recommended question
-- All non-parent relations ordered by height difference
--create table non_parents as
  --select "REPLACE THIS LINE WITH YOUR SOLUTION";

create table ints as
    with i(n) as (
        select 1 union
        select n+1 from i limit 100
    )
    select n from i;

create table divisors as
    select first.n*second.n as product, count(first.n*second.n) as coun from ints as first, ints as second group by first.n*second.n limit 100;

create table primes as
    select a.product from divisors as a where a.coun == 2;
