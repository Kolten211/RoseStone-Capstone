import { NavLink } from "react-router-dom"
import "./GreetingPage.css"
function Greeting() {
    return (
        <div className="Greeting-container">
            <div className>
                <h1 className="Greeting-title">Hola amigos, ¡espero que estén bien!</h1>
            </div>
            <h1 className="Greeting-title">Te damos la bienvenida a Rose</h1>
            <div className="click-me">
                <h2 className="Greeting-title">Aquí puedes ver la lista de todas las lecciones.</h2>
                <NavLink to='/landing-page' className='nav-link'>Click Me!</NavLink>
            </div>
        </div>
    )
}
export default Greeting