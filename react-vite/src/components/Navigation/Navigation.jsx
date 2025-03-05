import { NavLink } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import "./Navigation.css";

function Navigation() {
  return (
    <nav className="nav">
      <ul className="nav-contents">
        <li className="icon">
          <NavLink to="/profile-page" className='home'>Home</NavLink>
        </li>
        <li>
          <ProfileButton />
        </li>
      </ul>
    </nav>
  );
}

export default Navigation;
