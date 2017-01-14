var React = require('react');
var AuthForm = require('AuthForm');
var Token = require('Token');
var degreeAuditAuth = require('degreeAuditAuth');
var degreeAuditFetch = require('degreeAuditFetch');
var FetchForm = require('FetchForm');
var Courses = require('Courses');

var Auth = React.createClass({
    getInitialState: function() {
        return {
            isLoading: false
        }
    },
    handleAuth: function(username, password) {
        var that = this;
        this.setState({
            isLoading: true
        });

        degreeAuditAuth.getToken(username,password).then(function (token) {
            that.setState({
                token: token,
                username: username,
                password: password,
                isLoading: false
            });
        }, function (errorMessage) {
            alert(errorMessage);
            that.setState({
                isLoading: false,
                token: "",
                username: "",
                password: ""
            });
        });
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
                token: "",
                gpa: "",
                courses: ""
            });
        });
    },
    
    render: function() {
        var {isLoading, username, password, token, courses, gpa} = this.state;

        function renderMessage () {
            if (isLoading) {
                return <h3>Fetching token...</h3>;
            } else if (token && !(courses && gpa) ) {
                return (
                    <div>
                        <Token token={token}/>
                    </div>
                )
            } else if ((courses && gpa)) {
                console.log(gpa);
                console.log(courses);
                return (
                    <div>
                        <Courses gpa={gpa} courses={courses}/>
                    </div>
                )
            } else {
                <h1>Hi</h1>
            }
        }

        return (
            <div>
                <AuthForm onAuth={this.handleAuth}/>
                <FetchForm onFetch={this.handleFetch}/>
                {renderMessage()}
            </div>
        );
    }
});

module.exports = Auth;