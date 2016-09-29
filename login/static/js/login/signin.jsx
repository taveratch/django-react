import React from 'react';

class Signin extends React.Component {
  render() {
    return (
      <form action="/login/api/signin/" method="post">
        <h1>Sign in</h1>
        <div hidden dangerouslySetInnerHTML={{__html: this.props.token}}></div>
        <div>
          <input name="email"/>
          <input name="password"/>
          <input type="submit" value="Submit" />
        </div>
      </form>
    );
  }
}

export default Signin;
