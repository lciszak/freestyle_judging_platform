drop table if exists event_rider;
CREATE TABLE event_rider(
	rider_name VARCHAR(255) not null,
	event_id INT not null,
	division VARCHAR(255) not null
);


alter table event_rider add constraint primary key event_rider_pk (rider_name,event_id, division);
alter table event_rider add constraint event_rider_unq unique(rider_name,event_id);

drop table if exists event;
create table event(
	event_id INT not null,
	event_name VARCHAR(255) not null
);
alter table event add constraint primary key event_pk (event_id);




	