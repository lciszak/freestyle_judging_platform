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



drop table if exists event_run_judge;
CREATE TABLE event_run_judge(
	event_id integer not null,
	judge_name VARCHAR(255) not null COMMENT 'Judge',	
	rider_name VARCHAR(255) not null COMMENT 'Rider',	
	event_round VARCHAR(255) not null COMMENT 'Round',	
	run NUMERIC(1) not null COMMENT 'Run',	
	trick_points DECIMAL(5,2) not null COMMENT 'Trick points total',	
	bails_minor INTEGER not null COMMENT 'Minor bails',	
	bails_medium INTEGER not null COMMENT 'Medium Bails',	
	bails_severe INTEGER not null COMMENT 'Severe bails',	
	footwork_difficulty INTEGER not null COMMENT 'Difficulty',	
	footwork_variety INTEGER not null COMMENT 'Variety',	
	footwork_speed INTEGER not null COMMENT 'Speed',	
	footwork_smooothness INTEGER  not null COMMENT 'Smoothness',	
	variety_groups_covered INTEGER not null COMMENT 'All trick groups covered',	
	variety_uniqueness INTEGER not null COMMENT 'Tricks were unique',	
	variety_rare INTEGER not null COMMENT 'Rare or new tricks, non-standard trick combos',	
	music_fit INTEGER not null COMMENT 'The music fit the run',	
	music_synchronized integer not null COMMENT 'The run synchronized with the music',	
	run_planned INTEGER not null COMMENT 'The run seemed planned and rehearsed',	
	run_smooth INTEGER not null COMMENT 'The tricks flowed smoothly into one another',	
	run_tricks_clean INTEGER not null COMMENT 'All tricks were landed cleanly and performed technically correct',	
	run_tricks_confident INTEGER not null COMMENT 'All tricked were performed with confidence and seemed effortless',	
	run_personal_touch INTEGER not null COMMENT 'Tricks had the personal touch of the rider',	
	login VARCHAR(255) not null  COMMENT 'login',	
	insert_date TIMESTAMP  not null COMMENT 'insert date',	
	update_date TIMESTAMP not null COMMENT 'update date'
);

alter table event_run_judge add constraint primary key event_run_judge_pk(event_id, judge_name,rider_name,event_round,run);

alter table event_run_judge add constraint event_rider_fk foreign key(rider_name,event_id) references event_rider(rider_name,event_id);