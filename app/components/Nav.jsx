var React = require('react');
var {Link, IndexLink} = require('react-router');

var Nav = React.createClass({
    render: function () {
        return (
            <div>
                <IndexLink to="/" activeClassName="active" activeStyle={{fontWeight: 'bold'}}>Courses</IndexLink>
                <Link to="/token" activeClassName="active" activeStyle={{fontWeight: 'bold'}}>Get Token</Link>
            </div>
        );
    }
});

module.exports = Nav;