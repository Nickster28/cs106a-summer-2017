/**
 A React component for rendering the dropdown of section materials.
 When mounted, this component fetches the JSON file at section/section.json
 to know what section materials to render.  It expects an array of date strings
 in the format YYYYMMDDHH, and will display array.length sections starting at
 section 1.  It will only display links to solutions for section i+1 if array[i]
 has passed.  In other words, array[i] represents the time after which solutions
 for section i+1 will be visible.

 This component assumes that section materials are reachable as follows:

 section/[NUM]/Section[NUM].pdf -> handout
 section/[NUM]/Section[NUM]-Solutions.pdf -> solutions PDF
 section/[NUM]/Section[NUM].zip -> solutions code
**/

class SectionDropdown extends React.Component {
	
	constructor(props) {
		super(props);
		this.state = {
			error: null,
			isLoaded: false,
			sections: []
		};
	}

	componentDidMount() {
		fetch(PATH_TO_ROOT + "section/section.json")
			.then(res => res.json())
			.then((result) => {
				this.setState({
					isLoaded: true,
					sections: result
				});
			},
			(error) => {
				this.setState({
					isLoaded: true,
					error: error
				});
			});
	}

	pastSolutionsDate(dateString) {
		let releaseDate = moment(dateString, "YYYYMMDDHH");
		return releaseDate.isSameOrBefore(moment());
	}

	render() {
		if (!this.state.isLoaded) {
			return <li><a href="#">Loading...</a></li>;
		} else if (this.state.error) {
			return <li><a href="#">Error: Cannot Load</a></li>;
		}

		// Map each section release date to the li components displaying its materials
		let sectionElements = this.state.sections.map((solutionsDate, index) => {
			const path = PATH_TO_ROOT + "section/" + (index + 1) + "/Section" + (index + 1);
			return <React.Fragment key={index}>
				<li className="dropdown-header">Section {index + 1}</li>
				<li><a href={path + ".pdf"}>Handout</a></li>
				{this.pastSolutionsDate(solutionsDate) && (
					<React.Fragment>
						<li><a href={path + "-Solutions.pdf"}>Solutions (PDF)</a></li>
						<li><a href={path + ".zip"}>Solutions (Code)</a></li>
					</React.Fragment>
				)}
				{index < this.state.sections.length - 1 && (
					<li className="divider"></li>
				)}
			</React.Fragment>
		});

		return (
			<React.Fragment>
				{sectionElements}
				<li className="divider"></li>
				<li><a style={{"textAlign": "center"}} href="https://cs198.stanford.edu/cs198/auth/default.aspx">View My Section</a></li>
				<li><a style={{"textAlign": "center"}} href="https://cs198.stanford.edu/cs198/auth/section/ViewSections.aspx?class={{courseInfo.CS198_NUMBER}}">List of all section times/locations</a></li>
				<li><a style={{"textAlign": "center"}} href="https://cs198.stanford.edu/cs198/auth/section/DropClass.aspx?class={{courseInfo.CS198_NUMBER}}">Drop Section</a></li>
			</React.Fragment>
		);
	}
}