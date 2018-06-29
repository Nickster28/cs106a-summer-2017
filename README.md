# CS106A Summer 2017 Website

This is a pre-compiled, static website for the Summer 2017 offering of
Stanford's CS106A introductory programming course.  This repository is structured as
follows:

```
bottle/ - the source files for Bottle, the library used to compile templates
markdown/ - the source files for Python Markdown, the library used to compile announcements
templates/ - the uncompiled Bottle templates (.html represent actual pages,
.ptl represent 'partials' that are used within other files)
WWW/ - the output folder containing compiled pages and other static resources
compile.py - the template compilation script
announcements/ - Markdown files for course announcements
```

(Note: for hosting on Stanford servers, it's easiest to symlink from the course's WWW/ folder to the above WWW/ folder)

## Editing
Within `templates`, there are subfolders for exam pages, assignment pages, and
subparts of various pages.  Here are the relevant files for various tasks you
may want to do:

- **Initial setup and customization:** see `courseInfo.py` for various constants you must specify containing information about your course offering.  These constants define content displayed on various pages; info about these constants is documented within the file.

- **Posting announcements:** announcements are written using [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).  The `announcements` folder contains all announcement files (1 file per announcement) - to add a new announcement, create a new Markdown file in that directory.  The filename should be the timestamp after which the announcement is visible, in the format `YYYYMMDDHHMM`.  The file format is specified as follows:
```
TITLE HERE
-
MARKDOWN HERE
```
See the `announcements` directory for several examples.  Note that the second line of the file is always ignored (it is considered a separator between the announcement title and its markdown content).  Note that, if needed, you may include HTML in your Markdown.  When the website is compiled, all the announcement markdown files are rendered reverse-chronologically within `index.html`.

- **Adding handouts (excluding section materials):** add the handout to `WWW/handouts/`, with the
naming style `NUMBER-DASHED_NAME.extension`.  E.g. `1-General-Information.pdf`.
Any handouts in this folder will be automatically listed in the "Handouts"
dropdown with the format `NUMBER - SEPARATED_NAME`.
E.g. `1 - General Information`.

- **Adding section materials:** make a new folder of that section number in `WWW/section/` and add
materials according to the following naming conventions:
	- `Section[NUM].pdf` - handout
	- `Section[NUM].zip` - solution code
	- `Section[NUM]-Solutions.pdf` - solution handout

For instance, for section 6 you would add `Section6.pdf`, `Section6.zip` and `Section6-Solutions.pdf`.

You must also add an `info.json` file to the directory that looks as follows:
```
{
	"solutionsDate": "2017063017"
}
```
This timestamp should be when the solution materials will be made available (in the format YYYYMMDDHH).
The solution handout and code will be visible in the Section dropdown from that
date onwards.  The section handout will be visible as soon as it is added to the
repository.

- **Add a new assignment:** add the assignment page template to
`templates/assignments/` and update
`templates/navbar/assignmentsDropdownList.html` to list the new
assignment.

- **Change the lecture schedule:** the lecture calendar and the lectures
dropdown are both dynamically generated from the same JSON file,
`schedule.json`.  This JSON file has the following format:

```
{
	"days": ...,
	"weeks": ...
}
```

`days` maps to an array of strings naming each day on which there is lecture.
This is displayed as the header row in the schedule table.  E.g.

```
{
	"days": ["Monday", "Tuesday", "Wednesday", "Thursday"],
	"weeks": ...
}
```

`weeks` is a list containing data for each week.  Each week is itself a list of
objects representing each lecture that week.  Note that each week's length must
match the length of the `days` array.  (The reason for this is the added flexibility
of having assignments due on non-lecture days.)  These lecture objects have the following
keys (whose values are all strings):
```
date (REQUIRED): the date string (e.g. "June 26") to display
title (OPTIONAL): the name of the lecture (or event)
type (OPTIONAL): "HOLIDAY" if a holiday, or "OFF" if no lecture
filename (OPTIONAL): the filename prefix for all material filepaths (if not provided, neither code nor slides are linked to)
code (OPTIONAL): if false, does not show the "Code" link for this day
slides (OPTIONAL): if false, does not show the "Slides" links for this day
notes (OPTIONAL): a list of strings to display in gray on this calendar day,
				 each on its own line.
practice (OPTIONAL): a list of length-2 lists ([PROBLEM NAME, URL]) representing that day's practice problems. 
```

Of note, `filename` is used as follows:
- the lecture PPT is assumed to be at ```{{pathToRoot}}lectures/{{filename}}/{{filename}}.pptx```
- the lecture PDF is assumed to be at ```{{pathToRoot}}lectures/{{filename}}/{{filename}}.pdf```
- the lecture code ZIP is assumed to be at ```{{pathToRoot}}lectures/{{filename}}/{{filename}}.zip```

Holidays are grayed out in the calendar.  All
information is dynamically displayed from this JSON file for each lecture,
including date, title, links to material, any HWs due, and any reading due;
lectures are also numbered automatically.

All lectures in this file are also displayed in the "Lectures" dropdown in the
navbar, up to the first lecture without a filename.  Dividers are added between
weeks.


## Compiling
To compile all references and links to test locally, from the root directory run

```
python compile.py -t --output_dir myDirectory
```

This compiles all templates in the `templates/` folder ending with .html (.ptl
files are partial templates) and, preserving its directory structure and
filenames, creates all HTML files in the given output directory.  If no output
directory is specified, the files are outputted to the ```WWW/``` directory.

To compile all references and links to host, from the root directory run

```
python compile.py --output_dir myDirectory
```

This does the same thing as the previous command, but compiles all website URLs
based on the given ```ROOT``` constant in `compile.py` instead of local paths.

You may also change any of the default compilation settings in `compile.py`,
including:

```
ROOT - the root URL for the hosted version of this website
OUTPUT_DIR - the default output directory for compiled files
TEMPLATE_DIR - the directory of templates to compile
HANDOUTS_DIR - the directory within OUTPUT_DIR containing handout PDFs
SECTION_DIR - the directory within OUTPUT_DIR containing each week's section materials
ANNOUNCEMENTS_DIR - the directory of announcements to compile
```


## Testing Locally
To host the compiled site locally, from the `WWW/` directory run

`python -m SimpleHTTPServer`

This will host the site on `localhost:8000`.  Make sure to compile using the
`-t` flag beforehand; otherwise the paths will not function properly!

