import React from 'react'
import logo from 'Assets/images/logo.svg'
import './navbar.scss'

class Navbar extends React.Component {
    render() {
        return (
            <nav class='navbar'>
                <div className="navbar__brand">
                    <img src={logo} alt="React Logo" className="navbar__brand__logo" />
                    <div className="navbar__brand__name">Django React Starter</div>
                </div>
            </nav>
        )
    }
}

export default Navbar;