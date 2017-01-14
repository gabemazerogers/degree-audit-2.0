var React = require('react');
var Course = require('Course');
// var {Card, CardActions, CardHeader, CardText} = require('material-ui/Card');
// var FlatButton = require('material-ui/FlatButton');


var Courses = React.createClass({
    render: function () {
        var SPLIT_CHAR = '@';
        var {courses, gpa} = this.props;

        var courseArray = stringToArray(courses, SPLIT_CHAR);
        var courseArrayJSON = courseArray.map(function(courseString) {
            return JSON.parse(courseString);
        })

        //TODO: Implement a better way of displaying the grades.
        return (
            <div>
                <h3>{gpa.toString()}</h3>
                    {courseArrayJSON.map(function(object, i){
                     return (
                        <Course grade={object.grade} 
                                course={object.course} 
                                units={object.units} 
                                quarter={object.quarter} 
                                key={i}/>
                     );
                })}
            </div>
        );
    }
});

module.exports = Courses;

/**
 * Seperates Array as a string input, and returns it as an Array
 */
function stringToArray(inString, SPLIT_CHAR) {
    var modifiedString = inString.substring(1, inString.length-1);

    // Function from StackOverflow to have a replace all in string functionality
    String.prototype.replaceAll = function(search, replacement) {
        var target = this;
        return target.replace(new RegExp(search, 'g'), replacement);
    };

    modifiedString = modifiedString.replaceAll("},",`}${SPLIT_CHAR}`);
    var splitString = modifiedString.split(SPLIT_CHAR);

    return splitString;
}