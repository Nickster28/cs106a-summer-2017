# General course information
COURSE_NUMBER = "CS 106A"
COURSE_NAME = "Programming Methodology"
COURSE_TITLE = COURSE_NUMBER + ": " + COURSE_NAME
CS198_NUMBER = 1 # B = 2, X = 3

# General quarter information
QUARTER_NUMBER = 1178
QUARTER_NAME = "Summer"
QUARTER_YEAR = "2017"
QUARTER_FULL_NAME = QUARTER_NAME + " " + QUARTER_YEAR
QUARTER_OVER = True  # Set to True to add banner at the top redirecting to newer version of webpage

# Lecture information (displayed at top of home page)
LECTURE_DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday"]
LECTURE_TIME = "11:30AM-12:20PM PST"
LECTURE_LOCATION = "NVIDIA Auditorium"
LECTURE_LOCATION_LINK = "https://www.google.com/maps/place/NVIDIA+Auditorium/@37.4277284,-122.1763905,17z/data=!3m1!4b1!4m5!3m4!1s0x808fbb2ac97723cb:0xa6e8fc1a7a5f2c29!8m2!3d37.4277284!4d-122.1741965"
LECTURE_FEEDBACK_LINK = "https://goo.gl/forms/viRkXgYxDRq0Uorm2" # Length > 0

# Course staff (displayed in left sidebar and on staff page)
STAFF_INFO = [
	{
		"POSITION": "Instructor",
		"NAME": "Nick Troccoli",
		"IMAGE": "troccoli.jpg",
		"EMAIL": "troccoli@stanford.edu",
		"OFFICE_HOURS_LOCATION": "Gates B02",
		"OFFICE_HOURS_DATETIME": "Wed. + Thurs. 2-4PM",
		"DESCRIPTION": "The instructor teaches lectures and manages the overall course. Contact the instructor if you have a question that cannot be answered by your section leader; the SLs are your primary email contact for all questions about homework or other course issues.  Please also cc your section leader and/or Head TA.  In addition to at his office hours, please feel free to ask Nick questions before/after any lecture."
	},
	{
		"POSITION": "Head TA",
		"NAME": "Rishi Bedi",
		"IMAGE": "rbedi.jpg",
		"EMAIL": "rbedi@stanford.edu",
		"OFFICE_HOURS_LOCATION": "Gates B02",
		"OFFICE_HOURS_DATETIME": "Tues. + Thurs. 9-11AM",
		"DESCRIPTION": "The Head TA manages the section leaders and also oversees important course activities such as grading and section problems. Contact the Head TA if you need a regrade on an assignment, or have a question that cannot be answered by your section leader; the SLs are your primary email contact for all questions about homework or other course issues.  Please also cc your section leader and/or Instructor."
	}
]

# Note: section leader names MUST be formatted "NAME (SUNET)" as the image for a given Section Leader is assumed to be SUNET.jpg.
SECTION_LEADERS = [
	"Aleksander Dash (adash)",
	"Canyon Robins (crobins)",
	"Conner Smith (csmith95)",
	"Emily Ling (eling8)",
	"Farah Uraizee (farah)",
	"Garrick Fernandez (gfaerr)",
	"Gus Torres da Silva (gdasilva)",
	"Guy Blanc (gblanc)",
	"Jared Bitz (jbitz)",
	"Jestin Ma (jestinm)",
	"Kate Rydberg (rydbergk)",
	"Katherine Erdman (kerdman)",
	"Keanu Spies (keanus)",
	"Michael Hazard (cmhazard)",
	"Mirae Parker (miraep8)",
	"Nick Negrete (nnegrete)",
	"Nolan Handali (nolanh)",
	"Pras Ramakrishnan (pras1712)",
	"Regina Nguyen (renguyen)",
	"Tobin Bell (trfbell)",
	"Tyler Yep (tyep)",
	"Wil Kautz (wkautz)"
]

# SCPD (listed in left sidebar)
SCPD_OFFICE_HOURS = [
	"Sun 5:30-7PM PST",
	"Tues 9-11AM PST",
	"Tues 8-9PM PST",
	"Wed 8:30-10PM PST",
	"Thurs 4-5PM PST",
	"Thurs 8:30-9:30PM PST"
]
SCPD_OFFICE_HOURS_LINK = "http://www.queuestatus.com/queues/122"
SCPD_OFFICE_HOURS_DESCRIPTION = "SCPD students can sign up for help at the times above (free QueueStatus account required)."

