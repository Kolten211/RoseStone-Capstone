import { NavLink } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import "./Navigation.css";

function Navigation() {
  return (
    <nav className="nav">
      <ul className="nav-contents">
        <li className="icon">
          <NavLink to="/profile-page" className='home'>
          <img src="https://res.cloudinary.com/dozliephp/image/upload/v1741296002/Untitled_ksb0ig.png" alt="Rose" className="logo"/>
          </NavLink>
        </li>
        <li>
          <h1 className="the-title">ROSE</h1>
        </li>
        <li>
          <ProfileButton />
        </li>
      </ul>
    </nav>
  );
}

export default Navigation;
