import { NavLink } from "react-router-dom"
import "./GreetingPage.css"
function Greeting() {
    return (
        <>
            <div>
                <h1>Hola amigos, ¡espero que estén bien!</h1>
            </div>
            <h1>Te damos la bienvenida a Rose</h1>
            <div>
                <h2>Aquí puedes ver la lista de todas las lecciones.</h2>
                <NavLink to='/landing-page' className='nav-link'>Click Me!</NavLink>
            </div>
        </>
    )
}
export default Greeting