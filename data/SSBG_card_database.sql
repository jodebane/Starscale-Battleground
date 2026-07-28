DROP database SSBG_cards;
CREATE database SSBG_cards;

CREATE TABLE SSBG_cards.cardslist(
card_id int PRIMARY KEY NOT NULL,
card_name varchar(255) NOT NULL,
card_type varchar(255) NOT NULL,
card_subtype varchar(255),
card_other_subtype varchar(255),
card_tags varchar(300),
card_ep_cost int,
card_mission_cost int,
card_attack_power int,
card_hit_points int,
card_rules_text varchar(600) NOT NULL

);

