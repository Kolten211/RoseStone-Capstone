import { useEffect } from "react";
import { fetchLessons } from "../../redux/lesson";
import { Link } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";

const LandingPage = () => {
    const dispatch = useDispatch();
    const lessons = useSelector((state) => state.lessons);

    useEffect(() => {
        dispatch(fetchLessons())
    }, []);
    
    return (
        <div>
            <div>
                <h1>Hola amigos, ¡espero que estén bien!</h1>
            </div>
            <div>
                <h2>Aquí puedes ver la lista de todas las lecciones.</h2>
            </div>
            <div>
                <ul>
                    {lessons.map((lesson) => (
                        <li key={lesson.id}>
                            <Link to={`/lessons/${lessons.id}`}>{lesson.id}</Link>
                        </li>
                    ))}
                </ul>
            </div>
            <p>Estos cambiarán junto con los objetivos a medida que subas de nivel!</p>
        </div>
    )
}

export default LandingPage