# Exams (displayed in left sidebar, but locations and review session are only displayed on exam subpages)
MIDTERM = {
	"DATE": "Monday, July 24",
	"TIME": "7-9PM PST",
	"LOCATIONS": [ 	# A list of objects containing TITLE, LOCATION, MAP_LINK
		{
			"TITLE": "Exam",
			"LOCATION": "Hewlett 200",
			"MAP_LINK": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3168.345197243158!2d-122.1750263848679!3d37.42894923975373!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x808fbb2ae177cc91%3A0x5351ffed56456da8!2sWilliam+R.+Hewlett+Teaching+Center%2C+370+Serra+Mall%2C+Stanford%2C+CA+94305!5e0!3m2!1sen!2sus!4v1500400060838"
		}
	],
	"REVIEW_SESSION": {
		"DATE": "Friday, July 21",
		"TIME": "3:30-4:50PM PST",
		"LOCATION": "Gates B03 (basement)",
		"MAP_LINK": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3168.2942783500653!2d-122.17568493444799!3d37.4301523298236!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x808fbb2b3f50f727%3A0xfd9cc3200ee97fda!2sGates+Computer+Science%2C+353+Serra+Mall%2C+Stanford%2C+CA+94305!5e0!3m2!1sen!2sus!4v1500425297459"
	}
}

FINAL_EXAM = {
	"DATE": "Friday, August 18",
	"TIME": "12:15-3:15PM PST",
	"LOCATIONS": [	# A list of objects containing TITLE, LOCATION, MAP_LINK
		{
			"TITLE": "Last Names A-O",
			"LOCATION": "NVIDIA Auditorium",
			"MAP_LINK": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3168.396866793715!2d-122.17639054916224!3d37.42772837972516!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x808fbb2ac97723cb%3A0xa6e8fc1a7a5f2c29!2sNVIDIA+Auditorium!5e0!3m2!1sen!2sus!4v1502919715852"
		},
		{
			"TITLE": "Last Names P-Z",
			"LOCATION": "Gates B01 (Basement)",
			"MAP_LINK": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3168.2942783500653!2d-122.17568493444799!3d37.4301523298236!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x808fbb2b3f50f727%3A0xfd9cc3200ee97fda!2sGates+Computer+Science%2C+353+Serra+Mall%2C+Stanford%2C+CA+94305!5e0!3m2!1sen!2sus!4v1500425297459"
		}
	],
	"REVIEW_SESSION": {
		"DATE": "Mon/Tue, August 14-15",
		"TIME": "11:30AM-12:20PM PST",
		"LOCATION": "NVIDIA Auditorium",
		"MAP_LINK": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3168.396866793715!2d-122.17639054916224!3d37.42772837972516!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x808fbb2ac97723cb%3A0xa6e8fc1a7a5f2c29!2sNVIDIA+Auditorium!5e0!3m2!1sen!2sus!4v1502919715852"
	}
}

# Assignments (displayed in Assignments dropdown at the top)
STYLE_GUIDE = True
PAIR_PROGRAMMING = True
ASSIGNMENTS = [
	{
		"NAME": "Karel the Robot",
		"LINK": "karel.html"
	},
	{
		"NAME": "Intro to Java",
		"LINK": "introToJava.html"
	},
	{
		"NAME": "Hangman",
		"LINK": "hangman.html"
	},
	{
		"NAME": "Artistry and Breakout",
		"LINK": "breakout.html"
	},
	{
		"NAME": "ImageShop",
		"LINK": "imageshop.html"
	},
	{
		"NAME": "NameSurfer",
		"LINK": "namesurfer.html"
	}
]
ASSIGNMENT_DUE_TIME = "11AM PST"

# Software
SOFTWARE = "Eclipse"
SOFTWARE_ICON = "eclipse-icon.png"
SOFTWARE_LINK = "eclipse"

# Stanford Library
LIBRARY_DOCS_LINK = "http://stanford.edu/~stepp/acmdoc/"

BLANK_PROJECTS = [
	{
		"NAME": "Blank Karel Project",
		"LINK": "/resources/BlankKarelProject.zip"
	},
	{
		"NAME": "Blank Java Project",
		"LINK": "/resources/BlankJavaProject.zip"
	}
]
