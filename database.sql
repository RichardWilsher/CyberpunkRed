-- MySQL script to create the tables required for the CPR programs
-- No data is included
-- not all fields are actively used at this time
CREATE TABLE cpr.npcs (
id int,
name varchar(45),
description varchar(4000)
);
ALTER TABLE cpr.npcs CHANGE COLUMN id id INT NOT NULL AUTO_INCREMENT , ADD PRIMARY KEY (id);
CREATE TABLE cpr.roles (
id int,
ability varchar(20),
name varchar(15)
);
ALTER TABLE cpr.roles CHANGE COLUMN id id INT NOT NULL AUTO_INCREMENT , ADD PRIMARY KEY (id);
CREATE TABLE cpr.skill_category (
id int,
name varchar(45)
);
ALTER TABLE cpr.skill_category CHANGE COLUMN id id INT NOT NULL AUTO_INCREMENT , ADD PRIMARY KEY (id);
CREATE TABLE cpr.skills (
id int,
name varchar(45),
stat int,
difficult varchar(1),
category int,
modified varchar(1),
description varchar(4000),
example varchar(4000)
);
ALTER TABLE cpr.skills CHANGE COLUMN id id INT NOT NULL AUTO_INCREMENT , ADD PRIMARY KEY (id);
CREATE TABLE cpr.stats (
id int,
name varchar(45),
modified varchar(1)
);
ALTER TABLE cpr.stats CHANGE COLUMN id id INT NOT NULL AUTO_INCREMENT , ADD PRIMARY KEY (id);
CREATE TABLE cpr.mooks (
id int,
name varchar(45),
type int,
generic varchar(1),
headsp int,
bodysp int,
location varchar(45),
rep int
);
ALTER TABLE cpr.mooks CHANGE COLUMN id id INT NOT NULL AUTO_INCREMENT , ADD PRIMARY KEY (id);
CREATE TABLE cpr.mook_weapon (
id int,
mookid int,
weaponid int,
qualityid int
);
ALTER TABLE cpr.mook_weapon CHANGE COLUMN id id INT NOT NULL AUTO_INCREMENT , ADD PRIMARY KEY (id);
CREATE TABLE cpr.mook_stat (
id int,
mookid int,
statid int,
value varchar(8)
);
ALTER TABLE cpr.mook_stat CHANGE COLUMN id id INT NOT NULL AUTO_INCREMENT , ADD PRIMARY KEY (id);
CREATE TABLE cpr.mook_skill (
id int,
mookid int,
skillid int,
value varchar(8),
notes varchar(20)
);
ALTER TABLE cpr.mook_skill CHANGE COLUMN id id INT NOT NULL AUTO_INCREMENT , ADD PRIMARY KEY (id);
CREATE TABLE cpr.mook_role (
id int,
mookid int,
roleid int,
value varchar(2),
notes varchar(45)
);
ALTER TABLE cpr.mook_role CHANGE COLUMN id id INT NOT NULL AUTO_INCREMENT , ADD PRIMARY KEY (id);
CREATE TABLE cpr.mook_equipment (
id int,
mookid int,
equipmentid int,
quantity varchar(8),
subinformation varchar(60)
);
ALTER TABLE cpr.mook_equipment CHANGE COLUMN id id INT NOT NULL AUTO_INCREMENT , ADD PRIMARY KEY (id);
CREATE TABLE cpr.mook_cyberwear (
id int,
mookid int,
cyberwearid int,
quantity varchar(8),
notes varchar(80)
);
ALTER TABLE cpr.mook_cyberwear CHANGE COLUMN id id INT NOT NULL AUTO_INCREMENT , ADD PRIMARY KEY (id);
CREATE TABLE cpr.type (
id int,
name varchar(45)
);
ALTER TABLE cpr.type CHANGE COLUMN id id INT NOT NULL AUTO_INCREMENT , ADD PRIMARY KEY (id);
CREATE TABLE cpr.equipment_category (
id int,
name varchar(45)
);
ALTER TABLE cpr.equipment_category CHANGE COLUMN id id INT NOT NULL AUTO_INCREMENT , ADD PRIMARY KEY (id);
CREATE TABLE cpr.equipment (
id int,
categoryid int,
name varchar(45)
);
ALTER TABLE cpr.equipment CHANGE COLUMN id id INT NOT NULL AUTO_INCREMENT , ADD PRIMARY KEY (id);
CREATE TABLE cpr.cyberwear_category (
id int,
name varchar(45)
);
ALTER TABLE cpr.cyberwear_category CHANGE COLUMN id id INT NOT NULL AUTO_INCREMENT , ADD PRIMARY KEY (id);
CREATE TABLE cpr.cyberwear (
id int,
categoryid int,
name varchar(45)
);
ALTER TABLE cpr.cyberwear CHANGE COLUMN id id INT NOT NULL AUTO_INCREMENT , ADD PRIMARY KEY (id);
CREATE TABLE cpr.armour (
id int,
name varchar(45),
sp varchar(2),
modifier varchar(2)
);
ALTER TABLE cpr.armour CHANGE COLUMN id id INT NOT NULL AUTO_INCREMENT , ADD PRIMARY KEY (id);
CREATE TABLE cpr.weapons (
id int,
name varchar(45),
dice varchar(4),
rof varchar(1)
);
ALTER TABLE cpr.weapons CHANGE COLUMN id id INT NOT NULL AUTO_INCREMENT , ADD PRIMARY KEY (id);
CREATE TABLE cpr.weapon_quality (
id int,
name varchar(10)
);
ALTER TABLE cpr.weapon_quality CHANGE COLUMN id id INT NOT NULL AUTO_INCREMENT , ADD PRIMARY KEY (id);

