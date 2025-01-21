import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { fetchLessonDetails } from '../../redux/lesson';


function LessonDetails() {
    const { lesson_id } = useParams();
    const dispatch = useDispatch();
    const [lesson, setlesson] = useState(null)
    const [showTest, setShowTest] = useState(false)

    useEffect(() => {
        dispatch(fetchLessonDetails
            (lesson_id))
    }, []);

    

    const handleStart = () => {
        
    }

    console.log("Am i understanding you", lesson)
    

    return (
        <>
            <h2>{lesson.title}</h2>
            <p>Created by: {lesson.user_id}</p>
            <p>Difficulty: {lesson.difficulty}</p>
            <p>Description: {lesson.description}</p>
            <h3>Words</h3>
            <ul>
                {lesson.words.map((word) => (
                    <li key={word.id}>{word.word}</li>
                ))}
            </ul>
            <h3>Phrases</h3>
            <ul>
                {lesson.phrases.map((phrase) => (
                    <li key={phrase.id}>{phrase.phrase}</li>
                ))}
            </ul>
        </>
    )
}


export default LessonDetails