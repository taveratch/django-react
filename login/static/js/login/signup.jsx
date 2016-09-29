import React from 'react';

class Signup extends React.Component {
  render() {
    return (
      <form action="/login/api/signup/" method="post">
        <h1>Sign up</h1>
        <div hidden dangerouslySetInnerHTML={{__html: this.props.token}}></div>
        <div>
          <input name="email" placeholder="Email"/>
          <input name="password" placeholder="Password"/>
          <input name="confirm-password" placeholder="Confirm password"/>
          <input type="submit" value="Submit" />
        </div>
      </form>
    );
  }
}

export default Signup;
