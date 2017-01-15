var React = require('react');

var FetchForm = React.createClass({
    onFormSubmit: function(e) {
        e.preventDefault();
        console.log(this.refs.tokenField.value);
        var token = this.refs.tokenField.value;

        if (token.length > 0) {
            this.refs.tokenField.value = '';
            this.props.onFetch(token);
        }
    },
    render: function() {
        return (
            <div>
                <form onSubmit={this.onFormSubmit}>
                    <input type="text" placeholder="API Token" ref="tokenField"/>
                    <button>Fetch</button>
                </form>
            </div>
        )
    }
});

module.exports = FetchForm;