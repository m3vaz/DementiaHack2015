# DementiaHack2015

## Background

Dementia is a growing concern, especially in parts of the world where populations are aging. The focus of the hackathon is building solutions to help caregivers of dementia manage that growing population and to help those living with dementia carry on day-to-day life. The specific problem we chose to address was tracking patients while in healthcare institutions which fell under ["Institutional Caregivers" challenge set](http://hackernest.com/dementiahack/#challenge).

The solutions currently in the space rely on three basic mechanisms of location, WiFi, Infrared (IR), Ultrasound. Each has its own limitations, which we sought to address by instead relying on bluetooth. WiFi has the general benefit of not requiring infrastructure set up, since its increasingly common for hospitals to have their own internal wireless network, but the downside is (by one manufacturer's own admission) a margin of error on the vertical of 10 m, potentially placing patients on completely different floors. IR and Ultrasonic systems require setting up separate infrastructure, but has the benefit of stopping at a wall. For IR, zones are defined with sensors and the resolution with IR is at the zone level. Ultrasonic systems also work with zones, with devices emitting chirps, but could potentially have cross-talk interference between devices and requires purpose-built devices.

## Idea

Using Bluetooth addresses several of these issues. While still attenuated through floors and ceilings, it has some penetration through walls allowing trilateration reference points to be placed in the hallway to cover multiple patient rooms. These reference points can be off-the-shelf components, specifically iBeacons, driving down the cost and allowing any smartphone to verify the status of those points. 

The prototype uses 3 LightBlue Beans to act as reference points and a Raspberry Pi attached to the person. The Pi determines its relative strength to the closest set of reference points and uploads it for calculation on a central server. The result of that calculation is then stored and can be called up on a web page. [http://rov.mybluemix.net/index.html] (http://rov.mybluemix.net/index.html) has a mockup of the web interface, with sample data. The tracking dot turns red when the system has lost track of the subject, showing the last known position. 

## Contributions

m3vaz: Flask (Python, web micro-framework), SQLAlchemy (Python, interface for RDBMS), DB2

KevinLuong96: Raspberry PI, Bash, Bluetooth Interfacing (BlueZ), Wifi Interfacing

ilylambb/EmilyLam96: Market Research, Design, LightBlue Beans

celelista: Front-end Dev Elements(JQuery, AJAX, HTML, CSS)


