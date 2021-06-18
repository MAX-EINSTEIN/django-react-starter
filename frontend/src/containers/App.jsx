import React from 'react';
import Navbar from '../components/navbar/Navbar';
import './app.scss';

class App extends React.Component {
    render() {
        return (
            <div className="container">
                <Navbar />
                <div className="content">
                    <h1>Django React Starter</h1> <br />
                    <h4><strong>Rendered by: React </strong> </h4>
                </div>
            </div>
        )
    }
}

export default App;
