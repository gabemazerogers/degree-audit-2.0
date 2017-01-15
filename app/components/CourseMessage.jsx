var React = require('react');

var CourseMessage = React.createClass({
    render: function() {
        var {grade, course, units, quarter} = this.props;
        return (

            <div>
                <h3><span>          
                Grade: {grade},
                Course: {course},
                Units: {units},
                Quarter: {quarter}
                </span> </h3>
            </div>
        );
    }
})

module.exports = CourseMessage;