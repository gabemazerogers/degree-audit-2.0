var React = require('React');
var CourseMessages = require('CourseMessages');
var FetchForm = require('FetchForm');
var degreeAuditFetch = require('degreeAuditFetch');

var Course = React.createClass({
    getInitialState: function() {
        return {
            isLoading: false
        }
    },
    handleFetch: function(token) {
        var that = this;
        this.setState({
            isLoading: true
        });

        degreeAuditFetch.getCourses(token).then(function (degreeAuditJSON) {
            var parsedJSON = JSON.parse(degreeAuditJSON); 
            var gpa = (parsedJSON.GPA).toString();
            var courses = JSON.stringify(parsedJSON.courses);
            that.setState({
                isLoading: false,
                gpa: gpa,
                courses: courses
            });
        }, function (errorMessage) {
            alert(errorMessage);
            that.setState({
                isLoading: false,
                gpa: "",
                courses: ""
            });
        });
    },

    render: function() {
        var {isLoading, courses, gpa} = this.state;

        function renderMessage () {
            if (isLoading) {
                return <h3>Fetching courses...</h3>;
            } else if (courses && gpa) {
                return (
                  <div>
                        <CourseMessages gpa={gpa} courses={courses}/>
                  </div>
                )
            }
        }

        return (
            <div>
                <FetchForm onFetch={this.handleFetch}/>
                {renderMessage()}
            </div>
        );
    }
});

module.exports = Course;