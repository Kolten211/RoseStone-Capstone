
import {  useSelector } from "react-redux";
import { NavLink } from "react-router-dom";
import './ProfilePAge.css'



function ProfilePage() {
    
   
   const user = useSelector((store) => store.session.user)

   console.log("You have the right info", user)


   return (
    <div className="user-info">
        <h1 className="title">Perfil de usuario</h1>
        <div className="username">
            <label>Username
                <h3>{user.username}</h3>
            </label>
        </div>
        <div className="level">
            <label>Level
                <h3>{user.level}</h3>
            </label>
        </div>
        <div className="score">
            <label>Score
                <h3>{user.score}/1000</h3>
            </label>
        </div>
        <div className="links">
            <NavLink to='/learned-words' className="learned-link">Palabras aprendidas</NavLink>
            <NavLink to='/learned-phrases' className="phrase-link">La Frase</NavLink>
            <NavLink to='/phrase-builder' className="phrase-link">Generador de oraciones</NavLink>
        </div>
    </div>
   )
}
export default ProfilePage