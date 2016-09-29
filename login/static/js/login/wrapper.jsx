import React from 'react';
import Signin from './signin.jsx';
class Wrapper extends React.Component {
	render() {
    var token = <div hidden dangerouslySetInnerHTML={{__html: this.props.token}}></div>;
		return (
      <Signin token={token}/>
		);
	}
}
export default Wrapper;
