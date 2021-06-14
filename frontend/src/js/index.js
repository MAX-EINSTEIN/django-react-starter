import React from 'react';
import ReactDOM from 'react-dom';

class App extends React.Component {
    render() {
        return (
            <div className="container">
                <div className="content">
                    <h1>Django React Starter</h1> <br />
                    <h4><strong> Rendered by: React </strong> </h4>
                </div>
            </div>
        )
    }
}

ReactDOM.render(<App />, document.getElementById('react-app'));