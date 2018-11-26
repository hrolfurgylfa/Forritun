DROP DATABASE IF EXISTS 2109013290_company;
CREATE DATABASE 2109013290_company;
USE 2109013290_company;

create table dept
(
  dept_no int not null,
  dept_name varchar(100) not null,
  dept_location varchar(100) not null,
  primary key (dept_no)
);
create table employee 
(
  emp_id int not null,
  emp_name varchar(100) not null,
  mgr_emp_id int,
  dept_no int not null,
  salary  double  not null,
  primary key (emp_id),
  key employee_mgr_emp_id (mgr_emp_id),
  foreign key fk_employee_dept_dept_no (dept_no) references dept (dept_no) on delete no action on update no action
);

insert into dept values 
(1, 'Dept-1', 'Chicago'), 
(2, 'Dept-2', 'London'),
(3, 'Dept-3', 'Reykjavik'),
(4, 'Dept-4', 'Rabat');

insert into employee values 
(1, 'Clark Mgr', null, 1, 450000),
(2, 'Cameron Emp', 2, 1, 300000),
(3, 'Charlie Emp', 3, 1, 500000),
(4, 'Layton Emp', null, 2, 250000),
(5, 'Linda Emp', null, 2, 370000),
(6, 'Mikel Mor', null, 3, 290000),
(7, 'Mic Coleman', null, 3, 400000),
(8, 'Doud Valantino', null, 3, 300000);
