import { useEffect, useState } from "react";
import { fetchLessons } from "../../redux/lesson";
import { NavLink } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";

const LandingPage = () => {
    const dispatch = useDispatch();
    const [loading, setLoading] = useState(true)
    

   

    useEffect(() => {
        dispatch(fetchLessons())
        .then(() => setLoading(false))
        .catch(() => setLoading(false))
    }, []);

    const lessons = useSelector((state) => state.lesson);
    console.log("Lesson", lessons)
    const lessonIndex = lessons[0]
    console.log('INdex', lessonIndex)
    const user = useSelector(state => state.session.user)
    console.log("user", user)
   
    

    const filterdLessons = lessons?.filter((lesson) => {
        if (user && user.level === 'Beginner') {
            return lesson.difficulty === 'Beginner';
        } else if (user && user.level === 'Intermediate') {
            return lesson.difficulty === 'Intermediate'
        } else {
            return false
        }
    })

   

    return (
        <div>
        { loading ? (
            <p>Loading.....</p>
        ) : (
            <div>
                <ul>
                    {filterdLessons.map(lesson => (
                        <li key={lesson.id}>
                            <NavLink to={`/lesson/${lesson.id}`}>{lesson.title}</NavLink>
                        </li>
                    ))}
                </ul>
            </div>
        ) }
            <p>Estos cambiarán junto con los objetivos a medida que subas de nivel!</p>
        </div>
    );
}

export default LandingPage