var React = require('react');
var ReactDOM = require('react-dom');
var {Route, Router, IndexRoute, hashHistory} = require('react-router');
var Auth = require('Auth');
var Course = require('Course');
var Main = require('Main');

ReactDOM.render(
  <Router history={hashHistory}>
    <Route path="/" component={Main}>
      <Route path="token" component={Auth}/>
      <IndexRoute component={Course}/>
    </Route>
  </Router>,
  document.getElementById('app')
);
