
/*Technical Interview
SQL Prompt:
A simple fruit stand store maintains data about its’ fruit sales.
One table (Fruit_Fact) holds this information -the transaction price, the fruit sold, the quantity sold, a transaction number and the date.  
Ex.) Transaction 1 had 2 Apples sold on July 1, 2012. For $2.00.
E.g.) Fruit_Fact, an example row
Trans_Num
Fruit
Quantity
Date
Cum_Price
0000000001
Apple
2
20150603
2.00

As you can see, a row can contains only one type of fruit, but can hold multiple sales of that fruit for a given transaction. 
Exercises in SQL -
1)  What are all the different fruits we have ever sold?
2)  What are all the different fruits sold today?
3)  What fruits were sold today, that were not sold yesterday? Can you do this with at least three different methods?
4)  How many of each type of fruit did we sell today?
5)  How many of each type of fruit was sold during each month in 2015? What are all the different fruits sold in 2015 that sold at least 50 (Quantity) in that month?

*/

# schema 
/*
create table Fruit_Fact (
  Trans_Num int,
  Fruit varchar(255), 
  quantity int,
  Order_date date,
  Cum_Price float
);

insert into Fruit_Fact values ( 001, 'Apple', 2, 20180531, 2.00);
insert into Fruit_Fact values ( 002, 'Bannana', 2, 20180531, 2.25);
insert into Fruit_Fact values ( 003, 'Strawberry', 2, 20180530, 3.00);
insert into Fruit_Fact values ( 004, 'Apple', 4, 20180530, 2.00);
insert into Fruit_Fact values ( 005, 'Apple', 5, 20180530, 2.00);
insert into Fruit_Fact values ( 006, 'Strawberry', 2, 20150603, 3.00);
insert into Fruit_Fact values ( 007, 'pear', 1, 20180531, 1.00);
insert into Fruit_Fact values ( 008, 'sugarcane', 7, 20180530, 2.25);
insert into Fruit_Fact values ( 009, 'orange', 6, 20180531, 5.00);
insert into Fruit_Fact values ( 010, 'orange', 2, 20180531, 5.00);
insert into Fruit_Fact values ( 012, 'Apple', 8, 20180531, 2.00);
insert into Fruit_Fact values ( 013, 'mandaris', 8, 20180531, 2.00);
insert into Fruit_Fact values ( 014, 'mandaris', 8, 20150128, 2.00);
insert into Fruit_Fact values ( 015, 'mandaris', 8, 20150128, 2.00);

insert into Fruit_Fact values ( 016, 'apple', 8, 20150314, 2.00);
insert into Fruit_Fact values ( 017, 'apple', 8, 20150315, 2.00);


insert into Fruit_Fact values ( 018, 'orange', 8, 20150514, 2.00);
insert into Fruit_Fact values ( 019, 'orange', 8, 20150615, 2.00);
*/



# 1. What are all the different fruits we have ever sold?

SELECT  DISTINCT Fruit
FROM Fruit_Fact
WHERE Fruit is not null


# 2. What are all the different fruits sold today?

SELECT distinct Fruit 
FROM Fruit_Fact
WHERE order_date=date_format(now(),'%Y%m%d') and Fruit is not null 


#3. 

#
select distinct Fruit
from Fruit_Fact 
where Order_date = CURDATE() and Fruit not in 
( 
 select distinct Fruit
  from Fruit_Fact 
  where Order_date = SUBDATE(CURDATE(),1) and Fruit is not NULL
) 

#
select distinct Fruit from Fruit_Fact where Order_date =current_date()
minus 
select distinct Fruit from Fruit_Fact where Order_date = SUBDATE(current_date(), 1) 

Outer-join select items from today t left join yesterday y where y.item is null.

# 4. How many of each type of fruit did we sell today?

SELECT Fruit, sum(quantity), Order_date 
FROM Fruit_Fact 
WHERE  Order_date = date_format(now(),'%Y%m%d')
group by Fruit 

# 5. How many of each type of fruit was sold during each month in 2015? What are all the different fruits sold in 2015 that sold at least 50 (Quantity) in that month?

SELECT FRUIT, extract(month from order_date), sum(quantity) as total_quantity
FROM Fruit_Fact
where extract(year from order_date)=2015
group by extract(month from order_date)
having total_quantity> 50



# rankig by quantity sold 

 select Fruit, total, @cur_rank := @cur_rank +1 as arank from (select Fruit, sum(quantity) as total
  from Fruit_Facts
  group by Fruit
  order by sum(quantity) desc)t1, (select @cur_rank :=0) as r
