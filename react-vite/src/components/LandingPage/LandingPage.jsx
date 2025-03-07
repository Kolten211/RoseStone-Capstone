import { useEffect, useState } from "react";
import { fetchLessons } from "../../redux/lesson";
import { NavLink } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import './LandingPage.css'

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
            return lessons
        }
    })

   

    return (
        <div className="lessons-page">
        { loading ? (
            <p>Loading.....</p>
        ) : (
            <div className="lessons-container">
                <h1 className="title">Lessons</h1>
                <div className="lesson-items">
                    {filterdLessons.map(lesson => (
                        <NavLink key={lesson.id} to={`/lesson/${lesson.id}`} className="lesson-links">{lesson.title}</NavLink>
                    ))}
                </div>
            </div>
        ) }
            <p>Estos cambiarán junto con los objetivos a medida que subas de nivel!</p>
        </div>
    );
}

export default LandingPage