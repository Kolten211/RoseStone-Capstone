
import {  useSelector } from "react-redux";
import { NavLink } from "react-router-dom";



function ProfilePage() {
    
   
   const user = useSelector((store) => store.session.user)

   console.log("You have the right info", user)


   return (
    <div>
        <h1>Perfil de usuario</h1>
        <label>Username
            <h2>{user.username}</h2>
        </label>
        <label>Level
            <h3>{user.level}</h3>
        </label>
        <label>Score
            <h3>{user.score}/1000</h3>
        </label>
        <div>
            <NavLink to='/learned-words'>Palabras aprendidas</NavLink>
        </div>
    </div>
   )
}
export default ProfilePage