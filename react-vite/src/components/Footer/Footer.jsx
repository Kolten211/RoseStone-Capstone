import { NavLink } from "react-router-dom";
import "./Footer.css"


function FooterNavigation() {
    return (
      <nav className="foot_nav">
        <ul className="nav-contents">
            <NavLink to="letters-page" className='letters'>Alphabet</NavLink>
            <NavLink to="/dictionary">DICT</NavLink>
            <NavLink to="/translate">translate</NavLink>
        </ul>
      </nav>
    );
}

export default FooterNavigation